"""
-------------------------------------------------------
linked_list_test.py
-------------------------------------------------------
Author:  Adam Cassidy
ID:      161818720
Email:   cass8720@mylaurier.ca
__updated__ = 2017-10-27
-------------------------------------------------------
"""
from list_linked import List
from movie import Movie


def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    Use: list_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of List are tested for both empty and 
        non-empty lists using the data in a:
        is_empty, insert, remove, append, index, __contains__,
        find, max, min, __getitem__, __setitem__
    -------------------------------------------------------
    """
    l = List()
    m = Movie("Dark City", 1998, None, None, None)

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print("Empty list: {}".format(l.is_empty()))
    for i in a:
        l.append(i)
    print("Items append to list:")
    print("Len: {}".format(len(l)))
    l.insert(5, m)
    print("Insert value copy of Dark city title and year to index 5")
    if not l.is_empty():
        print("Index of Dark City: {}".format(l.index(m)))
        print("Contains 'Dark City': {}".format(m in l))
        print("Getitem index 2: {}".format(l[2]))
    else:
        print("list is empty.")
    print("Len: {}".format(len(l)))
    print("Max: {}".format(l.max()))
    print("Min: {}".format(l.min()))
    print("End result:")
    for j in l:
        print("{}".format(j), end="")

    return
