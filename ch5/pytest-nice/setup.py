"""Setup for pytest-nice plugin."""

from setuptools import setup

# Minimal setup() - required fields
setup(
    name="pytest-nice",
    version="0.1.0",
    description="A pytest plugin to turn FAILURE into OPPORTUNITY",
    url="https://wherever/you/have/info/on/this/package",
    author="Your Name",  # or maintainer
    author_email="your_email@somewhere.com",  # or maintainer_email
    license="proprietary",
    py_modules=["pytest_nice"],  # Module(s) for this plugin
    install_requires=["pytest"],
    # pytest11 is a special identifier that pytest looks for
    # nice is the name of our plugin
    # pytest_nice is the name of the module where our plugin lives
    entry_points={"pytest11": ["nice = pytest_nice",],},
)
