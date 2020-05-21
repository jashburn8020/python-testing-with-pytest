# Python Testing with pytest

- [Python Testing with pytest](#python-testing-with-pytest)
  - [1. Getting Started with pytest](#1-getting-started-with-pytest)
    - [Using Options](#using-options)
  - [2. Writing Test Functions](#2-writing-test-functions)
    - [Testing a Package](#testing-a-package)
      - [Installing a Package Locally](#installing-a-package-locally)
    - [Using `assert` Statements](#using-assert-statements)
    - [Expecting Exceptions](#expecting-exceptions)
    - [Marking Test Functions](#marking-test-functions)
    - [Skipping Tests](#skipping-tests)
    - [Marking Tests as Expecting to Fail](#marking-tests-as-expecting-to-fail)
    - [Running a Subset of Tests](#running-a-subset-of-tests)
      - [A Single Directory](#a-single-directory)
      - [A Single Test File/Module](#a-single-test-filemodule)
      - [A Single Test Function](#a-single-test-function)
      - [A Single Test Class](#a-single-test-class)
      - [A Single Test Method of a Test Class](#a-single-test-method-of-a-test-class)
      - [A Set of Tests Based on Test Name](#a-set-of-tests-based-on-test-name)
    - [Parametrized Testing](#parametrized-testing)
      - [One Parameter](#one-parameter)
      - [Multiple Parameters](#multiple-parameters)
      - [Arguments Assigned to a Variable](#arguments-assigned-to-a-variable)
      - [`ids` Optional Parameter to Make Our Own Identifiers](#ids-optional-parameter-to-make-our-own-identifiers)
      - [`parametrize()` on Classes](#parametrize-on-classes)
      - [Identify Parameters with an `id`](#identify-parameters-with-an-id)
  - [3. pytest Fixtures](#3-pytest-fixtures)
    - [Sharing Fixtures Through conftest.py](#sharing-fixtures-through-conftestpy)
    - [Using Fixtures for Setup and Teardown](#using-fixtures-for-setup-and-teardown)
    - [Tracing Fixture Execution with `--setup-show`](#tracing-fixture-execution-with---setup-show)
    - [Using Fixtures for Test Data](#using-fixtures-for-test-data)
    - [Using Multiple Fixtures](#using-multiple-fixtures)
    - [Specifying Fixture Scope](#specifying-fixture-scope)
    - [Specifying Fixtures with usefixtures](#specifying-fixtures-with-usefixtures)
    - [Using `autouse` for Fixtures That Always Get Used](#using-autouse-for-fixtures-that-always-get-used)
    - [Renaming Fixtures](#renaming-fixtures)
    - [Parametrizing Fixtures](#parametrizing-fixtures)
  - [4. Builtin Fixtures](#4-builtin-fixtures)
    - [Using `tmpdir` and `tmpdir_factory`](#using-tmpdir-and-tmpdir_factory)
    - [Using `pytestconfig`](#using-pytestconfig)
    - [Using `cache`](#using-cache)
    - [Using `capsys`](#using-capsys)
    - [Using `monkeypatch`](#using-monkeypatch)
    - [Using `doctest_namespace`](#using-doctest_namespace)
    - [Using `recwarn`](#using-recwarn)
  - [5.Plugins](#5plugins)
    - [Finding Plugins](#finding-plugins)
    - [Installing Plugins](#installing-plugins)
      - [Install from PyPI](#install-from-pypi)
      - [Install from a .tar.gz or .whl](#install-from-a-targz-or-whl)
      - [Install from a Local Directory](#install-from-a-local-directory)
      - [Install from a Git Repository](#install-from-a-git-repository)
    - [Writing Your Own Plugins](#writing-your-own-plugins)
    - [Creating an Installable Plugin](#creating-an-installable-plugin)
    - [Testing Plugins](#testing-plugins)
    - [Creating a Distribution](#creating-a-distribution)
      - [Distributing Plugins Through a Shared Directory](#distributing-plugins-through-a-shared-directory)
      - [Distributing Plugins Through PyPI](#distributing-plugins-through-pypi)
  - [6. Configuration](#6-configuration)
    - [Understanding pytest Configuration Files](#understanding-pytest-configuration-files)
    - [Changing the Default Command-Line Options](#changing-the-default-command-line-options)
    - [Registering Markers to Avoid Marker Typos](#registering-markers-to-avoid-marker-typos)
    - [Requiring a Minimum pytest Version](#requiring-a-minimum-pytest-version)
    - [Stopping pytest from Looking in the Wrong Places](#stopping-pytest-from-looking-in-the-wrong-places)
    - [Specifying Test Directory Locations](#specifying-test-directory-locations)
    - [Changing Test Discovery Rules](#changing-test-discovery-rules)
    - [Disallowing XPASS](#disallowing-xpass)
    - [Avoiding Filename Collisions](#avoiding-filename-collisions)
  - [7. Using pytest with Other Tools](#7-using-pytest-with-other-tools)
    - [pdb: Debugging Test Failures](#pdb-debugging-test-failures)
    - [Coverage.py: Determining How Much Code Is Tested](#coveragepy-determining-how-much-code-is-tested)
    - [mock: Swapping Out Part of the System](#mock-swapping-out-part-of-the-system)
    - [tox: Testing Multiple Configurations](#tox-testing-multiple-configurations)
  - [A3. Plugin Sampler Pack](#a3-plugin-sampler-pack)
    - [Plugins That Change the Normal Test Run Flow](#plugins-that-change-the-normal-test-run-flow)
      - [pytest-repeat: Run Tests More Than Once](#pytest-repeat-run-tests-more-than-once)
      - [pytest-xdist: Run Tests in Parallel](#pytest-xdist-run-tests-in-parallel)
      - [pytest-timeout: Put Time Limits on Your Tests](#pytest-timeout-put-time-limits-on-your-tests)
    - [Plugins That Alter or Enhance Output](#plugins-that-alter-or-enhance-output)
      - [pytest-instafail: See Details of Failures and Errors as They Happen](#pytest-instafail-see-details-of-failures-and-errors-as-they-happen)
      - [pytest-sugar: Instafail + Colors + Progress Bar](#pytest-sugar-instafail--colors--progress-bar)
      - [pytest-emoji: Add Some Fun to Your Tests](#pytest-emoji-add-some-fun-to-your-tests)
      - [pytest-html: Generate HTML Reports for Test Sessions](#pytest-html-generate-html-reports-for-test-sessions)
    - [Plugins for Static Analysis](#plugins-for-static-analysis)
      - [pytest-pycodestyle, pytest-pep8: Comply with Python's Style Guide](#pytest-pycodestyle-pytest-pep8-comply-with-pythons-style-guide)
      - [pytest-flake8: Check for Style Plus Linting](#pytest-flake8-check-for-style-plus-linting)
    - [Plugins for Web Development](#plugins-for-web-development)
      - [pytest-selenium: Test with a Web Browser](#pytest-selenium-test-with-a-web-browser)
      - [pytest-django: Test Django Applications](#pytest-django-test-django-applications)
      - [pytest-flask: Test Flask Applications](#pytest-flask-test-flask-applications)
  - [A4. Packaging and Distributing Python Projects](#a4-packaging-and-distributing-python-projects)
    - [Creating an Installable Module](#creating-an-installable-module)
    - [Creating an Installable Package](#creating-an-installable-package)
    - [Creating a Source Distribution and Wheel](#creating-a-source-distribution-and-wheel)
  - [Sources](#sources)

## 1. Getting Started with pytest

```console
​$ pytest --help​
usage: pytest [options] [file_or_dir] [file_or_dir] [...]
...
```

- Given no arguments, pytest looks at your current directory and all subdirectories for test files and runs the test code it finds
- If you give pytest a filename, a directory name, or a list of those, it looks there instead of the current directory
- Each directory listed on the command line is recursively traversed to look for test code
- The part of pytest execution where pytest goes off and finds which tests to run is called _test discovery_
- Naming conventions to keep your test code discoverable:
  - test files: `test_<something>.py` or `<something>_test.py`
  - test methods and functions: `test_<something>`
  - test classes: `Test<Something>`
- There are ways to alter these discovery rules
  - see: _Configuration_
- Running only one test:
  - `pytest <directory>/<file.py>::<test_name>`
  - e.g., `pytest tasks/test_four.py::test_asdict`

### Using Options

- Some useful pytest command line options
- `--collect-only`
  - shows you which tests will be run with the given options and configuration
  - e.g., when used in conjunction with `-k`
- `-k`
  - use an expression to find what test functions to run
  - e.g., `pytest -k "asdict or defaults"`
    - run the `test_asdict()` and `test_defaults()` tests
- `-m MARKEXPR`
  - markers allow you to mark a subset of your test functions so that they can be run together
  - e.g., `pytest -m run_these_please`
    - will run tests with the `@pytest.mark.run_these_please` marker
  - further examples:
    - `-m "mark1 and mark2"`
    - `-m "mark1 and not mark2"`
    - `-m "mark1 or mark2"`
- `-x, --exitfirst`
  - stop the entire test session immediately when a test fails
  - useful when debugging a problem
- `-s` and `--capture=method`
  - `-s` flag allows anything that normally would be printed to stdout to actually be printed to stdout while the tests are running
    - shortcut for `--capture=no`
  - example: without and with `-s`:

```python
def test_fail():
    a = 1
    print("--- a is " + str(a))
    assert a == 2
```

```console
$ pytest
====================== test session starts =======================
...
collected 1 item

tests/test_s_option.py F                                   [100%]

============================ FAILURES ============================
___________________________ test_fail ____________________________

    def test_fail():
        a = 1
        print("--- a is " + str(a))
>       assert a == 2
E       assert 1 == 2

tests/test_s_option.py:4: AssertionError
---------------------- Captured stdout call ----------------------
--- a is 1
==================== short test summary info =====================
FAILED tests/test_s_option.py::test_fail - assert 1 == 2
======================= 1 failed in 0.02s ========================

$ pytest -s
====================== test session starts =======================
...
collected 1 item

tests/test_s_option.py --- a is 1
F

============================ FAILURES ============================
___________________________ test_fail ____________________________

    def test_fail():
        a = 1
        print("--- a is " + str(a))
>       assert a == 2
E       assert 1 == 2

tests/test_s_option.py:4: AssertionError
==================== short test summary info =====================
FAILED tests/test_s_option.py::test_fail - assert 1 == 2
======================= 1 failed in 0.02s ========================
```

- `-lf`, `--last-failed`
  - when one or more tests fails, run just the failing tests
  - helpful for debugging
- `-ff`, `--failed-first`
  - run all tests but run the last failures first
- `-v`, `--verbose`
  - report more information than without it
- `-q`, `--quiet`
  - opposite of `-v`/`--verbose`
  - decrease the information reported
- `-l`, `--showlocals`
  - local variables and their values are displayed with tracebacks for failing tests
- `--tb=style`
  - modify the way tracebacks for failures are output
  - useful styles:
    - `short`: prints just the `assert` line and the `E` evaluated line with no context
    - `line`: keep the failure to one line
    - `no`: remove the traceback entirely
- `--durations=N`
  - report the slowest N number of tests/setups/teardowns after the tests run
  - `--durations=0` reports everything in order of slowest to fastest

## 2. Writing Test Functions

### Testing a Package

- File structure for the Tasks project:

```text
​tasks_proj/
​├── CHANGELOG.rst
​├── LICENSE
​├── MANIFEST.in
​├── README.rst
​├── setup.py
​├── src
│   └── tasks
​│       ├── __init__.py
​│       ├── api.py
​│       ├── cli.py
​│       ├── config.py
​│       ├── tasksdb_pymongo.py
​│       └── tasksdb_tinydb.py
​└── tests
​    ├── conftest.py
​    ├── pytest.ini
​    ├── func
​    │   ├── __init__.py
​    │   ├── test_add.py
​    │   └── ...
​    └── unit
​        ├── __init__.py
​        ├── test_task.py
​        └── ...
```

- All of the tests are kept in `tests` and separate from the package source files in `src`
  - not a requirement of pytest, but a best practice
- Functional (`func`) and unit (`unit`) tests are separated into their own directories
  - allows you to easily run a subset of tests
    - functional tests should only break if we are intentionally changing functionality of the system
    - unit tests could break during a refactoring or an implementation change
- Two types of `__init__.py` files
  - under the `src/` directory
    - `src/tasks/__init__.py` tells Python that the directory is a package
    - acts as the main interface to the package when someone uses `import tasks`
    - contains code to import specific functions from `api.py`
      - `cli.py` and our test files can access package functionality like `tasks.add()` instead of having to do `tasks.api.add()`
  - under `tests/`
    - `tests/func/__init__.py` and `tests/unit/__init__.py` files are empty
      - tell pytest to go up one directory to look for the root of the test directory and to look for the `pytest.ini` file
- `pytest.ini`
  - optional
  - contains project-wide pytest configuration, at most only one of these in your project
    - directives that change the behaviour of pytest
    - e.g., a list of options that will always be used
- `conftest.py`
  - optional
  - considered by pytest as a "local plugin" and can contain hook functions and fixtures
  - hook functions
    - a way to insert code into part of the pytest execution process to alter how pytest works
  - fixtures
    - setup and teardown functions that run before and after test functions
    - can be used to represent resources and data used by the tests
  - hook functions and fixtures that are used by tests in multiple subdirectories should be contained in `tests/conftest.py`
  - can have multiple `conftest.py` files
    - e.g., you can have one at `tests` and one for each subdirectory under `tests`

#### Installing a Package Locally

- The best way to allow the tests to be able to `import tasks` or `from tasks import something` is to install `tasks` locally using pip
  - possible because there's a [`setup.py`](tasks_proj/setup.py) file present to direct pip
- Install `tasks` either by running `pip install .` or `pip install -e .` from the `tasks_proj` directory
  - or you can run `pip install -e tasks_proj` from one directory up
  - `-e, --editable <path/url>`: Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url
    - be able to modify the source code while `tasks` is installed
- Run tests:

```console
​$ cd /path/to/code/ch2/tasks_proj/tests/unit​
$ pytest test_task.py​
```

### Using `assert` Statements

- The normal Python `assert` statement is your primary tool to communicate test failure
- The following is a list of a few of the `assert` forms and `assert` helper functions:

| pytest             | unittest                |
| ------------------ | ----------------------- |
| `assert something` | `assertTrue(something)` |
| `assert a == b`    | `assertEqual(a, b)`     |
| `assert a <= b`    | `assertLessEqual(a, b)` |

- You can use `assert <expression>` with any expression
  - if the expression would evaluate to `False` if converted to a `bool`, the test would fail
- pytest includes a feature called `assert` rewriting that intercepts `assert` calls and replaces them with something that can tell you more about why your assertions failed

```console
$ pytest test_task_fail.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /.../ch2/tasks_proj/tests, inifile: pytest.ini
collected 2 items

test_task_fail.py FF                                                     [100%]

=================================== FAILURES ===================================
______________________________ test_task_equality ______________________________

    def test_task_equality():
        """Different tasks should not be equal."""
        t1 = Task('sit there', 'brian')
        t2 = Task('do something', 'okken')
>       assert t1 == t2
E       AssertionError: assert Task(summary=...alse, id=None) == Task(summary=...alse, id=None)
E         At index 0 diff: 'sit there' != 'do something'
E         Use -v to get the full diff

test_task_fail.py:9: AssertionError
______________________________ test_dict_equality ______________________________
...
```

- See:
  - [`unit/test_task_fail.py`](ch2/tasks_proj/tests/unit/test_task_fail.py)
  - [Demo of Python failure reports with pytest](https://docs.pytest.org/en/latest/example/reportingdemo.html)

### Expecting Exceptions

- Check for the type of exception
  - use the wrong type in a test function to intentionally cause `TypeError` exceptions, and use **`with pytest.raises(<expected exception>)`**

```python
def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")
```

- Check the parameters to the exception
  - you can check to make sure the exception message is correct by adding **`as excinfo`**

```python
def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db("some/great/path", "mysql")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
```

- See: [`func/test_api_exceptions.py`](ch2/tasks_proj/tests/func/test_api_exceptions.py)

### Marking Test Functions

- A test can have more than one marker, and a marker can be on multiple tests
- E.g., to add a smoke test suite to the Tasks project, we can add **`@mark.pytest.smoke`** to some of the tests

```python
@pytest.mark.smoke
def test_list_raises():
    """One marker: 'smoke'"""
    ...


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """Two markers: 'get' and 'smoke'"""
    ...
```

- Run just those tests that are marked with **`-m marker_name`**

```console
$ pytest -v -m 'smoke or get' test_api_exceptions.py

============================= test session starts ==============================
...
collected 7 items / 5 deselected / 2 selected

test_api_exceptions.py::test_list_raises PASSED                          [ 50%]
test_api_exceptions.py::test_get_raises PASSED                           [100%]
```

### Skipping Tests

- pytest includes a few helpful builtin markers: `skip`, `skipif`, and `xfail`
- `skip` and `skipif` markers enable you to skip tests you don't want to run
- **`skip`**
  - see: [`func/test_unique_id_2.py`](ch2/tasks_proj/tests/func/test_unique_id_2.py)

```python
@pytest.mark.skip(reason="misunderstood the API")
def test_unique_id_1():
    """s (skipped)"""
    ...
```

```console
$ pytest test_unique_id_2.py
============================= test session starts ==============================
...
collected 2 items

test_unique_id_2.py s.                                                   [100%]

========================= 1 passed, 1 skipped in 0.48s =========================
```

- **`skipif`**
  - let's say we decide the test should be valid, and we intend to make that work in version 0.2.0 of the package
  - the expression we pass into `skipif()` can be any valid Python expression
  - see: [`func/test_unique_id_3.py`](ch2/tasks_proj/tests/func/test_unique_id_3.py)

```python
@pytest.mark.skipif(
    tasks.__version__ < "0.2.0", reason="not supported until version 0.2.0"
)
def test_unique_id_1():
    """s (skipped): skipped because we're currently at version 0.1.0"""
    ...
```

```console
$ pytest -r s test_unique_id_3.py
============================= test session starts ==============================
...
collected 2 items

test_unique_id_3.py s.                                                   [100%]

=========================== short test summary info ============================
SKIPPED [1] func/test_unique_id_3.py:8: not supported until version 0.2.0
========================= 1 passed, 1 skipped in 0.31s =========================
```

- **`reason`**
  - not required in `skip`, but it is required in `skipif`
  - show skip reason in test output with `pytest -r s`

```console
  -r chars              show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. (w)arnings are enabled by default (see
                        --disable-warnings), 'N' can be used to reset the list.
                        (default: 'fE').
```

### Marking Tests as Expecting to Fail

- With the **`xfail`** marker, we are telling pytest to run a test function, but that we expect it to fail
- See: [`func/test_unique_id_4.py`](ch2/tasks_proj/tests/func/test_unique_id_4.py)

```python
@pytest.mark.xfail(
    tasks.__version__ < "0.2.0", reason="not supported until version 0.2.0"
)
def test_unique_id_1():
    """x (xfail): expected to fail"""
    ...


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """x (xfail): expected to fail"""
    ...


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """X (xpass): expected to fail but passed """
    ...
```

```console
$ pytest -r sxX test_unique_id_4.py
============================= test session starts ==============================
...
collected 4 items

test_unique_id_4.py xxX.                                                 [100%]

=========================== short test summary info ============================
XFAIL test_unique_id_4.py::test_unique_id_1
  not supported until version 0.2.0
XFAIL test_unique_id_4.py::test_unique_id_is_a_duck
XPASS test_unique_id_4.py::test_unique_id_not_a_duck
=================== 1 passed, 2 xfailed, 1 xpassed in 0.43s ====================
```

- You can configure pytest to report the tests that pass but were marked with `xfail` to be reported as `FAIL`
  - done in a `pytest.ini` file:

```ini
[pytest]
xfail_strict=true
```

### Running a Subset of Tests

#### A Single Directory

- To run all the tests from one directory, use the directory as a parameter to pytest
  - `​pytest tests/func`

```console
$ pytest --disable-warnings -v tests/func
============================= test session starts ==============================
...
collected 50 items

tests/func/test_add.py::test_add_returns_valid_id PASSED                 [  2%]
tests/func/test_add.py::test_added_task_has_id_set PASSED                [  4%]
...
tests/func/test_api_exceptions.py::test_add_raises PASSED                [ 70%]
tests/func/test_api_exceptions.py::test_list_raises PASSED               [ 72%]
tests/func/test_api_exceptions.py::test_get_raises PASSED                [ 74%]
tests/func/test_api_exceptions.py::TestUpdate::test_bad_id PASSED        [ 76%]
tests/func/test_api_exceptions.py::TestUpdate::test_bad_task PASSED      [ 78%]
tests/func/test_api_exceptions.py::test_delete_raises PASSED             [ 80%]
tests/func/test_api_exceptions.py::test_start_tasks_db_raises PASSED     [ 82%]
...
```

- Using `-v` gives you the syntax for how to run a specific directory, class, and test

#### A Single Test File/Module

- To run a file full of tests, list the file with the relative path as a parameter
  - `pytest tests/func/test_add.py`

#### A Single Test Function

- To run a single test function, add `::` and the test function name
  - `pytest​ tests/func/test_add.py::test_add_returns_valid_id​`

#### A Single Test Class

- Test classes are a way to group tests that make sense to be grouped together
  - see: [`func/test_api_exceptions.py`](ch2/tasks_proj/tests/func/test_api_exceptions.py)

```python
class TestUpdate:
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an exception."""
        ...

    def test_bad_task(self):
        """A non-Task task should raise an exception."""
        ...
```

- To run just this class, add `::`, then the class name to the file parameter
  - `pytest tests/func/test_api_exceptions.py::TestUpdate`
- Note: Running pylint on the above will result in `R0201: Method could be a function (no-self-use)` messages
  - fix as folllows:

```python
class TestUpdate:
    """Test expected exceptions with tasks.update()."""

    @staticmethod
    def test_bad_id():
        """A non-int id should raise an exception."""
        ...
```

#### A Single Test Method of a Test Class

- If you want to run just one method, add another `::` and the method name
  - `pytest tests/func/test_api_exceptions.py::TestUpdate::test_bad_id​`

#### A Set of Tests Based on Test Name

- The `-k` option enables you to pass in an expression to run tests that have certain names specified by the expression as a substring of the test name
  - you can use `and`, `or`, and `not` in your expression

```console
$ pytest -v -k "_raises and not delete"
============================= test session starts ==============================
...
collected 56 items / 52 deselected / 4 selected

tests/func/test_api_exceptions.py::test_add_raises PASSED                [ 25%]
tests/func/test_api_exceptions.py::test_list_raises PASSED               [ 50%]
tests/func/test_api_exceptions.py::test_get_raises PASSED                [ 75%]
tests/func/test_api_exceptions.py::test_start_tasks_db_raises PASSED     [100%]
```

### Parametrized Testing

- Parametrized testing is a way to send multiple sets of data through the same test and have pytest report if any of the sets failed
- We can use `@pytest.mark.parametrize(argnames, argvalues)` to pass lots of data through the same test
  - first argument is a string with a comma-separated list of names
  - second argument is a list of values
  - pytest will run this test once for each value and report each as a separate test
- See: [`func/test_add_variety.py`](ch2/tasks_proj/tests/func/test_add_variety.py)

#### One Parameter

```python
@pytest.mark.parametrize(
    "task",
    [
        Task("sleep", done=True),
        Task("wake", "brian"),
        Task("breathe", "BRIAN", True),
        Task("exercise", "BrIaN", False),
    ],
)
def test_add_2(task):
    """parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
```

```console
$ pytest -v tests/func/test_add_variety.py::test_add_2
============================= test session starts ==============================
...
collected 4 items

tests/func/test_add_variety.py::test_add_2[task0] PASSED                 [ 25%]
tests/func/test_add_variety.py::test_add_2[task1] PASSED                 [ 50%]
tests/func/test_add_variety.py::test_add_2[task2] PASSED                 [ 75%]
tests/func/test_add_variety.py::test_add_2[task3] PASSED                 [100%]

============================== 4 passed in 0.51s ===============================
```

#### Multiple Parameters

```python
@pytest.mark.parametrize(
    "summary, owner, done",
    [
        ("sleep", None, False),
        ("wake", "brian", False),
        ("breathe", "BRIAN", True),
        ("eat eggs", "BrIaN", False),
    ],
)
def test_add_3(summary, owner, done):
    ...
```

```console
$ pytest -v tests/func/test_add_variety.py::test_add_3
============================= test session starts ==============================
...
collected 4 items

tests/func/test_add_variety.py::test_add_3[sleep-None-False] PASSED      [ 25%]
tests/func/test_add_variety.py::test_add_3[wake-brian-False] PASSED      [ 50%]
tests/func/test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED    [ 75%]
tests/func/test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED  [100%]

============================== 4 passed in 0.47s ===============================
```

- You can use that whole test identifier (**node**) to re-run a test
  - use quotes if there are spaces in the identifier

```console
$ pytest -v "tests/func/test_add_variety.py::test_add_3[eat eggs-BrIaN-False]"
============================= test session starts ==============================
...
collected 1 item

tests/func/test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED  [100%]

============================== 1 passed in 0.15s ===============================
```

#### Arguments Assigned to a Variable

```python
tasks_to_try = (
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
)


@pytest.mark.parametrize("task", tasks_to_try)
def test_add_4(task):
    ...
```

```console
$ pytest -v tests/func/test_add_variety.py::test_add_4
============================= test session starts ==============================
...
collected 5 items

tests/func/test_add_variety.py::test_add_4[task0] PASSED                 [ 20%]
tests/func/test_add_variety.py::test_add_4[task1] PASSED                 [ 40%]
tests/func/test_add_variety.py::test_add_4[task2] PASSED                 [ 60%]
tests/func/test_add_variety.py::test_add_4[task3] PASSED                 [ 80%]
tests/func/test_add_variety.py::test_add_4[task4] PASSED                 [100%]

============================== 5 passed in 1.07s ===============================
```

#### `ids` Optional Parameter to Make Our Own Identifiers

- Use the `ids` optional parameter to `parametrize()` to make our own identifiers for each data set
  - a list of strings the same length as the number of data sets

```python
tasks_to_try = (
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
)


task_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done) for t in tasks_to_try]


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
def test_add_5(task):
    ...
```

```console
$ pytest -v tests/func/test_add_variety.py::test_add_5
============================= test session starts ==============================
...
collected 5 items

tests/func/test_add_variety.py::test_add_5[Task(sleep,None,True)] PASSED [ 20%]
tests/func/test_add_variety.py::test_add_5[Task(wake,brian,False)0] PASSED [ 40%]
tests/func/test_add_variety.py::test_add_5[Task(wake,brian,False)1] PASSED [ 60%]
tests/func/test_add_variety.py::test_add_5[Task(breathe,BRIAN,True)] PASSED [ 80%]
tests/func/test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)] PASSED [100%]

============================== 5 passed in 0.57s ===============================
```

#### `parametrize()` on Classes

- The same data sets will be sent to all test methods in the class

```python
@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
class TestAdd:
    """parametrize and test classes"""

    def test_equivalent(self, task):
        ...

    def test_valid_id(self, task):
        ...
```

```console
$ pytest -v tests/func/test_add_variety.py::TestAdd
============================= test session starts ==============================
...
collected 10 items

tests/func/test_add_variety.py::TestAdd::test_equivalent[Task(sleep,None,True)] PASSED [ 10%]
tests/func/test_add_variety.py::TestAdd::test_equivalent[Task(wake,brian,False)0] PASSED [ 20%]
tests/func/test_add_variety.py::TestAdd::test_equivalent[Task(wake,brian,False)1] PASSED [ 30%]
tests/func/test_add_variety.py::TestAdd::test_equivalent[Task(breathe,BRIAN,True)] PASSED [ 40%]
tests/func/test_add_variety.py::TestAdd::test_equivalent[Task(exercise,BrIaN,False)] PASSED [ 50%]
tests/func/test_add_variety.py::TestAdd::test_valid_id[Task(sleep,None,True)] PASSED [ 60%]
tests/func/test_add_variety.py::TestAdd::test_valid_id[Task(wake,brian,False)0] PASSED [ 70%]
tests/func/test_add_variety.py::TestAdd::test_valid_id[Task(wake,brian,False)1] PASSED [ 80%]
tests/func/test_add_variety.py::TestAdd::test_valid_id[Task(breathe,BRIAN,True)] PASSED [ 90%]
tests/func/test_add_variety.py::TestAdd::test_valid_id[Task(exercise,BrIaN,False)] PASSED [100%]

============================== 10 passed in 1.34s ==============================
```

#### Identify Parameters with an `id`

- Identify parameters by including an `id` right alongside the parameter value
  - syntax: `pytest.param(<value>, id="something")`
  - useful when the `id` cannot be derived from the parameter value

```python
@pytest.mark.parametrize(
    "task",
    [
        pytest.param(Task("create"), id="just summary"),
        pytest.param(Task("inspire", "Michelle"), id="summary/owner"),
        pytest.param(Task("encourage", "Michelle", True), id="summary/owner/done"),
    ],
)
def test_add_6(task):
    ...
```

```console
$ pytest -v tests/func/test_add_variety.py::test_add_6
============================= test session starts ==============================
...
collected 3 items

tests/func/test_add_variety.py::test_add_6[just summary] PASSED          [ 33%]
tests/func/test_add_variety.py::test_add_6[summary/owner] PASSED         [ 66%]
tests/func/test_add_variety.py::test_add_6[summary/owner/done] PASSED    [100%]

============================== 3 passed in 0.46s ===============================
```

## 3. pytest Fixtures

- Fixtures are functions that are run by pytest before (and sometimes after) the actual test functions
  - the mechanism pytest provides to allow the separation of "getting ready for" and "cleaning up after" code from your test functions
- You can use fixtures to
  - get a data set for the tests to work on
  - get a system into a known state before running a test
  - get data ready for multiple tests
- `@pytest.fixture()` decorator is used to tell pytest that a function is a fixture
- When you include the fixture name in the parameter list of a test function, pytest knows to run it before running the test

```python
@pytest.fixture()
def​ some_data():
    """Return answer to ultimate question."""
    ​return​ 42


​def​ test_some_data(some_data):
    """Use fixture return value in a test."""
    ​assert​ some_data == 42
```

- `test_some_data()` has the name of the fixture, `some_data`, as a parameter
  - pytest will look for a fixture with this name in the module of the test
  - or in `conftest.py` files if it doesn't find it in this file

### Sharing Fixtures Through conftest.py

- To share fixtures among multiple test files
  - use a **`conftest.py`** file somewhere centrally located for all of the tests
  - for the Tasks project: `tasks_proj/tests/conftest.py`
- You can put fixtures in individual test files
  - to only be used by tests in that file
- You can have other `conftest.py` files in subdirectories of the top tests directory
  - will be available to tests in that directory and subdirectories
- Although `conftest.py` is a Python module, it should _not_ be imported by test files
  - gets read by pytest, and is considered a local _plugin_

### Using Fixtures for Setup and Teardown

- pytest includes a fixture called **`tmpdir`** that we can use for testing and don't have to worry about cleaning up

```python
@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
```

- If there is a **`yield`** in the function
  - fixture execution stops there
  - passes control to the tests
  - picks up on the next line after the tests are done
- Code after the `yield` is guaranteed to run regardless of what happens during the tests
- We're not returning any data with the `yield` in this fixture, but you can
- See: [`tests/conftest.py`](ch3/a/tasks_proj/tests/conftest.py)

### Tracing Fixture Execution with `--setup-show`

- Use `--setup-show` to see what fixtures are run

```python
def test_add_returns_valid_id(tasks_db):
    ...
```

```console
$ pytest --setup-show func/test_add.py -k valid_id
============================= test session starts ==============================
...
collected 3 items / 2 deselected / 1 selected

func/test_add.py
SETUP    S tmp_path_factory
        SETUP    F tmp_path (fixtures used: tmp_path_factory)
        SETUP    F tmpdir (fixtures used: tmp_path)
        SETUP    F tasks_db (fixtures used: tmpdir)
        func/test_add.py::test_add_returns_valid_id (fixtures used: request, tasks_db, tmp_path, tmp_path_factory, tmpdir).
        TEARDOWN F tasks_db
        TEARDOWN F tmpdir
        TEARDOWN F tmp_path
TEARDOWN S tmp_path_factory
```

- The `F` and `S` in front of the fixture names indicate scope
  - `F` for function scope
  - `S` for session scope

### Using Fixtures for Test Data

- Fixtures are a great place to store data to use for testing
  - you can return anything
- When an exception occurs in a fixture:

```console
$ pytest test_fixtures.py::test_other_data
============================= test session starts ==============================
...
collected 1 item

test_fixtures.py E                                                       [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_other_data _______________________

    @pytest.fixture()
    def some_other_data():
        """Raise an exception from fixture."""
>       return 1 / 0
E       ZeroDivisionError: division by zero

test_fixtures.py:20: ZeroDivisionError
=========================== short test summary info ============================
ERROR test_fixtures.py::test_other_data - ZeroDivisionError: division by zero
=============================== 1 error in 0.02s ===============================
```

### Using Multiple Fixtures

- [`tests/conftest.py`](ch3/a/tasks_proj/tests/conftest.py):

```python
@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task("Write some code", "Brian", True),
        Task("Code review Brian's code", "Katie", False),
        Task("Fix what Brian did", "Michelle", False),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)
```

- [`func/test_add.py`](ch3/a/tasks_proj/tests/func/test_add.py):

```python
def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task("throw a party"))

    #  THEN the count increases by 1
    assert tasks.count() == 4
```

```console
$ pytest --setup-show func/test_add.py::test_add_increases_count
============================= test session starts ==============================
...
collected 1 item

func/test_add.py
SETUP    S tmp_path_factory
        SETUP    F tmp_path (fixtures used: tmp_path_factory)
        SETUP    F tmpdir (fixtures used: tmp_path)
        SETUP    F tasks_db (fixtures used: tmpdir)
        SETUP    F tasks_just_a_few
        SETUP    F db_with_3_tasks (fixtures used: tasks_db, tasks_just_a_few)
        func/test_add.py::test_add_increases_count (fixtures used: db_with_3_tasks, request, tasks_db, tasks_just_a_few, tmp_path, tmp_path_factory, tmpdir).
        TEARDOWN F db_with_3_tasks
        TEARDOWN F tasks_just_a_few
        TEARDOWN F tasks_db
        TEARDOWN F tmpdir
        TEARDOWN F tmp_path
TEARDOWN S tmp_path_factory
```

### Specifying Fixture Scope

- Fixtures include an optional parameter called **`scope`**, which controls how often a fixture gets set up and torn down
  - `scope="function"`
    - run once per test function
    - default scope used when no `scope` parameter is specified
  - `scope="class"`
    - run once per test class, regardless of how many test methods are in the class
  - `scope="module"`
    - run once per module, regardless of how many test functions or methods or other fixtures in the module use it
  - `scope="session"`
    - run once per session
    - all test methods and functions using a fixture of session scope share one setup and teardown call
- The scope is set at the definition of a fixture, and not at the place where it's called
  - test functions that use a fixture don't control how often a fixture is set up and torn down
- Fixtures can only depend on other fixtures of their same scope or wider
- [`tests/conftest.py`](ch3/b/tasks_proj/tests/conftest.py):

```python
@pytest.fixture(scope="session")
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task("Write some code", "Brian", True),
        Task("Code review Brian's code", "Katie", False),
        Task("Fix what Brian did", "Michelle", False),
    )


@pytest.fixture(scope="session")
def tasks_db_session(tmpdir_factory):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), "tiny")
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)
```

- [`func/test_add.py`](ch3/b/tasks_proj/tests/func/test_add.py):

```python
def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task("throw a party"))

    #  THEN the count increases by 1
    assert tasks.count() == 4
```

```console
$ pytest --setup-show func/test_add.py::test_add_increases_count
============================= test session starts ==============================
...
collected 1 item

func/test_add.py
SETUP    S tasks_just_a_few
SETUP    S tmp_path_factory
SETUP    S tmpdir_factory (fixtures used: tmp_path_factory)
SETUP    S tasks_db_session (fixtures used: tmpdir_factory)
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F db_with_3_tasks (fixtures used: tasks_db, tasks_just_a_few)
        func/test_add.py::test_add_increases_count (fixtures used: db_with_3_tasks, request, tasks_db, tasks_db_session, tasks_just_a_few, tmp_path_factory, tmpdir_factory).
        TEARDOWN F db_with_3_tasks
        TEARDOWN F tasks_db
TEARDOWN S tasks_db_session
TEARDOWN S tmpdir_factory
TEARDOWN S tmp_path_factory
TEARDOWN S tasks_just_a_few
```

### Specifying Fixtures with usefixtures

- You can also mark a test or a class with `@pytest.mark.usefixtures('fixture1', 'fixture2')`
  - takes a string that is composed of a comma-separated list of fixtures to use
- A test using a fixture due to `usefixtures` cannot use the fixture's return value
- See: [`ch3/test_scope.py`](ch3/test_scope.py)

### Using `autouse` for Fixtures That Always Get Used

- You can use `autouse=True` to get a fixture to run all of the time
- See: [`ch3/test_autouse.py`](ch3/test_autouse.py)

### Renaming Fixtures

- pytest allows you to rename fixtures with a **`name`** parameter to `@pytest.fixture()`

```python
@pytest.fixture(name="lue")
def ultimate_answer_to_life_the_universe_and_everything():
    """Return ultimate answer."""
    return 42


def test_everything(lue):
    """Use the shorter name."""
    assert lue == 42
```

```console
$ pytest --setup-show test_rename_fixture.py
============================= test session starts ==============================
...
collected 1 item

test_rename_fixture.py
        SETUP    F lue
        test_rename_fixture.py::test_everything (fixtures used: lue).
        TEARDOWN F lue

============================== 1 passed in 0.00s ===============================
```

- Use the `--fixtures` pytest option to find out where `lue` is defined
  - lists all the fixtures available for the test, including ones that have been renamed

```console
--fixtures, --funcargs
                        show available fixtures, sorted by plugin appearance
                        (fixtures with leading '_' are only shown with '-v')
```

```console
$ pytest --fixtures test_rename_fixture.py
============================= test session starts ==============================
...
collected 1 item
cache
    Return a cache object that can persist state between testing sessions.
    ...
...
------------------ fixtures defined from test_rename_fixture -------------------
lue
    Return ultimate answer.


============================ no tests ran in 0.00s =============================
```

### Parametrizing Fixtures

- [`func/test_add_variety2.py`](ch3/b/tasks_proj/tests/func/test_add_variety2.py)

```python
tasks_to_try = (
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
)


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Using no ids."""
    return request.param


def test_add_a(tasks_db, a_task):
    """Using a_task fixture (no ids)."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)
```

- `request` is a built-in fixture that represents the calling state of the fixture
  - has a field `param` that is filled in with one element from the list assigned to `params` in `@pytest.fixture(params=tasks_to_try)`

```console
$ pytest --setup-show test_add_variety2.py::test_add_a
============================= test session starts ==============================
...
collected 4 items

test_add_variety2.py
SETUP    S tmp_path_factory
SETUP    S tmpdir_factory (fixtures used: tmp_path_factory)
SETUP    S tasks_db_session (fixtures used: tmpdir_factory)
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F a_task[Task(summary='sleep', owner=None, done=True, id=None)]
        func/test_add_variety2.py::test_add_a[a_task0] (fixtures used: a_task, request, tasks_db, tasks_db_session, tmp_path_factory, tmpdir_factory).
        TEARDOWN F a_task[Task(summary='sleep', owner=None, done=True, id=None)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F a_task[Task(summary='wake', owner='brian', done=False, id=None)]
        func/test_add_variety2.py::test_add_a[a_task1] (fixtures used: a_task, request, tasks_db, tasks_db_session, tmp_path_factory, tmpdir_factory).
        TEARDOWN F a_task[Task(summary='wake', owner='brian', done=False, id=None)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F a_task[Task(summary='breathe', owner='BRIAN', done=True, id=None)]
        func/test_add_variety2.py::test_add_a[a_task2] (fixtures used: a_task, request, tasks_db, tasks_db_session, tmp_path_factory, tmpdir_factory).
        TEARDOWN F a_task[Task(summary='breathe', owner='BRIAN', done=True, id=None)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F a_task[Task(summary='exercise', owner='BrIaN', done=False, id=None)]
        func/test_add_variety2.py::test_add_a[a_task3] (fixtures used: a_task, request, tasks_db, tasks_db_session, tmp_path_factory, tmpdir_factory).
        TEARDOWN F a_task[Task(summary='exercise', owner='BrIaN', done=False, id=None)]
        TEARDOWN F tasks_db
TEARDOWN S tasks_db_session
TEARDOWN S tmpdir_factory
TEARDOWN S tmp_path_factory

============================== 4 passed in 0.67s ===============================
```

- `ids`: list of string ids each corresponding to the params so that they are part of the test id

```python
task_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done) for t in tasks_to_try]


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Using a list of ids."""
    return request.param
```

- We can also set the `ids` parameter to a function that provides the identifiers

```python
def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return "Task({},{},{})".format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    return request.param


def test_add_c(tasks_db, c_task):
    """Use fixture with generated ids."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)
```

- Since the parametrization is a list of `Task` objects, `id_func()` will be called with a `Task` object, which allows us to use the `namedtuple` accessor methods to access a single `Task` object to generate the identifier for one `Task` object at a time

## 4. Builtin Fixtures

### Using `tmpdir` and `tmpdir_factory`

- The `tmpdir` and `tmpdir_factory` builtin fixtures are used to create a temporary file system directory before your test runs, and remove the directory when your test is finished
- [`tmpdir`](https://docs.pytest.org/en/stable/reference.html#tmpdir)
  - to create files or directories used by a single test
  - function scope
  - the value returned from `tmpdir` is an object of type [`py.path.local`](https://py.readthedocs.io/en/latest/path.html)
- [`tmpdir_factory`](https://docs.pytest.org/en/stable/reference.html#tmpdir-factory)
  - to set up a directory for many tests
  - session scope
  - `mktemp()`: creates a directory
  - `getbasetemp()`: returns the base directory used for this session
    - base directory is left alone after a session, but only the most recent few temporary base directories are left on the system
    - `pytest --basetemp=mydir` to specify your own base directory
- See: [`ch4/test_tmpdir.py`](ch4/test_tmpdir.py)
- Temporary directories for other scopes
  - create another fixture of the scope we want and have it use `tmpdir_factory`
  - e.g., put a `module` scope fixture in either the module itself, or in a `conftest.py` file
  - see:
    - [`authors/conftest.py`](ch4/authors/conftest.py)
    - [`authors/test_authors.py`](ch4/authors/test_authors.py)

### Using `pytestconfig`

- With the `pytestconfig` builtin fixture, you can control how pytest runs through command-line arguments and options, configuration files, plugins, and the directory from which you launched pytest
- Shortcut to `request.config`
- Sometimes referred to in the pytest documentation as "the pytest config object"
- Adding a custom command-line option and read the option value from within a test
  - read the value of command-line options directly from `pytestconfig`
  - add the option and have pytest parse it using a _hook function_
    - should be done via plugins or in the `conftest.py` file at the top of your project directory structure
    - see: [`pytestconfig/conftest.py`](ch4/pytestconfig/conftest.py)

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
custom options:
  --myopt               some boolean option
  --foo=FOO             foo: bar or baz
```

- You can then
  - access options from a test
  - access `pytestconfig` from a fixture
  - make fixture for the option name
  - access builtin options as well as information about how pytest was started (the directory, the arguments, and so on)
  - see: [`pytestconfig/test_config.py`](ch4/pytestconfig/test_config.py)

```console
$ pytest -s -q --myopt --foo baz test_config.py::test_option
"foo" set to: baz
"myopt" set to: True
.
1 passed in 0.07s

$ pytest -s -q --myopt --foo baz test_config.py::test_pytestconfig
args            : ['test_config.py::test_pytestconfig']
inifile         : None
invocation_dir  : /.../ch4/pytestconfig
rootdir         : /.../ch4/pytestconfig
-k EXPRESSION   :
-v, --verbose   : -1
-q, --quiet     : 1
-l, --showlocals: False
--tb=style      : auto
.
1 passed in 0.00s
```

### Using `cache`

- Sometimes passing information from one test session to the next can be quite useful
  - with the `cache` builtin fixture
- `cache` is used for the `--last-failed` and `--failed-first` builtin functionality

```console
$ pytest --cache-clear cache/test_pass_fail.py
============================= test session starts ==============================
...
collected 2 items

cache/test_pass_fail.py .F                                               [100%]

=================================== FAILURES ===================================
_______________________________ test_this_fails ________________________________

    def test_this_fails():
>       assert 1 == 2
E       assert 1 == 2

cache/test_pass_fail.py:6: AssertionError
=========================== short test summary info ============================
FAILED cache/test_pass_fail.py::test_this_fails - assert 1 == 2
========================= 1 failed, 1 passed in 0.02s ==========================

$ pytest --cache-show
============================= test session starts ==============================
...
cachedir: /.../ch4/.pytest_cache
----------------------------- cache values for '*' -----------------------------
cache/lastfailed contains:
  {'cache/test_pass_fail.py::test_this_fails': True}
cache/nodeids contains:
  ['cache/test_pass_fail.py::test_this_passes',
   'cache/test_pass_fail.py::test_this_fails']
cache/stepwise contains:
  []

============================ no tests ran in 0.00s =============================
```

- The interface for the `cache` fixture:
  - `cache.get(key, default)`
  - `cache.set(key, value)`
- By convention, key names start with the name of your application or plugin, followed by a `/`, and continuing to separate sections of the key name with `/`s
  - the value you store can be anything that is convertible to json
- Example: a fixture that records how long tests take, saves the times, and on the next run, reports an error on tests that take longer than, say, twice as long as last time
  - see: [`cache/test_slower.py`](ch4/cache/test_slower.py)
  - see also: [`cache/test_slower_2.py`](ch4/cache/test_slower_2.py)

### Using `capsys`

- The `capsys` builtin fixture provides two bits of functionality:
  - retrieve `stdout` and `stderr` from some code
  - disables output capture temporarily
- The captured `stdout` and `stderr` are retrieved from `capsys.readouterr()`
  - return value is whatever has been captured since the beginning of the function, or from the last time it was called
  - see [`cap/test_capsys.py`](ch4/cap/test_capsys.py)
- Use `with capsys.disabled()` to temporarily let output get past the capture mechanism

### Using `monkeypatch`

- A "monkey patch" is a dynamic modification of a class or module during runtime
  - a convenient way to take over part of the runtime environment of the code under test and replace either input dependencies or output dependencies with objects or functions that are more convenient for testing
- The `monkeypatch` fixture provides the following functions:
  - `setattr(target, name, value=<notset>, raising=True)`: Set an attribute
  - `delattr(target, name=<notset>, raising=True)`: Delete an attribute
  - `setitem(dic, name, value)`: Set a dictionary entry
  - `delitem(dic, name, raising=True)`: Delete a dictionary entry
  - `setenv(name, value, prepend=None)`: Set an environmental variable
  - `delenv(name, raising=True)`: Delete an environmental variable
  - `syspath_prepend(path)`: Prepend path to sys.path, which is Python's list of import locations
  - `chdir(path)`: Change the current working directory
- See: <https://docs.pytest.org/en/latest/reference.html#monkeypatch>
- Consider (see: [`monkey/cheese.py`](ch4/monkey/cheese.py)):

```python
def write_cheese_preferences(prefs):
    full_path = os.path.expanduser("~/.cheese.json")
    with open(full_path, "w") as f:
        json.dump(prefs, f, indent=4)


def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)
```

- `write_default_cheese_preferences()` is a function that takes no parameters and doesn't return anything
  - has a side effect that we can test - it writes a file to the current user's home directory
  - patch `expanduser` so that anything in the `cheese` module that calls `os.path.expanduser()` gets our lambda expression instead
  - see: `test_def_prefs_change_expanduser(tmpdir, monkeypatch)` in [`monkey/test_cheese.py`](ch4/monkey/test_cheese.py)

```python
monkeypatch.setattr(
    cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
)
```

- Use `monkeypatch.setitem()` to change dictionary items just for the duration of the test
  - see: `test_def_prefs_change_defaults(tmpdir, monkeypatch)` in [`monkey/test_cheese.py`](ch4/monkey/test_cheese.py)
- `syspath_prepend(path)`
  - puts your new path at the head of the line for module import directories
  - one use would be to replace a system-wide module or package with a stub version, and the code under test will find the stub version first
- `chdir(path)`
  - changes the current working directory during the test
  - useful for testing command-line scripts and other utilities that depend on what the current working directory is by setting up a temporary directory with whatever contents make sense for your script
- You can also use the `monkeypatch` fixture functions in conjunction with `unittest.mock` to temporarily replace attributes with mock objects

### Using `doctest_namespace`

- The `doctest` module is part of the standard Python library and allows you to put little code examples inside docstrings for a function and test them to make sure they work
- You can have pytest look for and run doctest tests within your Python code by using the `--doctest-modules` flag
- With the `doctest_namespace` fixture, you can build `autouse` fixtures to add symbols to the namespace pytest uses while running doctest tests
  - commonly used to add module imports into the namespace
- See: [`3/unnecessary_math.py`](ch4/dt/3/unnecessary_math.py)
  - since the name `unnecessary_math` is long, we decide to use `um` instead by using `import unnecessary_math as um` in the top docstring
  - code in the docstrings of the functions doesn't include the `import` statement, but continue with the `um` convention
  - the problem is that pytest treats each docstring with code as a different test
- `doctest_namespace`, used in an `autouse` fixture at a top-level `conftest.py` file, will fix the problem without changing the source code
  - see: [`3/conftest.py`](ch4/dt/3/conftest.py)
  - any doctests found within the scope of this `conftest.py` file will have the `um` symbol defined

```console
$ pytest -v --doctest-modules dt/3/unnecessary_math.py
============================= test session starts ==============================
...
collected 3 items

dt/3/unnecessary_math.py::unnecessary_math PASSED                        [ 33%]
dt/3/unnecessary_math.py::unnecessary_math.divide PASSED                 [ 66%]
dt/3/unnecessary_math.py::unnecessary_math.multiply PASSED               [100%]

============================== 3 passed in 0.02s ===============================
```

### Using `recwarn`

- Warnings work a lot like assertions, but are used for things that don't need to stop execution
- The `recwarn` fixture is used to examine warnings generated by code under test
  - see: [`ch4/test_warnings.py`](ch4/test_warnings.py)
- The `recwarn` value acts like a list of warnings, and each warning in the list has a `category`, `message`, `filename`, and `lineno` defined
- The warnings are collected at the beginning of the test
  - if that is inconvenient because the portion of the test where you care about warnings is near the end, you can use `recwarn.clear()` to clear out the list before the chunk of the test where you do care about collecting warnings
- pytest can also check for warnings with `pytest.warns()`

```python
with pytest.warns(None) as warning_list:
    lame_function()
```

- `recwarn` and the `pytest.warns()` context manager provide similar functionality, so the decision of which to use is purely a matter of taste

## 5.Plugins

- The pytest code base is structured with customization and extensions, and there are hooks available to allow modifications and improvements through plugins

### Finding Plugins

- <https://docs.pytest.org/en/latest/plugins.html>
  - lists a few common plugins
- <https://pypi.python.org>
  - the Python Package Index (PyPI) is a great place to find pytest plugins
  - enter "pytest," "pytest-," or "-pytest" into the search box
- <https://github.com/pytest-dev>
  - you can find some popular pytest plugins that are intended to be maintained long-term by the pytest core team

### Installing Plugins

#### Install from PyPI

- As PyPI is the default location for pip, installing plugins from PyPI is the easiest method

```console
$ pip install pytest-cov​
```

- This installs the latest stable version from PyPI.

#### Install from a .tar.gz or .whl

- File Packages on PyPI are distributed as zipped files with the extensions `.tar.gz` (tar balls) and/or `.whl` (wheels)
  - you can download and install from that

```console
$ pip install pytest-cov-2.4.0.tar.gz​
​# or
$ pip install pytest_cov-2.4.0-py2.py3-none-any.whl​
```

#### Install from a Local Directory

- You can keep a local stash of plugins (and other Python packages) in a local or shared directory in `.tar.gz` or `.whl` format, and use that instead

```console
$ cp pytest_cov-2.4.0-py2.py3-none-any.whl some_plugins/​
$ pip install --no-index --find-links=./some_plugins/ pytest-cov​
```

- `--no-index` tells `pip` to not connect to PyPI
- `--find-links=./some_plugins/` tells `pip` to look in the directory called some_plugins

#### Install from a Git Repository

```console
$ pip install git+https://github.com/pytest-dev/pytest-cov
```

- With version tag:

```console
$ pip install git+https://github.com/pytest-dev/pytest-cov@v2.4.0​
```

- Specify a branch:

```console
$ pip install git+https://github.com/pytest-dev/pytest-cov@master​
```

### Writing Your Own Plugins

- Plugins can include hook functions that alter pytest's behavior
- A lot of hook functions are available
  - see:
    - <https://docs.pytest.org/en/latest/_modules/_pytest/hookspec.html>
    - <https://docs.pytest.org/en/latest/reference.html#hooks>
- Frequently, changes you only intended to use on one project will become useful enough to share and grow into a plugin
  - therefore, we'll start by adding functionality to a `conftest.py` file, then, after we get things working in `conftest.py,` we'll move the code to a package
- See: [`func/test_api_exceptions.py`](ch5/a/tasks_proj/tests/func/test_api_exceptions.py)

```console
$ pytest -v --tb=no func/test_api_exceptions.py::TestAdd
============================= test session starts ==============================
...
collected 2 items

func/test_api_exceptions.py::TestAdd::test_missing_summary PASSED        [ 50%]
func/test_api_exceptions.py::TestAdd::test_done_not_bool FAILED          [100%]
```

- Changes:
  - see: [`tests/conftest.py`](ch5/c/tasks_proj/tests/conftest.py)
  - add "Thanks for running the tests" to the header
    - [`pytest_report_header()`](https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_report_header)
  - change FAILED status indicators (`F`) to "OPPORTUNITY for improvement" (`O`)
    - [`pytest_report_teststatus(report)`](https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_report_teststatus)
  - use the `--nice` option to turn the behavior on
    - [`pytest_addoption(parser)`](https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_addoption)

```console
$ pytest --nice --tb=no func/test_api_exceptions.py::TestAdd
============================= test session starts ==============================
...
Thanks for running the tests.
...
collected 2 items

func/test_api_exceptions.py .O                                           [100%]

=============================== warnings summary ===============================
...
=========================== short test summary info ============================
OPPORTUNITY for improvement func/test_api_exceptions.py::TestAdd::test_done_not_bool
=================== 1 failed, 1 passed, 3 warnings in 0.26s ====================
```

```console
$ pytest --nice -v --tb=no func/test_api_exceptions.py::TestAdd
============================= test session starts ==============================
...
Thanks for running the tests.
...
collected 2 items

func/test_api_exceptions.py::TestAdd::test_missing_summary PASSED        [ 50%]
func/test_api_exceptions.py::TestAdd::test_done_not_bool OPPORTUNITY for improvement [100%]

=============================== warnings summary ===============================
...
=========================== short test summary info ============================
OPPORTUNITY for improvement func/test_api_exceptions.py::TestAdd::test_done_not_bool
=================== 1 failed, 1 passed, 3 warnings in 0.25s ====================
```

### Creating an Installable Plugin

- Directory structure:

```text
pytest-nice
​├── LICENSE
​├── README.rst
​├── pytest_nice.py
​├── setup.py
└── tests
    ├── conftest.py
    └── test_nice.py
```

- See:
  - [`pytest-nice/pytest_nice.py`](ch5/pytest-nice/pytest_nice.py)
  - [`pytest-nice/setup.py`](ch5/pytest-nice/setup.py)
  - [`pytest-nice/README.rst`](ch5/pytest-nice/README.rst)
    - Some form of README is a requirement by `setuptools`

### Testing Plugins

- Test a plugin using a plugin called `pytester` that ships with pytest but is disabled by default
  - to use `pytester`, we need to add just one line to `conftest.py`
  - a fixture called `testdir` becomes available when pytester is enabled
  - see: [`tests/conftest.py`](ch5/pytest-nice/tests/conftest.py)
- Tests: [`tests/test_nice.py`](ch5/pytest-nice/tests/test_nice.py)
- To run the tests:

```console
$ cd /path/to/ch5/pytest-nice/
$ pip install .
...
$ pytest -v
...
```

- We can uninstall it just like any other Python package or pytest plugin
  - `​​pip​​ ​​uninstall​​ ​​pytest-nice​`

### Creating a Distribution

- We can use the `setup.py` file to create a distribution

```console
$ cd /path/to/ch5/pytest-nice/
$ python setup.py sdist
...
$ ls dist
pytest-nice-0.1.0.tar.gz
```

- Note: `sdist` stands for "source distribution"

#### Distributing Plugins Through a Shared Directory

- See: [Install from a Local Directory](#install-from-a-local-directory)
- If you've done some bug fixes and there are newer versions in myplugins, you can upgrade by adding `--upgrade`:
  - `pip install --upgrade --no-index --find-links myplugins pytest-nice`

#### Distributing Plugins Through PyPI

- When you are contributing a pytest plugin, a great place to start is by using the `cookiecutter-pytest-plugin`
  - see <https://github.com/pytest-dev/cookiecutter-pytest-plugin>

## 6. Configuration

### Understanding pytest Configuration Files

- `pytest.ini`
  - primary pytest configuration file that allows you to change default behavior
- `conftest.py`
  - local plugin to allow hook functions and fixtures for the directory where the `conftest.py` file exists and all subdirectories
- `__init__.py`
  - when put into every test subdirectory, this file allows you to have identical test filenames in multiple test directories
- If you use tox, `tox.ini`
  - similar to `pytest.ini`, but for tox
  - you can put your pytest configuration here instead of having both a `tox.ini` and a `pytest.ini` file
- If you want to distribute a Python package, `setup.cfg`
  - in `ini` file format and affects the behavior of `setup.py`
  - possible to add a couple of lines to `setup.py` to allow you to run python `setup.py test` and have it run all of your pytest tests
  - if you are distributing a package, you may already have a `setup.cfg` file, and you can use that file to store pytest configuration
- You can get a list of all the valid settings for `pytest.ini` from `pytest --help`
- It is possible for plugins (and `conftest.py` files) to add `ini` file options
  - the added options will be added to the pytest `--help` output as well

### Changing the Default Command-Line Options

- To always use some command line options for a project, set `addopts` in `pytest.ini` to the options you want:

```ini
[pytest]
addopts = -rsxX -l --tb=short --strict
```

### Registering Markers to Avoid Marker Typos

- It's too easy to misspell a marker and end up having some tests with different markers, e.g., `@pytest.mark.smoke` and `@pytest.mark.somke`
- Register markers in `pytest.ini`
  - see: [`tests/pytest.ini`](ch6/b/tasks_proj/tests/pytest.ini)
  - if you use the `--strict` command line option, any misspelled or unregistered markers show up as an error

```ini
[pytest]
  smoke: Run the smoke test functions for tasks project
  get: Run the test functions that test tasks.get()
```

```console
$ pytest --markers
@pytest.mark.smoke: Run the smoke test test functions

@pytest.mark.get: Run the test functions that test tasks.get()

@pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/latest/warnings.html#pytest-mark-filterwarnings
```

### Requiring a Minimum pytest Version

- The `minversion` setting enables you to specify a minimum pytest version you expect for your tests
  - `approx()` for testing floating point numbers for was introduced into pytest version 3.0

```ini
[pytest]
minversion = 3.0
```

### Stopping pytest from Looking in the Wrong Places

- Test discovery traverses many directories recursively
  - there are some directories you don't want pytest looking in
- The default setting for `norecursedirs` is `.* build dist CVS _darcs {arch}` and `*.egg`
  - you can add `venv` and `src`

```ini
norecursedirs = .* venv src *.egg dist build
```

### Specifying Test Directory Locations

- Opposite to `norecursedirs`, `testpaths` tells pytest where to look
  - a list of directories relative to the root directory
- Example:

```text
tasks_proj/
​├── pytest.ini
​├── src
│   └── ...
​└── tests
​    └── ...
```

```ini
[pytest]
testpaths = tests
```

### Changing Test Discovery Rules

- Standard test discovery rules:
  - start at one or more directory
    - you can specify filenames or directory names on the command line
    - if you don't specify anything, the current directory is used
  - look in the directory and all subdirectories recursively for test modules
    - a test module is a file with a name that looks like `test_*.py` or `*_test.py`
  - look in test modules for functions that start with `test_`
  - look for classes that start with `Test`
    - look for methods in those classes that start with `test_` but don't have an `__init__` method
- `python_classes`, `python_files` and `python_functions` allow us to name test classes, files and function/method names something else

```ini
[pytest]
python_classes = *Test Test* *Suite
python_files = test_* *_test check_*
python_functions = test_* check_*
```

### Disallowing XPASS

- Setting `xfail_strict = true` causes tests marked with `@pytest.mark.xfail` that don't fail to be reported as an error

### Avoiding Filename Collisions

- If you have empty `__init__.py` files in all of your test subdirectories, you can have the same test filename show up in multiple directories

## 7. Using pytest with Other Tools

### pdb: Debugging Test Failures

- pytest options available to help speed up debugging test failures:
  - `--tb=[auto/long/short/line/native/no]`: Controls the traceback style
  - `-v / --verbose`: Displays all the test names, passing or failing
  - `-l / --showlocals`: Displays local variables alongside the stacktrace
  - `-lf / --last-failed`: Runs just the tests that failed last
  - `-x / --exitfirst`: Stops the tests session with the first failure
  - `--pdb`: Starts an interactive debugging session at the point of failure
- Commands that you can use when you are at the `(Pdb)` prompt:
  - `p/print expr`: Prints the value of `expr`
  - `pp expr`: Pretty prints the value of `expr`
  - `l/list`: Lists the point of failure and five lines of code above and below
  - `l/list begin,end`: Lists specific line numbers
  - `a/args`: Prints the arguments of the current function with their values (helpful when in a test helper function)
  - `u/up`: Moves up one level in the stack trace
  - `d/down`: Moves down one level in the stack trace
  - `q/quit`: Quits the debugging session
  - other navigation commands like `step` and `next` aren't that useful since we are sitting right at an `assert` statement
  - you can also just type variable names and get the values

```console
$ pytest -x --pdb ch2/tasks_proj/tests
============================= test session starts ==============================
...
collected 56 items

ch2/tasks_proj/tests/func/test_add.py ..                                 [  3%]
ch2/tasks_proj/tests/func/test_add_variety.py .......................... [ 50%]
......                                                                   [ 60%]
ch2/tasks_proj/tests/func/test_api_exceptions.py .......                 [ 73%]
ch2/tasks_proj/tests/func/test_unique_id_1.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def test_unique_id():
        """Calling unique_id() twice should return different numbers."""
        id_1 = tasks.unique_id()
        id_2 = tasks.unique_id()
>       assert id_1 != id_2
E       assert 1 != 1

ch2/tasks_proj/tests/func/test_unique_id_1.py:11: AssertionError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>
> /path/to/ch2/tasks_proj/tests/func/test_unique_id_1.py(11)test_unique_id()
-> assert id_1 != id_2
(Pdb) p tasks.unique_id()
1
(Pdb) id_1
1
(Pdb) id_2
1
(Pdb) l
  6
  7  	def test_unique_id():
  8  	    """Calling unique_id() twice should return different numbers."""
  9  	    id_1 = tasks.unique_id()
 10  	    id_2 = tasks.unique_id()
 11  ->	    assert id_1 != id_2
 12
 13
 14  	@pytest.fixture(autouse=True)
 15  	def initialized_tasks_db(tmpdir):
 16  	    """Connect to db before testing, disconnect after."""
(Pdb) u
> /path/to/venv/lib/python3.6/site-packages/_pytest/python.py(184)pytest_pyfunc_call()
-> result = testfunction(**testargs)
(Pdb) a
pyfuncitem = <Function test_unique_id>
(Pdb) d
> /path/to/ch2/tasks_proj/tests/func/test_unique_id_1.py(11)test_unique_id()
-> assert id_1 != id_2
(Pdb) q


=============================== warnings summary ===============================
...
=========================== short test summary info ============================
FAILED ch2/tasks_proj/tests/func/test_unique_id_1.py::test_unique_id - assert...
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!! _pytest.outcomes.Exit: Quitting debugger !!!!!!!!!!!!!!!!!!!
============= 1 failed, 41 passed, 4 warnings in 60.26s (0:01:00) ==============
```

### Coverage.py: Determining How Much Code Is Tested

- Coverage.py is the preferred Python coverage tool that measures code coverage
- Installing `pytest-cov` plugin will pull in `coverage.py` since coverage is one its dependencies
  - `pip install pytest-cov`

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
coverage reporting with distributed testing support:
  --cov=[SOURCE]        Path or package name to measure during execution (multi-
                        allowed). Use --cov= to not do any source filtering and
                        record everything.
  --cov-report=TYPE     Type of report to generate: term, term-missing,
                        annotate, html, xml (multi-allowed). term, term-missing
                        may be followed by ":skip-covered". annotate, html and
                        xml may be followed by ":DEST" where DEST specifies the
                        output location. Use --cov-report= to not generate any
                        output.
  --cov-config=PATH     Config file for coverage. Default: .coveragerc
  --no-cov-on-fail      Do not report coverage if test run fails. Default: False
  --no-cov              Disable coverage report completely (useful for
                        debuggers). Default: False
  --cov-fail-under=MIN  Fail if the total coverage is less than MIN.
  --cov-append          Do not delete coverage but append to current. Default:
                        False
  --cov-branch          Enable branch coverage.
  --cov-context=CONTEXT
                        Dynamic contexts to use. "test" for now.
```

```console
$ pytest --cov=src
============================= test session starts ==============================
...
plugins: cov-2.8.1, mock-3.1.0
collected 62 items

tests/func/test_add.py ...                                               [  4%]
tests/func/test_add_variety.py ............................              [ 50%]
tests/func/test_add_variety2.py ............                             [ 69%]
tests/func/test_api_exceptions.py .........                              [ 83%]
tests/func/test_unique_id.py .                                           [ 85%]
tests/unit/test_cli.py .....                                             [ 93%]
tests/unit/test_task.py ....                                             [100%]

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/tasks/__init__.py              2      0   100%
src/tasks/api.py                  79     22    72%
src/tasks/cli.py                  45     14    69%
src/tasks/config.py               18     12    33%
src/tasks/tasksdb_pymongo.py      74     74     0%
src/tasks/tasksdb_tinydb.py       32      4    88%
--------------------------------------------------
TOTAL                            250    126    50%


============================== 62 passed in 5.14s ==============================
```

### mock: Swapping Out Part of the System

- The `mock` package is shipped as part of the Python standard library as `unittest.mock` as of Python 3.3
- For use with pytest, a plugin called `pytest-mock` has some conveniences
- `list_tasks(owner)` in [`tasks/cli.py`](ch7/tasks_proj_v2/src/tasks/cli.py)
  - depends on a couple of other functions
    - `tasks_db()`, which is a context manager
    - `tasks.list_tasks(owner)`, which is the API function in [`tasks/api.py`](ch7/tasks_proj_v2/src/tasks/api.py)
  - use mock to put fake functions in place for `tasks_db()` and `tasks.list_tasks()`
    - we can call the `list_tasks` method through the command-line interface and make sure it
      - calls the `tasks.list_tasks()` function correctly
      - deals with the return value correctly
- Stub `_tasks_db()`
  - see `stub_tasks_db()` in [`unit/test_cli.py`](ch7/tasks_proj_v2/tests/unit/test_cli.py)
- Use `mocker` to replace the real context manager with our stub
  - `mocker` is a fixture provided by the `pytest-mock` plugin a convenience interface to `unittest.mock`
  - see `test_list_no_args(mocker)` in [`unit/test_cli.py`](ch7/tasks_proj_v2/tests/unit/test_cli.py)
- The `MagicMock` class is a flexible subclass of `unittest.Mock` with reasonable default behavior and the ability to specify a return value
- The `Mock` and `MagicMock` classes (and others) are used to mimic the interface of other code with introspection methods built in to allow you to ask them how they were called

```python
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
```

- See:
  - <https://docs.python.org/dev/library/unittest.mock.html>
  - <https://pypi.org/project/pytest-mock/>

### tox: Testing Multiple Configurations

- tox is a command-line tool that allows you to run your complete suite of tests in multiple environments
- You can use it to test with different
  - versions of Python
  - dependency configurations
  - configurations for different operating systems
- tox uses the `setup.py` file for the package under test to create an installable source distribution of your package
- It looks in `tox.ini` for a list of environments and then for each environment, tox:
  - creates a virtual environment in a `.tox` directory
  - `pip` installs some dependencies
  - `pip` installs your package from the `sdist`
  - runs your tests
  - reports a summary of how they all did
- Add a `tox.ini` file at the same level as `setup.py` - the top project directory
  - move anything that's in `pytest.ini` into `tox.ini`
  - see [`tasks_proj_v2/tox.ini`](ch7/tasks_proj_v2/tox.ini)
- Install tox (can be done within a virtual environment):
  - `pip install tox`
- Run tox:
  - `tox`
- See: <https://tox.readthedocs.io/en/latest/>

## A3. Plugin Sampler Pack

- All of the plugins featured here are available on PyPI and are installed with `pip install <plugin-name>`

### Plugins That Change the Normal Test Run Flow

#### pytest-repeat: Run Tests More Than Once

- To run tests more than once per session, use the `pytest-repeat` plugin
- This plugin is useful if you have an intermittent failure in a test
- You can use `--count=2` to run everything twice
- See: <https://pypi.org/project/pytest-repeat/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
custom options:
  --count=COUNT         Number of times to repeat each test
  --repeat-scope={function,class,module,session}
                        Scope for repeating tests
```

```console
$ pytest --count=2 -v -k test_list
============================= test session starts ==============================
...
plugins: repeat-0.8.0, cov-2.8.1, mock-3.1.0
collected 124 items / 112 deselected / 12 selected

tests/func/test_api_exceptions.py::test_list_raises[1-2] PASSED          [  8%]
tests/func/test_api_exceptions.py::test_list_raises[2-2] PASSED          [ 16%]
tests/unit/test_cli.py::test_list_no_args[1-2] PASSED                    [ 25%]
tests/unit/test_cli.py::test_list_no_args[2-2] PASSED                    [ 33%]
tests/unit/test_cli.py::test_list_print_empty[1-2] PASSED                [ 41%]
tests/unit/test_cli.py::test_list_print_empty[2-2] PASSED                [ 50%]
tests/unit/test_cli.py::test_list_print_many_items[1-2] PASSED           [ 58%]
tests/unit/test_cli.py::test_list_print_many_items[2-2] PASSED           [ 66%]
tests/unit/test_cli.py::test_list_dash_o[1-2] PASSED                     [ 75%]
tests/unit/test_cli.py::test_list_dash_o[2-2] PASSED                     [ 83%]
tests/unit/test_cli.py::test_list_dash_dash_owner[1-2] PASSED            [ 91%]
tests/unit/test_cli.py::test_list_dash_dash_owner[2-2] PASSED            [100%]

====================== 12 passed, 112 deselected in 0.26s ======================
```

#### pytest-xdist: Run Tests in Parallel

- If your tests do not need access to a shared resource, you could speed up test sessions by running multiple tests in parallel using the `pytest-xdist` plugin
- You can specify multiple processors and run many tests in parallel
- You can even push off tests onto other machines and use more than one computer
- [`xdist/test_parallel.py`](appendices/xdist/test_parallel.py)
  - a test that takes at least a second to run, with parametrization such that it runs ten times
- See: <https://pypi.org/project/pytest-xdist/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
distributed and subprocess testing:
  -n numprocesses, --numprocesses=numprocesses
                        shortcut for '--dist=load --tx=NUM*popen', you can use
                        'auto' here for auto detection CPUs number on host
                        system and it will be 0 when used with --pdb
  --maxprocesses=maxprocesses
                        limit the maximum number of workers to process the tests
                        when using --numprocesses=auto
  --max-worker-restart=MAXWORKERRESTART, --max-slave-restart=MAXWORKERRESTART
                        maximum number of workers that can be restarted when
                        crashed (set to zero to disable this feature) '--max-
                        slave-restart' option is deprecated and will be removed
                        in a future release
  --dist=distmode       set mode for distributing tests to exec environments.
                        each: send each test to all available environments.
                        load: load balance by sending any pending test to any
                        available environment. loadscope: load balance by
                        sending pending groups of tests in the same scope to any
                        available environment. loadfile: load balance by sending
                        test grouped by file to any available environment.
                        (default) no: run tests inprocess, don't distribute.
  --tx=xspec            add a test execution environment. some examples: --tx
                        popen//python=python2.5 --tx socket=192.168.1.102:8888
                        --tx ssh=user@codespeak.net//chdir=testcache
  -d                    load-balance tests. shortcut for '--dist=load'
  --rsyncdir=DIR        add directory for rsyncing to remote tx nodes.
  --rsyncignore=GLOB    add expression for ignores when rsyncing to remote tx
                        nodes.
  --boxed               backward compatibility alias for pytest-forked --forked
  --testrunuid=TESTRUNUID
                        provide an identifier shared amongst all workers as the
                        value of the 'testrun_uid' fixture, ,if not provided,
                        'testrun_uid' is filled with a new unique string on
                        every test run.
  -f, --looponfail      run tests in subprocess, wait for modified files and re-
                        run failing test set until all pass.
```

```console
$ pytest test_parallel.py
============================= test session starts ==============================
plugins: xdist-1.32.0, forked-1.1.3, repeat-0.8.0, cov-2.8.1, mock-3.1.0
collected 10 items

test_parallel.py ..........                                              [100%]

============================= 10 passed in 10.08s ==============================
```

- You can use
  - `-n numprocesses` to run each test in a subprocess
  - `-n auto` to automatically detect the number of CPUs on the system

```console
$ pytest -n auto test_parallel.py
============================= test session starts ==============================
plugins: xdist-1.32.0, forked-1.1.3, repeat-0.8.0, cov-2.8.1, mock-3.1.0
gw0 [10] / gw1 [10] / gw2 [10] / gw3 [10] / gw4 [10] / gw5 ok / gw6 [10] / gw7 ogw0 [10] / gw1 [10] / gw2 [10] / gw3 [10] / gw4 [10] / gw5 ok / gw6 [10] / gw7 [gw0 [10] / gw1 [10] / gw2 [10] / gw3 [10] / gw4 [10] / gw5 [10] / gw6 [10] / gw7 [10]
..........                                                               [100%]
============================== 10 passed in 3.02s ==============================
```

#### pytest-timeout: Put Time Limits on Your Tests

- The `pytest-timeout` plugin allows you pass a timeout period on the command line or mark individual tests with timeout periods in seconds
  - the mark overrides the command line timeout
    - `pytest.mark.timeout(timeout=0, method="thread|signal")`
- See: <https://pypi.org/project/pytest-timeout/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
Interrupt test run and dump stacks of all threads after a test times out:
  --timeout=TIMEOUT     Timeout in seconds before dumping the stacks. Default is
                        0 which means no timeout.
  --timeout_method={signal,thread}
                        Deprecated, use --timeout-method
  --timeout-method={signal,thread}
                        Timeout mechanism to use. 'signal' uses SIGALRM if
                        available, 'thread' uses a timer thread. The default is
                        to use 'signal' and fall back to 'thread'.
```

```console
$ pytest --timeout=0.5 -x test_parallel.py
============================= test session starts ==============================
...
plugins: timeout-1.3.4, xdist-1.32.0, forked-1.1.3, repeat-0.8.0, cov-2.8.1, mock-3.1.0
timeout: 0.5s
timeout method: signal
timeout func_only: False
collected 10 items

test_parallel.py F

=================================== FAILURES ===================================
______________________________ test_something[0] _______________________________

x = 0

    @pytest.mark.parametrize("x", list(range(10)))
    def test_something(x):
>       time.sleep(1)
E       Failed: Timeout >0.5s

test_parallel.py:7: Failed
=========================== short test summary info ============================
FAILED test_parallel.py::test_something[0] - Failed: Timeout >0.5s
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
============================== 1 failed in 0.60s ===============================
```

### Plugins That Alter or Enhance Output

- These plugins don't change how test are run, but they do change the output you see

#### pytest-instafail: See Details of Failures and Errors as They Happen

- If your test suite takes quite a bit of time, you may want to see the tracebacks as they happen, rather than wait until the end
- See: <https://pypi.org/project/pytest-instafail/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
reporting:
  ...
  --instafail           show failures and errors instantly as they occur
                        (disabled by default).
```

```console
$ pytest --instafail --timeout=0.5 --tb=line --maxfail=2 test_parallel.py
============================= test session starts ==============================
...
plugins: cov-2.8.1, mock-3.1.0, instafail-0.4.1.post0
timeout: 0.5s
timeout method: signal
timeout func_only: False
collected 10 items

test_parallel.py F

/path/to/appendices/xdist/test_parallel.py:7: Failed: Timeout >0.5s

test_parallel.py F

/path/to/appendices/xdist/test_parallel.py:7: Failed: Timeout >0.5s

=========================== short test summary info ============================
FAILED test_parallel.py::test_something[0] - Failed: Timeout >0.5s
FAILED test_parallel.py::test_something[1] - Failed: Timeout >0.5s
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 2 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
============================== 2 failed in 1.04s ===============================
```

#### pytest-sugar: Instafail + Colors + Progress Bar

- Lets you see status not just as characters, but also in color
- Also shows failure and error tracebacks during execution, and has a cool progress bar to the right of the shell
- See: <https://pypi.org/project/pytest-sugar/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
reporting:
  ...
  --old-summary         Show tests that failed instead of one-line tracebacks
  --force-sugar         Force pytest-sugar output even when not in real terminal
```

```console
$ pytest test_parallel.py
Test session starts (platform: linux, Python 3.6.9, pytest 5.4.1, pytest-sugar 0.9.3)
...
plugins: timeout-1.3.4, sugar-0.9.3, cov-2.8.1, mock-3.1.0
collecting ...
 test_parallel.py ✓✓✓✓✓✓✓✓✓✓                                     100% ██████████

Results (10.09s):
      10 passed
```

```console
$ pytest --timeout=0.5 --tb=line --maxfail=2 test_parallel.py
Test session starts (platform: linux, Python 3.6.9, pytest 5.4.1, pytest-sugar 0.9.3)
...
plugins: timeout-1.3.4, sugar-0.9.3, cov-2.8.1, mock-3.1.0
timeout: 0.5s
timeout method: signal
timeout func_only: False
collecting ...
/home/jashburn/devel/sandbox/python/python-testing-with-pytest/appendices/xdist/test_parallel.py:7: Failed: Timeout >0.5s

 test_parallel.py ⨯                                               10% █
/home/jashburn/devel/sandbox/python/python-testing-with-pytest/appendices/xdist/test_parallel.py:7: Failed: Timeout >0.5s

 test_parallel.py ⨯                                               20% ██
=========================== short test summary info ============================
FAILED test_parallel.py::test_something[0] - Failed: Timeout >0.5s
FAILED test_parallel.py::test_something[1] - Failed: Timeout >0.5s
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 2 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!

Results (1.05s):
       2 failed
         - test_parallel.py:5 test_something[0]
         - test_parallel.py:5 test_something[1]
```

#### pytest-emoji: Add Some Fun to Your Tests

- Allows you to replace all of the test status characters with emojis
- A small plugin and is a good example on which to base your own plugins
- Allows you to change the emoji using hook functions
  - one of the few pytest plugins that demonstrates how to add hook functions to plugin code
- See: <https://pypi.org/project/pytest-emoji/>

#### pytest-html: Generate HTML Reports for Test Sessions

- Useful in conjunction with continuous integration, or in systems with large, long-running test suites
- Creates a webpage to view the test results for a pytest session
- See: <https://pypi.org/project/pytest-html/>

```console
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

...
reporting:
  ...
  --html=path           create html report file at given path.
  --self-contained-html
                        create a self-contained html file containing all
                        necessary styles, scripts, and images - this means that
                        the report may not render or function where CSP
                        restrictions are in place (see
                        https://developer.mozilla.org/docs/Web/Security/CSP)
  --css=path            append given css file content to report style file.
```

```console
$ pytest --html=report.html
============================= test session starts ==============================
...
plugins: metadata-1.9.0, timeout-1.3.4, cov-2.8.1, mock-3.1.0, html-2.1.1
collected 6 items

test_outcomes.py .FxXsE                                                  [100%]

==================================== ERRORS ====================================
_________________________ ERROR at setup of test_error _________________________

    @pytest.fixture()
    def flaky_fixture():
>       assert 1 == 2
E       assert 1 == 2

test_outcomes.py:29: AssertionError
=================================== FAILURES ===================================
__________________________________ test_fail ___________________________________

    def test_fail():
>       assert 1 == 2
E       assert 1 == 2

test_outcomes.py:9: AssertionError
- generated html file: file:///path/to/appendices/outcomes/report.html -
=========================== short test summary info ============================
FAILED test_outcomes.py::test_fail - assert 1 == 2
ERROR test_outcomes.py::test_error - assert 1 == 2
==== 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.16s =====
```

### Plugins for Static Analysis

#### pytest-pycodestyle, pytest-pep8: Comply with Python's Style Guide

- Use the `pytest-pycodestyle` plugin to run `pycodestyle` on code in your project, including test code, with the `--pycodestyle` flag

#### pytest-flake8: Check for Style Plus Linting

- With the `pytest-flake8` plugin, you can run all of your source code and test code through flake8 and get a failure if something isn't right
  - checks for PEP 8, as well as for logic errors
  - use the `--flake8` option to run `flake8` during a pytest session
- You can extend flake8 with plugins that offer even more checks, such as `flake8-docstrings`

### Plugins for Web Development

#### pytest-selenium: Test with a Web Browser

- The `pytest-selenium` plugin is the Python binding for Selenium
- With it, you can
  - launch a web browser and use it to open URLs
  - exercise web applications
  - fill out forms
  - programmatically control the browser to test a web site or web application

#### pytest-django: Test Django Applications

- By default, the builtin testing support in Django is based on unittest
- The `pytest-django` plugin allows you to use pytest instead of unittest
  - includes helper functions and fixtures to speed up test implementation

#### pytest-flask: Test Flask Applications

- The `pytest-flask` plugin provides a handful of fixtures to assist in testing Flask applications

## A4. Packaging and Distributing Python Projects

### Creating an Installable Module

- For a simple one-module project, the minimal configuration is small

```text
​some_module_proj/
​├── setup.py
​└── some_module.py
```

- The code we want to share is in `some_module.py`
- To make it installable with pip, we need a [`setup.py`](appendices/packaging/some_module_proj/setup.py) file

```console
$ pip install ./some_module_proj
Processing ./some_module_proj
Installing collected packages: some-module
  Running setup.py install for some-module ... done
Successfully installed some-module-0.0.0
```

```console
$ python
Python 3.6.9 (default, Apr 18 2020, 01:56:04)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from some_module import some_func
>>> some_func()
42
>>>
```

### Creating an Installable Package

```text
some_package_proj
├── setup.py
└── src
    └── some_package
        ├── __init__.py
        └── some_module.py
```

- `__init__.py` needs to be written to expose the module functionality to the outside world through the package namespace
  - see: <https://docs.python.org/3/tutorial/modules.html#packages>
- If we do something like this in `__init__.py`:

```python
import some_package.some_module
```

- The client code will have to specify:

```python
import some_package
some_package.some_module.some_func()
```

- [`some_package/__init__.py`](appendices/packaging/some_package_proj/src/some_package/__init__.py)
  - expose everything in it to the package level
  - client code can do this:

```python
import some_package
some_package.some_func()
```

- [`some_package_proj/setup.py`](appendices/packaging/some_package_proj/setup.py)
  - specify packages

```console
$ pip install ./some_package_proj/
Processing ./some_package_proj
Installing collected packages: some-package
  Running setup.py install for some-package ... done
Successfully installed some-package-0.0.0
```

```console
$ python
Python 3.6.9 (default, Apr 18 2020, 01:56:04)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from some_package import some_func
>>> some_func()
42
>>>
```

- You can add a `tests` directory at the same level of `src` to add our tests

### Creating a Source Distribution and Wheel

```text
some_package_proj_v2/
├── CHANGELOG.rst
├── LICENSE
├── README.rst
├── setup.py
└── src
    └── some_package
        ├── __init__.py
        └── some_module.py
```

```console
$ pip install --upgrade setuptools wheel
```

```console
$ python setup.py sdist bdist_wheel
running sdist
running egg_info
creating src/some_package.egg-info
writing src/some_package.egg-info/PKG-INFO
writing dependency_links to src/some_package.egg-info/dependency_links.txt
writing top-level names to src/some_package.egg-info/top_level.txt
writing manifest file 'src/some_package.egg-info/SOURCES.txt'
reading manifest file 'src/some_package.egg-info/SOURCES.txt'
writing manifest file 'src/some_package.egg-info/SOURCES.txt'
running check
creating some_package-1.0
creating some_package-1.0/src
creating some_package-1.0/src/some_package
creating some_package-1.0/src/some_package.egg-info
copying files to some_package-1.0...
copying README.rst -> some_package-1.0
copying setup.py -> some_package-1.0
copying src/some_package/__init__.py -> some_package-1.0/src/some_package
copying src/some_package/some_module.py -> some_package-1.0/src/some_package
copying src/some_package.egg-info/PKG-INFO -> some_package-1.0/src/some_package.egg-info
copying src/some_package.egg-info/SOURCES.txt -> some_package-1.0/src/some_package.egg-info
copying src/some_package.egg-info/dependency_links.txt -> some_package-1.0/src/some_package.egg-info
copying src/some_package.egg-info/top_level.txt -> some_package-1.0/src/some_package.egg-info
Writing some_package-1.0/setup.cfg
creating dist
Creating tar archive
removing 'some_package-1.0' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/some_package
copying src/some_package/some_module.py -> build/lib/some_package
copying src/some_package/__init__.py -> build/lib/some_package
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/some_package
copying build/lib/some_package/some_module.py -> build/bdist.linux-x86_64/wheel/some_package
copying build/lib/some_package/__init__.py -> build/bdist.linux-x86_64/wheel/some_package
running install_egg_info
Copying src/some_package.egg-info to build/bdist.linux-x86_64/wheel/some_package-1.0-py3.6.egg-info
running install_scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build/bdist.linux-x86_64/wheel/some_package-1.0.dist-info/WHEEL
creating 'dist/some_package-1.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'some_package/__init__.py'
adding 'some_package/some_module.py'
adding 'some_package-1.0.dist-info/LICENSE'
adding 'some_package-1.0.dist-info/METADATA'
adding 'some_package-1.0.dist-info/WHEEL'
adding 'some_package-1.0.dist-info/top_level.txt'
adding 'some_package-1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
```

```console
$ pip install --no-index --find-links=dist some_package
Collecting some_package
Installing collected packages: some-package
Successfully installed some-package-1.0
```

## Sources

- Okken, Brian. _Python Testing with Pytest: Simple, Rapid, Effective, and Scalable_. The Pragmatic Bookshelf, 2017.
