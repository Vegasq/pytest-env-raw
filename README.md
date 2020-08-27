Simplifyed fork of [https://github.com/MobileDynasty/pytest-env](https://github.com/MobileDynasty/pytest-env)

I got a value like `aaaaaa{bbb}aaaaa` I wanted to put in ENV, and `pytest-env` have no way to _not_ act like it's an f-string.

# pytest-envraw

This is a py.test plugin that enables you to set environment variables in the pytest.ini file.

## Installation

Install with pip:

    pip install pytest-envraw

Uninstall with pip:

    pip uninstall pytest-envraw

## Usage

In your pytest.ini file add a key value pair with `envraw` as the key and the environment variables as a line separated list of `KEY=VALUE` entries.  The defined variables will be added to the environment before any tests are run:

    [pytest]
    envraw =
        HOME=~/tmp
        RUN_ENV=test
