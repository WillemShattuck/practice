"""
Testing library for MyList class 
"""

import pytest
from my_list import MyList as mlist


def test_len_simple():

    """
    simple test of len
    """
    lst = mlist()

    lst.append(33)
    lst.append(22)

    assert len(lst) == 2


def test_len_with_pop():
    """
    Append 3 elements and pop one
    """


pytest.main()
