"""
-------------------------------------------------------
sorts_list_linked.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-03-19
-------------------------------------------------------
"""
from copy import deepcopy
from hash_set_array import HashSet
from list_linked import List


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Selection Sort algorithm.
        Finds maximum value each pass.
        Use: selection_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked list of comparable elements (List)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        # Split the list into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None
        # Go through each node in the unsorted list and find the max value
        # to insert at the front of the sorted list.
        while unsorted is not None:
            max_prev = None
            max_node = unsorted
            previous = unsorted
            current = max_node._next

            while current is not None:
                if current._data > max_node._data:
                    max_prev = previous
                    max_node = current
                previous = current
                current = current._next

            Sorts.swaps += 1
            # Remove the max node from the list.
            if max_prev is None:
                unsorted = max_node._next
            else:
                max_prev._next = max_node._next
            # Move the next max node to the front of the sorted list.
            max_node._next = a._front
            a._front = max_node
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Bubble Sort algorithm.
        Use: bubble_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked list of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        done = False
        last = None

        while not done:
            # if no elements have been swapped, then the list is sorted
            done = True
            # Get the front of the list.
            previous = None
            current = a._front
            swapped = a._front

            while current is not last and current._next is not None:

                if current._data > current._next._data:
                    # If you swapped you need another pass.
                    done = False
                    # The pair current, current._next is out of order.
                    Sorts.swaps += 1
                    a._swap(previous, current)
                    # Keep track of last node swapped
                    swapped = current
                    # current is unchanged - update previous
                    if previous is None:
                        previous = a._front
                    else:
                        previous = previous._next
                else:
                    # Move to next node.
                    previous = current
                    current = current._next
            last = swapped
        # done == True iff no pair of keys was swapped on the last pass.
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an List using the Comb Sort algorithm.
        Use: comb_sort(a)
        -------------------------------------------------------
        Preconditions:
          a - a linked list of comparable elements (?)
        Postconditions:
          Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)

        if n > 0:
            gap = n
            done = False

            while gap > 1 or not done:
                done = True
                previous = None
                current = a._front
                gap = int(gap / 1.3)

                if gap < 1:
                    gap = 1

                i = 0
                prev_far = current
                far = current._next
                # Move to the far node for comparison.
                while i < gap - 1 and far is not None:
                    prev_far = far
                    far = far._next
                    i += 1

                while current is not None and far is not None:
                    if current._data > far._data:
                        Sorts.swaps += 1
                        a._swap(previous, prev_far)
                        done = False
                    # Increment all nodes.
                    prev_far = far
                    far = far._next
                    previous = current
                    current = current._next
        return

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Insertion Sort algorithm.
        Use: insertion_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked list of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        # Split the list into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None

        # Go through each node in the unsorted list and insert it into the
        # proper position in the sorted list.
        while unsorted is not None:
            # Isolate the first node of the unsorted list.
            node = unsorted
            unsorted = unsorted._next
            # Find the proper place for the new node in the sorted so far list.
            # (Very similar to priorityQueue insertion.)
            previous = None
            current = a._front

            while current is not None and current._data < node._data:
                previous = current
                current = current._next

            # Insert node into the proper place in the sorted list.
            Sorts.swaps += 1

            if previous is None:
                node._next = a._front
                a._front = node
            else:
                node._next = current
                previous._next = node
        return

    @staticmethod
    def merge_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Merge Sort algorithm.
        Use: merge_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked list of comparable elements (List)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        a._front = Sorts._merge_sort_aux(a._front)
        return

    @staticmethod
    def _merge_sort_aux(current):
        """
        -------------------------------------------------------
        Divides a linked list into halves, sorts each half, then
        merges the halves back together.
        Use: current = _merge_sort_aux(current)
        -------------------------------------------------------
        Preconditions:
          current - pointer to a List node (_ListNode)
        Postconditions:
          returns:
          current - pointer to sorted List segment (_ListNode)
        -------------------------------------------------------
        """
        # Split the list only if there are at least two elements.
        if current is not None and current._next is not None:
            # Generate the left and right lists.
            left, right = Sorts._merge_split(current)
            # Put the left list in order.
            left = Sorts._merge_sort_aux(left)
            # Put the right list in order.
            right = Sorts._merge_sort_aux(right)
            # Merge the left and right lists.
            current = Sorts._merge(left, right)
        return current

    @staticmethod
    def _merge_split(current):
        """
        -------------------------------------------------------
        Split the list by putting alternating nodes into left and right lists.
        Use: left, right = _merge_split(current)
        -------------------------------------------------------
        Preconditions:
          current - pointer to a List node (_ListNode)
        Postconditions:
          returns:
          left - pointer to left List segment (_ListNode)
          right - pointer to right list segment (_ListNode)
        -------------------------------------------------------
        """
        #
        left = None
        right = None
        toggle = 'l'

        while current is not None:
            next_node = current._next

            if toggle == 'l':
                current._next = left
                left = current
                toggle = 'r'
            else:
                current._next = right
                right = current
                toggle = 'l'

            current = next_node
        return left, right

    @staticmethod
    def _merge(left, right):
        """
        -------------------------------------------------------
        Merges two parts of a linked list together.
        Use: new = _merge(left, right)
        -------------------------------------------------------
        Preconditions:
          left - pointer to a List node (_ListNode)
          right - pointer to a List node (_ListNode)
        Postconditions:
          returns:
          new - pointer to sorted merge of left and right (_ListNode)
        -------------------------------------------------------
        """
        # Initialize the new list.
        if left._data <= right._data:
            new = left
            left = left._next
        else:
            new = right
            right = right._next

        # Create a pointer to traverse the new list.
        current = new

        # Traverse both lists appending larger value to the end of the list.
        while left is not None and right is not None:

            if left._data <= right._data:
                current._next = left
                current = current._next
                left = left._next
            else:
                current._next = right
                current = current._next
                right = right._next

        # Append the remaining list.
        if left is not None:
            current._next = left
        elif right is not None:
            current._next = right
        return new

    @staticmethod
    def quick_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Quick Sort algorithm.
        Use: quick_sort(a)
        -------------------------------------------------------
        Preconditions:
          a - a linked list of comparable elements (?)
        Postconditions:
          Contents of a are sorted.
        -------------------------------------------------------
        """
        a._front = Sorts._quick_sort_aux(a._front)
        return

    @staticmethod
    def _quick_sort_aux(current):
        """
        -------------------------------------------------------
        Divides a linked list into halves, sorts each half, then
        concatenates the halves back together.
        Use: current = _quick_sort_aux(current)
        -------------------------------------------------------
        Preconditions:
          current - pointer to a List node (_ListNode)
        Postconditions:
          returns:
          current - pointer to a sorted List (_ListNode)
        -------------------------------------------------------
        """
        # to sort the sublist a[p:q] of linked list a into ascending order
        if current is not None:
            # partitions a[first:last] into a[first:pivot] and a[pivot+1:last]
            lesser, equals, greater = Sorts._partition(current)
            lesser = Sorts._quick_sort_aux(lesser)
            greater = Sorts._quick_sort_aux(greater)
            current = Sorts._append(lesser, equals)
            current = Sorts._append(current, greater)
        return current

    @staticmethod
    def _partition(current):
        """
        -------------------------------------------------------
        Divides a linked list into three parts.
        Use: l, e, g = _partition(current)
        -------------------------------------------------------
        Preconditions:
          current - pointer to a List node containing pivot value (_ListNode)
        Postconditions:
          returns:
          lesser - a list of values less than the pivot value (_ListNode)
          greater - a list of values greater than the pivot value (_ListNode)
          equals - a list of values equal to the pivot value (_ListNode)
        -------------------------------------------------------
        """
        pivotValue = current._data
        lesser = None
        greater = None
        equals = None

        while current is not None:
            next_node = current._next

            if pivotValue > current._data:
                current._next = lesser
                lesser = current
            elif pivotValue < current._data:
                current._next = greater
                greater = current
            else:
                current._next = equals
                equals = current

            current = next_node
        return lesser, equals, greater

    @staticmethod
    def _append(head, tail):
        """
        -------------------------------------------------------
        Combines two lists together in order.
        Use: current = _append(head, tail)
        -------------------------------------------------------
        Preconditions:
          head - pointer to a List node of the first list (_ListNode)
          tail - pointer to a List node of the second list (_ListNode)
        Postconditions:
          returns:
          head - pointer to the combined nodes in order (_ListNode)
        -------------------------------------------------------
        """
        current = head
        previous = None

        while current is not None:
            previous = current
            current = current._next

        if previous is None:
            head = tail
        else:
            previous._next = tail
        return head

    # Sort Utilities

    @staticmethod
    def to_array(a):
        """
        -------------------------------------------------------
        Copies list values to a Python list.
        Use: values = to_array(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked list of comparable elements (?)
        Postconditions:
            returns
            values - the contents of a in a Python list.= (list of ?)
        -------------------------------------------------------
        """
        values = []
        current = a._front

        while current is not None:
            values.append(current._data)
            current = current._next
        return values

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked list is is_sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Preconditions:
          a - a linked list of comparable elements (?)
        Postconditions:
          returns:
          is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._data <= current._next._data:
                current = current._next
            else:
                is_sorted = False
        return is_sorted

    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: radix_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a List of base 10 integers (List)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        first_hash = HashSet(10)
        first_result = []
        second_hash = HashSet(10)
        second_result = []
        current = a._front
        previous = None
        n = 0

        while current is not None and n < (a._count - 1):
            for j in range(0, 10):
                if str(current._data)[-1] == j:
                    first_hash[j].append(current._data)
            previous = current
            current = current._next
            n += 1

        if previous == None:
            for j in range(0, 10):
                if str(current._data)[-1] == j:
                    first_hash[j].append(current._data)

        for i in range(len(first_hash)):
            for v in first_hash[i]:
                first_result.append(v)

        for n in range(0, 10):
            for m in first_result:
                if len(m) == 2:
                    if m[0] == n:
                        second_hash[n].append(m)
                else:
                    second_hash[0].append(n)

        for i in range(len(second_hash)):
            for v in second_hash[i]:
                second_result.append(v)

        a = List()

        for q in second_result:
            a.append(q)

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a linked structure of comparable elements (Deque)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        last = len(a)
        i = 1
        current = a._front

        while i < (last - 1) and current is not None:
            if current._prev is not None:
                if current._prev._data > current._data:
                    Sorts._swap(a, current._prev, current)
                    i -= 1
                else:
                    i += 1
                    current = current._next
            else:
                i += 1
        return

    @staticmethod
    def _swap(a, previous, current):
        """
        -------------------------------------------------------
        Swaps the data contents of two array elements.
        Updates 'swaps'.
        Use: Sorts._swap(a, i, j)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            i - index of one value (int 0 <= i < len(a))
            j - index of another value (int 0 <= j < len(a))
        Postconditions:
            Values in a[i] and a[j] are swapped.
        -------------------------------------------------------
        """
        Sorts.swaps += 1

        temp = current._prev
        current._prev = current
        current = temp
        return

    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: Sorts.radix_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of base 10 integers (list)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        max_digit = 0
        my_list = []
        count = 0
        neg_count = -1
        my_temp = []
        new_temp = []
        passed_zeros = False
        num_string = str()

        for i in range(0, 9):
            my_list.append([])

        for i in a:
            new_temp.append([])
            for j in str(i):
                new_temp[-1].append(j)
            if len(str(i)) > max_digit:
                max_digit = len(str(i))
            count += 1

        for i in new_temp:
            while len(i) < max_digit:
                i.insert(0, "0")

        temp = deepcopy(new_temp)

        for i in range(0, (max_digit)):
            my_temp = deepcopy(my_list)
            for j in temp:
                my_temp[int(j[neg_count])].append(j)
            temp = []
            for k in my_temp:
                for l in k:
                    temp.append(l)
            neg_count -= 1

        count = 0

        for k in temp:
            for i in k:
                if i != "0":
                    passed_zeros = True
                if passed_zeros:
                    num_string += i
            a.pop()
            a.insert(count, int(num_string))
            num_string = str()
            passed_zeros = False
            count += 1

        return
