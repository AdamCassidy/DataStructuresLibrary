"""
-------------------------------------------------------
sorted_list_linked.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-03-01
-------------------------------------------------------
"""

# Imports
from copy import deepcopy


class _SLNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SLNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            next_ - another sorted list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class SortedList:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty sorted list.
        Use: sl = SortedList()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty sorted list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        i = 0

        if self._count == 0 or value is None:
            # Insert a new node into the front of the list.
            self._front = _SLNode(value, self._front)
            self._count += 1
        elif self._count == 1:
            if value > current._data:
                current._next = _SLNode(value, None)
                self._count += 1
            else:
                self._front = _SLNode(value, self._front)
                self._count += 1
        else:
            while i < (self._count - 1) and current is not None:
                # find the proper location in the list
                if current._data > value:
                    break
                previous = current
                current = current._next
                i += 1

            if current != None:
                if current == self._front:
                    self._front = _SLNode(value, self._front)
                    self._count += 1
                elif current._data < value:
                    current._next = _SLNode(value, None)
                    self._count += 1

                elif previous != None:
                    previous._next = _SLNode(value, current)
                    self._count += 1

        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        current = self._front
        previous = None
        index = -1
        count = 0

        if self._count != 0:
            while count < (self._count - 1) and current is not None and current._data != key:
                previous = current
                current = current._next
                count += 1

            if current != None:
                if key == current._data:
                    index = count

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        _, _, i = self._linear_search(key)

        if i > -1:
            value = self.pop(i)
            self._count -= 1
        else:
            value = None

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find in an empty list"

        _, current, i = self._linear_search(key)
        value = None

        if i > -1:
            value = deepcopy(current._data)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = self._front._data

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)

        return i

    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Preconditions:
            i - an index value (int)
        Postconditions:
            returns
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
        Postconditions:
            returns
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._data)

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        _, _, i = self._linear_search(key)

        return i != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        n = 0
        value = None

        while n < (self._count - 1) and current != None:
            current = current._next
            n += 1

        if current != None:
            value = current._data

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        value = self._front._data

        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """

        number = 0
        n = 0
        current = self._front

        while n < (self._count - 1) and current != None:
            if current._data == key:
                number += 1
            elif number > 0:
                break
            current = current._next
            n += 1

        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        n = 0
        current = self._front
        previous = None

        if self._count != 0 and self._count != 1:
            while n < (self._count - 1) and current != None:
                previous = current
                current = current._next
                while previous._data == current._data:
                    current = current._next
                    self._count -= 1
                    n += 1
                previous._next = current
                n += 1

        return

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Preconditions:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Postconditions:
            returns
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._data

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (SortedList)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (SortedList)
        -------------------------------------------------------
        """

        new_list = SortedList()
        n = 0
        current = self._front

        if self._count == 0:
            pass
        elif rs._count == 0:
            pass
        else:
            current = self._front
            while n < self._count and current != None:
                _, _, i = new_list._linear_search(current._data)
                _, _, rs_i = rs._linear_search(current._data)
                if i == -1 and rs_i != -1:
                    new_list.insert(current._data)
                current = current._next
                n += 1

            if n == self._count:
                _, _, i = new_list._linear_search(current._data)
                _, _, rs_i = rs._linear_search(current._data)
                if i == -1 and rs_i != -1:
                    new_list.insert(current._data)

        return new_list

    def union(self, rs):
        """
        -------------------------------------------------------
        Copies all of the values in both self and rs to
        a new List. Each value appears only once. (iterative)
        -------------------------------------------------------
        Preconditions:
            rs - another List (SortedList)
        Postconditions:
            Returns:
            new_list - a List containing one copy each of all values
            in both self and rs. (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()

        if self._count == 0:
            new_list = deepcopy(rs)
        elif rs._count == 0:
            new_list = deepcopy(self)
        else:
            n = 0
            current = self._front
            rs_current = rs._front

            while n < (self._count - 1) and current != None:
                _, _, i = new_list._linear_search(current._data)
                if i == -1:
                    new_list.insert(current._data)
                current = current._next
                n += 1

            if n == (self._count - 1):
                _, _, i = new_list._linear_search(current._data)
                if i == -1:
                    new_list.insert(current._data)

            n = 0

            while n < (rs._count - 1) and current != None:
                _, _, i = new_list._linear_search(rs_current._data)
                if i == -1:
                    new_list.insert(rs_current._data)
                rs_current = rs_current._next
                n += 1

            if n == (rs._count - 1):
                _, _, i = new_list._linear_search(rs_current._data)
                if i == -1:
                    new_list.insert(rs_current._data)

        return new_list

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = sl.remove_front()
        -------------------------------------------------------
        Postconditions:
          Returns:
          value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """

        value = None

        if self._count != 0:
            if self._front != None:
                value = self._front._data
                self._front = self._front._next

        return value

    def _reverse(self):
        """
        -------------------------------------------------------
        Helper method - reverses the order of the elements in list.
        Use: l._reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next
