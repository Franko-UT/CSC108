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
    return ( section_num - 1 )  * section_len
#write the rest of your functions here
 
def get_section_start(section1:int, section2:int) -> int :
    index_section = int ( ( section1 - 1 ) * section2 )
    return index_section


def is_valid_move(mvmt:str) -> bool :
    if mvmt == "R" or mvmt == "C" or mvmt == "S":
        return True
    return False

def get_num_sections(correctstr:str, section:int) -> int :
    num_section = int ( len ( correctstr ) / section)
    return num_section

def is_valid_section(inputsec: int, ans: str, sec: int) -> bool :
    if 0 < inputsec <= len ( ans ) / sec :
        return True
    return False

def check_section(crt_section:str, ans:str, sec_num:int, sec_len:int) -> bool :
    if crt_section == ans[ ( sec_num - 1 ) * sec_len : ( sec_num ) * sec_len ] :
        return True
    return False

def modify_section(move_state:str, gamestr:str, sec_num:int, sec_len:int) -> str :
    if move_state == "S":
        temp = gamestr [ ( sec_num - 1 ) * sec_len ]
        gamestring = list ( gamestr )
        gamestring [ ( sec_num - 1 ) * sec_len ] = gamestr [ ( sec_num ) * sec_len - 1 ]
        gamestring [ ( sec_num ) * sec_len - 1] = temp
    elif move_state == "R":
        temp = gamestr [ ( sec_num ) * sec_len - 1 ]
        gamestring = list (gamestr)
        for i in range ( sec_len ):
            gamestring [ ( sec_num ) * sec_len - i ] = gamestring [ ( sec_num ) * sec_len - i - 1]
        gamestring [ ( sec_num - 1 ) * sec_len ] = temp 
    donestring = "".join (gamestring)
    return donestring

def section_needs_swap(currentstatus:str, ans:str, lenth:int) -> bool :
    currentstatus