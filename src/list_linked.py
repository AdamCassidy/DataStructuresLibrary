"""
-------------------------------------------------------
list_linked.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-02-15
-------------------------------------------------------
"""

from copy import deepcopy


class _ListNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            _data - data value for node (?)
            _next - another list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
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
            returns
            True if the list is empty, False otherwise.
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
            returns
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the list at index i.
        Use: l.insert(i, value)
        -------------------------------------------------------
        Preconditions:
            i - index value (int)
            value - a data element (?)
        Postconditions:
            a copy of value is added to index i, all other values are pushed right
            If i outside of range of length of list, appended to end
        -------------------------------------------------------
        """
        if i < 0:
            # negative index
            i = self._count + i

        n = 0
        previous = None
        current = self._front

        while n < i and current is not None:
            # find the proper location in the list
            previous = current
            current = current._next
            n += 1

        if previous is None:
            # Insert a new node into the front of the list.
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            previous._next = _ListNode(value, current)
        self._count += 1
        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        self.insert(0, value)
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
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

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------
        """
        previous, current, index = self._linear_search_r_aux(
            None, self._front, 0, key)
        return previous, current, index

    def _linear_search_r_aux(self, previous, current, index, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------
        """

        if current is not None:
            if current._data == key:
                pass
            else:
                previous = current
                current = current._next
                previous, current, index = self._linear_search_r_aux(
                    previous, current, index + 1, key)
        else:
            previous = None
            current = None
            index = -1

        return previous, current, index

    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != rs._count:
            is_identical = False
        else:
            current1 = self._front
            current2 = rs._front

            while current1 is not None and current1._data == current2._data:
                current1 = current1._next
                current2 = current2._next

            is_identical = current1 is None
        return is_identical

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        current1 = self._front
        current2 = rs._front

        if self._count != rs._count:
            is_identical = False
        else:
            is_identical = self.identical_r_aux(rs, current1, current2)

        return is_identical

    def identical_r_aux(self, rs, current1, current2):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        if current1 is None and current2 is None:
            is_identical = True
        elif current1._data == current2._data:
            current1 = current1._next
            current2 = current2._next
            is_identical = self.identical_r_aux(rs, current1, current2)

        return is_identical

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        if self._count == 0:
            pass
        else:
            self.reverse_r_aux(self._front)
        return

    def reverse_r_aux(self, current):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """

        if current._next is None:
            self._front = current
        else:
            self.reverse_r_aux(current._next)
            current._next._next = current
            current._next = None
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
            The list is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()

        while self._front is not None:
            if even._front is None:
                even._front = _ListNode(self._front._data, None)
                ecurrent = even._front
                even._count += 1
            else:
                new_node = _ListNode(self._front._data, None)
                ecurrent._next = new_node
                ecurrent = ecurrent._next
                even._count += 1
            self._front = self._front._next

            if self._front is not None:
                if odd._front is None:
                    odd._front = _ListNode(self._front._data, None)
                    ocurrent = odd._front
                    odd._count += 1
                else:
                    new_node = _ListNode(self._front._data, None)
                    ocurrent._next = new_node
                    ocurrent = ocurrent._next
                    odd._count += 1
                self._front = self._front._next
        self._count = 0

        return even, odd

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
            The list is empty.
        -------------------------------------------------------
        """
        current = self._front
        even = List()
        odd = List()

        if self._count == 0:
            even = deepcopy(self)
        else:
            even, odd = self.split_alt_r_aux(current, even, odd)

        return even, odd

    def split_alt_r_aux(self, current, even, odd):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
            The list is empty.
        -------------------------------------------------------
        """
        if current is None:
            pass
        elif len(even) > len(odd):
            odd.append(current._data)
            current = current._next
            even, odd = self.split_alt_r_aux(current, even, odd)
        else:
            even.append(current._data)
            current = current._next
            even, odd = self.split_alt_r_aux(current, even, odd)
        return even, odd

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (List)
        -------------------------------------------------------
        """
        new_list = List()
        temp = rs._front
        current = self._front
        n = 0

        while temp is not None and current is not None and n < (rs._count - 1):
            if current._data == temp._data:
                new_list.insert(0, temp._data)
            current = current._next
            temp = temp._next

        return new_list

    def intersection_r(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (List)
        -------------------------------------------------------
        """
        current = self._front
        new_list = List()

        new_list = self.intersection_r_aux(current, rs)
        return new_list

    def intersection_r_aux(self, current, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (List)
        -------------------------------------------------------
        """
        if current is None:
            new_node = None
        else:
            _, _, i = rs._linear_search(current._data)
            if i != -1:
                new_node = _ListNode(current._data, None)
                new_node._next = self.intersection_r_aux(current._next, rs)
            else:
                new_node = self.intersection_r_aux(current._next, rs)
        return new_node

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = None
        count = 0
        current = self._front
        previous = None

        while count < (self._count - 1) and current._data != key:
            previous = current
            current = current._next
            count += 1

        if current != None:
            if current._data == key:
                value = current._data
                if current._data == self._front._data:
                    self._front = self._front._next
                else:
                    previous._next = current._next
                self._count -= 1

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._data
        self._front = self._front._next
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        count = 0
        current = self._front
        previous = None

        while count < (self._count - 1):
            if count == 0:
                while self._front._data == key:
                    self._front = self._front._next
                    current = self._front
                    self._count -= 1
                    count += 1
            previous = current
            current = current._next
            while current._data == key:
                current = current._next
                self._count -= 1
                count += 1
            previous._next = current
            count += 1

        if current._data == key:
            previous._next = None
            self._count -= 1

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        _, current, _ = self._linear_search(key)
        value = current._data

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

        assert self._count is not None, \
            "Cannot peek at an empty list"

        value = deepcopy(self._front._data)

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index(key)
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

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
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

        current._data = deepcopy(value)
        return

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

        current = self._front
        count = 0

        while count < self._count and current is not None and current._data != key:
            current = current._next
            count += 1

        if count == self._count:
            current = None

        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

# your c
        current = self._front
        count = 0
        max_data = deepcopy(self._front._data)

        while count < self._count and current is not None:
            if current._data > max_data:
                max_data = deepcopy(current._data)
            current = current._next
            count += 1

        if count == self._count:
            current = None

        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        count = 0
        min_data = deepcopy(self._front._data)

        while count < self._count and current._data is not None:
            if current._data < min_data:
                min_data = deepcopy(current._data)
            current = current._next
            count += 1

        if count == self._count:
            current = None

        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """

        number = 0
        current = self._front

        while current is not None:
            if key == current._data:
                number += 1
            current = current._next

        return number

    def append(self, value):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the List.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the List.
        -------------------------------------------------------
        """
        n = 0
        current = self._front
        while n < (self._count - 1):
            # find the proper location in the list
            current = current._next
            n += 1

        if current is None:
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            current._next = _ListNode(value, None)
        self._count += 1

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (iterative algorithm)
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        n = 0
        current = self._front
        previous = None
        temp = List()

        if self._count != 0 and self._count != 1:
            while current is not None:
                # find the proper location in the list
                if current._data in temp:
                    previous = current
                    while current._data in temp:
                        current = current._next
                        self._count -= 1
                        n += 1
                    previous._next = current
                if current is not None:
                    temp.append(current._data)
                    previous = current
                    current = current._next
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

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
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

    def union(self, rs):
        """
        -------------------------------------------------------
        Returns a list that contains all values in both
        the current List and rs. (iterative algorithm)
        Use: nl = l.union(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains all values found in both the current
            List and rs. Values do not repeat. (List)
        -------------------------------------------------------
        """

        new_list = List()

        if self._count == 0:
            new_list = deepcopy(rs)
        elif rs._count == 0:
            new_list = deepcopy(self)
        else:
            n = 0
            current = self._front
            rs_current = rs._front

            while n < (self._count - 1):
                _, _, i = new_list._linear_search(current._data)
                if i == -1:
                    new_list.append(current._data)
                current = current._next
                n += 1

            if n == (self._count - 1):
                _, _, i = new_list._linear_search(current._data)
                if i == -1:
                    new_list.append(current._data)

            n = 0

            while n < (rs._count - 1):
                _, _, i = new_list._linear_search(rs_current._data)
                if i == -1:
                    new_list.append(rs_current._data)
                rs_current = rs_current._next
                n += 1

            if n == (rs._count - 1):
                _, _, i = new_list._linear_search(rs_current._data)
                if i == -1:
                    new_list.append(rs_current._data)

        return new_list

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. ls contains the first half,
        rs the second half. Uses counting algorithm.
        Current list is empty.
        Use: ls, rs = l.split_th()
        -------------------------------------------------------
        Postconditions:
            returns
            ls - a new List with >= 50% of the original List (List)
            rs - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        ls = List()
        rs = List()
        current = self._front
        n = self._count

        if self.count != 0:
            while n > self._count // 2:
                ls.append(current._data)
                current = current._next
                n -= 1

            while n > 0:
                rs.append(current._data)
                current = current._next
                n -= 1

        self._front = None
        self._count = 0

        return ls, rs

    def combine(self, s2):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(s2)
        -------------------------------------------------------
        Preconditions:
            s2- an linked-based List (List)
        Postconditions:
            returns
            new_list - the contents of the current List and s2
            are interlaced into new_list - current List and s2
            are empty (List)
        -------------------------------------------------------
        """

        new_list = List()
        n = 0

        if self._count == 0:
            new_list = deepcopy(s2)
        elif s2._count == 0:
            new_list = deepcopy(self)
        else:
            current = self._front
            s2_current = s2._front

            while n < (self._count - 1) and n < (s2._count - 1):
                new_list.append(current._data)

                current = current._next
                if n < (s2._count - 1):
                    new_list.append(s2_current._data)
                    s2_current = s2_current._next
                n += 1

            while n < (self._count - 1) and current != None:
                new_list.append(current._data)
                current = current._next
                n += 1

            if n == (self._count - 1):
                if current._data:
                    new_list.append(current._data)

            while n < (s2._count - 1) and current != None:
                new_list.append(s2_current._data)
                s2_current = s2_current._next
                n += 1

            if n == (s2._count - 1):
                if s2_current._data:
                    new_list.append(s2_current._data)

        self._front = None
        s2._front = None
        self._count = 0
        s2._count = 0

        return new_list

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

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Preconditions:
            pln - node before list node to swap (_ListNode)
            prn - node before list node to swap (_ListNode)
        Postconditions:
            The nodes in pln.next and prn.next have been swapped,
                and all links to them updated.
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                l = self._front
                self._front = prn._next
            else:
                l = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                r = self._front
                self._front = l
            else:
                r = prn._next
                prn._next = l

            # Swap next pointers
            # l._next, r._next = r._next, l._next
            temp = l._next
            l._next = r._next
            r._next = temp
        return
