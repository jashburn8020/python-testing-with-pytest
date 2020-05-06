# Python Testing with pytest

- [Python Testing with pytest](#python-testing-with-pytest)
  - [Getting Started with pytest](#getting-started-with-pytest)
    - [Using Options](#using-options)
  - [Writing Test Functions](#writing-test-functions)
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
  - [pytest Fixtures](#pytest-fixtures)
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
  - [Sources](#sources)

## Getting Started with pytest

```console
​$ ​​pytest​​ ​​--help​
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
  - e.g., `​​pytest​​ ​​​​tasks/test_four.py::test_asdict`

### Using Options

- Some useful pytest command line options
- `--collect-only`
  - shows you which tests will be run with the given options and configuration
  - e.g., when used in conjunction with `-k`
- `-k`
  - use an expression to find what test functions to run
  - e.g., `pytest​​ ​​-k​​ ​​"asdict or defaults"​​`
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

## Writing Test Functions

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
​$ ​​cd​​ ​​/path/to/code/ch2/tasks_proj/tests/unit​
$ ​​pytest​​ ​​test_task.py​
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
  - `​​​pytest​​ ​​tests/func`

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
  - `pytest​​ ​​tests/func/test_add.py`

#### A Single Test Function

- To run a single test function, add `::` and the test function name
  - `pytest​​​ ​​tests/func/test_add.py::test_add_returns_valid_id​`

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
  - `pytest​​ ​​tests/func/test_api_exceptions.py::TestUpdate​`

#### A Single Test Method of a Test Class

- If you want to run just one method, add another `::` and the method name
  - `​​pytest​​ ​​tests/func/test_api_exceptions.py::TestUpdate::test_bad_id​`

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

## pytest Fixtures

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

## Sources

- Okken, Brian. _Python Testing with Pytest: Simple, Rapid, Effective, and Scalable_. The Pragmatic Bookshelf, 2017.
