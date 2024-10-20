"""Week 6 Perform - Part 2"""
# file name: w06_markus.py
#
# Complete the following steps:
#  (1) Complete the following function according to its docstring.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101
#      w06_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When you are convinced that your function is correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


def count_odds(values: list[list[int]]) -> list[int]:
    """Return a list of counts of odd numbers in each of the inner lists of
    values.

    >>> count_odds([[111, 165, 207]])
    [3]
    >>> count_odds([[1, 2], [8], [5, 6, 7]])
    [1, 0, 2]
    """
    odd_counts = []
    
    for sublist in values:
        # Count the odd numbers in the sublist
        count = sum(1 for x in sublist if x % 2 != 0)
        odd_counts.append(count)
    
    return odd_counts