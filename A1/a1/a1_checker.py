"""CSC108: Fall 2024 -- Assignment 1: Wordlock

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 CSC108 Teaching Team
"""

from typing import Any, Dict
import unittest
import checker_generic
import wordlock_functions as uf

PYTA_CONFIG = 'a1_pyta.json'
FILENAME = 'wordlock_functions.py'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {
    'ROTATE': 'R', 'SWAP': 'S', 'CHECK': 'C', 'HINT_MODE_SECTION_LENGTH': 3
}


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_get_section_start(self) -> None:
        """Function get_section_start."""
        self._check(uf.get_section_start, [3, 5], int)

    def test_modify_section(self) -> None:
        """Function modify_section."""
        self._check(uf.modify_section, ['TACDOGOFXMUE', 'S', 1, 3], str)

    def test_check_section(self) -> None:
        """Function check_section."""
        self._check(uf.check_section, ['CATDGOXOFMUE', 'CATDOGFOXEMU', 2, 3], bool)

    def test_is_valid_move(self) -> None:
        """Function is_valid_move."""
        self._check(uf.is_valid_move, ['F'], bool)

    def test_is_valid_section(self) -> None:
        """Function is_valid_section."""
        self._check(uf.is_valid_section, [6, 'CATDOGEMUFOX', 2], bool)

    def test_get_num_sections(self) -> None:
        """Function get_num_sections."""
        self._check(uf.get_num_sections, ['CATDOGEMUFOX', 2], int)

    def test_section_needs_swap(self) -> None:
        """Function section_needs_swap."""
        self._check(uf.section_needs_swap, ['CATGDOMUEXOF', 'CATDOGEMUFOX', 2], bool)

    def test_get_move_hint(self) -> None:
        """Function get_move_hint."""
        self._check(uf.get_move_hint, ['TACDOGEMUFOX', 'CATDOGEMUFOX', 3], str)

    def test_check_constants(self) -> None:
        """Values of constants."""

        print('\nChecking that constants refer to their original values')
        self._check_constants(CONSTANTS, uf)
        print('  check complete')

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete')

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            self.assertEqual(expected, actual, msg)


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
