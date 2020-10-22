"""
-------------------------------------------------------
test_sorts_array.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-03-19
-------------------------------------------------------
"""
from copy import deepcopy
import random

from number import Number
from sorts_array import Sorts


# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Create a sorted list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a sorted list of SIZE Number objects.
    -------------------------------------------------------
    """

    a = []
    for i in range(0, SIZE):
        a.append(Number(i))
    return a


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a reversed list of SIZE Number objects.
    -------------------------------------------------------
    """
    a = []
    for i in range(0, SIZE):
        a.insert(0, Number(i))
    values = a

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE.
    -------------------------------------------------------
    """

    arrays = []
    for j in range(0, TESTS):
        temp = random.sample(range(XRANGE), SIZE)
        a = []
        for i in range(0, SIZE):
            a.append(Number(temp[i]))
        arrays.append(a)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and print out
    its comparisons for sorted, reversed, and random arrays
    of data.
    -------------------------------------------------------
    Preconditions:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Postconditions:
        prints the number of comparisons necessary to sort an
        array: in order, in reverse order, and a list of arrays
        in random order.
    -------------------------------------------------------
    """

    Sorts.swaps = 0
    Number.comparisons = 0

    csorted = create_sorted()
    func(csorted)
    sortswap = Sorts.swaps
    sortcomp = Number.comparisons
    Sorts.swaps = 0
    Number.comparisons = 0

    creversed = create_reversed()
    func(creversed)
    revswap = Sorts.swaps
    revcomp = Number.comparisons
    Sorts.swaps = 0
    Number.comparisons = 0

    randoms = create_randoms()
    for i in randoms:
        func(i)
    randswap = Sorts.swaps // TESTS
    randcomp = Number.comparisons // TESTS
    Sorts.swaps = 0
    Number.comparisons = 0

    print("{:>18} {:>9} {:>9}  {:>9} {:>9} {:>9}".format(
        int(sortcomp), int(revcomp), int(randcomp), int(sortswap), int(revswap), int(randswap)))

    return
