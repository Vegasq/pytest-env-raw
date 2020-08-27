"""Adopt environment section in pytest configuration files."""

import os
import pytest


def pytest_addoption(parser):
    """Add section to configuration files."""
    help_msg = (
        "a line separated list of environment variables of the form NAME=VALUE."
    )

    parser.addini("envraw", type="linelist", help=help_msg, default=[])


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    """Load environment variables from configuration files."""
    for e in early_config.getini("envraw"):
        part = e.partition("=")
        key = part[0].strip()
        value = part[2].strip()
        os.environ[key] = value
