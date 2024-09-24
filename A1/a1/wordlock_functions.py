"""CSC108: Fall 2024 -- Assignment 1: Wordlock

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 CSC108 Teaching Team
"""

# Move constants
ROTATE = 'R'
SWAP = 'S'
CHECK = 'C'

# Constant for hint functions
HINT_MODE_SECTION_LENGTH = 3


def get_section_start(section_num: int, section_len: int) -> int:
    """Return the starting index of the section corresponding to section_num
    if the length of a section is section_len.

    >>> get_section_start(1, 3)
    0
    >>> get_section_start(2, 3)
    3
    >>> get_section_start(3, 3)
    6
    >>> get_section_start(4, 3)
    9
    """
    # write your code for get_section_start here

#write the rest of your functions here 
