"""CSC108: Fall 2021 -- Assignment 1: Unscramble

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton,
Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

import sys
import subprocess
import importlib
from typing import Tuple

PYTHON_TA_VERSION = '2.8.1'


def python_ta_installed() -> bool:
    """Return True if PythonTA is installed."""
    try:
        import python_ta
        importlib.reload(python_ta)
        installed_version = python_ta.__version__
        return installed_version == PYTHON_TA_VERSION
    except:
        return False


def install_python_ta():
    """Tries to install PythonTA."""
    if not python_ta_installed():
        print("[Installing the style checker] Attempt #1 ...")
        try:
            subprocess.Popen(f'python3 -m pip install python-ta=={PYTHON_TA_VERSION}', shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        except:
            pass

    if not python_ta_installed():
        print("[Installing the style checker] Attempt #2 ...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                                   f'python-ta=={PYTHON_TA_VERSION}'],
                                  stderr=subprocess.DEVNULL,
                                  stdout=subprocess.DEVNULL)
        except:
            pass


def run_pyta(filename: str, config_file: str) -> None:
    """Run PYTA with configuration config_file on the file named filename.
    """
    import json
    install_python_ta()

    error_message = '\nCould not install or run the style checker correctly.\n' \
                    'Please try to re-run the checker once.\n' \
                    'If you have already tried to re-run it, please go to office hours\n' \
                    'in order to resolve this.' \
                    'For now, you may upload your code to MarkUs and run the self-test\n' \
                    'to see the style checker results.'

    try:
        import python_ta
        with open(config_file) as cf:
            config_dict = json.loads(cf.read())
            config_dict['output-format'] = 'python_ta.reporters.PlainReporter'

        python_ta.check_all(filename, config=config_dict)
    except:
        print(error_message)


def check(func: callable, args: list,
          expected: type) -> Tuple[bool, object]:
    """Check if func(args) returns a result of type expected.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.
    """

    try:
        returned = func(*args)
    except Exception as exn:
        return (False, _error_message(func, args, exn))

    if isinstance(returned, expected):
        return (True, returned)

    return (False, _type_error_message(func, expected, returned))


def _type_error_message(func: callable, expected: type,
                        got: object) -> str:
    """Return an error message for function func returning got, where the
    correct return type is expected.

    """

    return ('{} should return a {}, but returned {}' +
            '.').format(func.__name__, expected.__name__, got)


def _error_message(func: callable, args: list,
                   error: Exception) -> str:
    """Return an error message: func(args) raised an error."""

    return 'The call {}({}) caused an error: {}'.format(
        func.__name__, ','.join(map(str, args)), error)
