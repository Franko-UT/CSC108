"""Week 3 Perform - Part 2"""

"""
# w03_markus.py
# Frank Lou
"""
# w03_markus.py
#
# Complete the following steps:
#  (1) Complete the following functions according to their docstrings.
#  (2) Save your file after you make changes, and then run the file by 
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101 
#      w03_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your functions in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your functions using different function arguments.
#  (5) When you are convinced that your functions are correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in last week's Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


def is_odd(value: int) -> bool:
    """Return True if and only if value is an odd number.
    
    >>> is_odd(108)
    False
    >>> is_odd(165)
    True
    """
    if value % 2 == 1 :
        ture = bool(1)
        return ture


def convert_time(hour_24: int) -> int:
    """Return the 12-hour-clock hour that corresponds to the given 
    24-hour-clock hour hour_24.

    Precondition: 0 <= hour_24 <= 23

    >>> convert_time(0)
    12
    >>> convert_time(4)
    4
    >>> convert_time(12)
    12
    >>> convert_time(15)
    3
    """
    if hour_24 != 0:
        hour_12 = int ( ( hour_24 - 1 ) % 12 + 1 )
    elif  hour_24 == 0:
        hour_12 = 12
    return hour_12

