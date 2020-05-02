# Python Testing with pytest

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

# Sources

- Okken, Brian. _Python Testing with Pytest: Simple, Rapid, Effective, and Scalable_. The Pragmatic Bookshelf, 2017.
