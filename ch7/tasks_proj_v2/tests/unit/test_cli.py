from contextlib import contextmanager
import pytest
from click.testing import CliRunner
import tasks.cli
import tasks.config
from tasks.api import Task


@contextmanager
def stub_tasks_db():
    yield


def test_list_no_args(mocker):
    # Replace the _tasks_db() context manager with our stub that does nothing.
    mocker.patch.object(tasks.cli, "_tasks_db", new=stub_tasks_db)

    # Replace any calls to tasks.list_tasks() from within tasks.cli to a default
    # MagicMock object with a return value of an empty list.
    mocker.patch.object(tasks.cli.tasks, "list_tasks", return_value=[])

    # Use the Click CliRunner to do the same thing as calling tasks list on the command
    # line.
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ["list"])

    # Use the mock object to make sure the API call was called correctly.
    # assert_called_once_with() is part of unittest.mock.Mock objects.
    tasks.cli.tasks.list_tasks.assert_called_once_with(None)


@pytest.fixture()
def no_db(mocker):
    """Put the mock stubbing of _tasks_db into a fixture so we can reuse it more easily
    in future tests."""
    mocker.patch.object(tasks.cli, "_tasks_db", new=stub_tasks_db)


def test_list_print_empty(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, "list_tasks", return_value=[])
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ["list"])
    expected_output = (
        "  ID      owner  done summary\n" "  --      -----  ---- -------\n"
    )

    # Check the output of the command-line action
    assert result.output == expected_output


def test_list_print_many_items(no_db, mocker):
    many_tasks = (
        Task("write chapter", "Brian", True, 1),
        Task("edit chapter", "Katie", False, 2),
        Task("modify chapter", "Brian", False, 3),
        Task("finalize chapter", "Katie", False, 4),
    )
    mocker.patch.object(tasks.cli.tasks, "list_tasks", return_value=many_tasks)
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ["list"])
    expected_output = (
        "  ID      owner  done summary\n"
        "  --      -----  ---- -------\n"
        "   1      Brian  True write chapter\n"
        "   2      Katie False edit chapter\n"
        "   3      Brian False modify chapter\n"
        "   4      Katie False finalize chapter\n"
    )
    assert result.output == expected_output


def test_list_dash_o(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, "list_tasks")
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ["list", "-o", "brian"])
    tasks.cli.tasks.list_tasks.assert_called_once_with("brian")


def test_list_dash_dash_owner(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, "list_tasks")
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ["list", "--owner", "okken"])
    tasks.cli.tasks.list_tasks.assert_called_once_with("okken")
