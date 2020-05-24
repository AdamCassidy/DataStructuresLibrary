"""
-------------------------------------------------------
priority_queue_array.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-01-24
-------------------------------------------------------
"""
from copy import deepcopy


class PriorityQueue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._values = []
        self._first = None
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the priority queue.
        Use: pq.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        if self._first == None:
            self._first = len(self._values) - 1
        else:
            if value < self._values[self._first]:
                self._first = len(self._values) - 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the priority queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the highest priority value in the priority queue -
            the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(
            self._values) > 0, "Cannot remove from an empty priority queue"

        value = self._values.pop(self._first)
        count = 0

        for i in self._values:
            if count == 0:
                self._first = count
            elif i < self._values[self._first]:
                self._first = count
            count += 1

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the highest priority value in the priority queue -
            the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        lowest_index = int()
        count = 0

        for i in self._values:
            if count == 0:
                lowest_index = count
            elif i < self._values[lowest_index]:
                lowest_index = count
            count += 1
        self._first = lowest_index

        value = deepcopy(self._values[self._first])
        return value

    def split(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The split is stable.
        Use: pq2, pq3 = pq1.split(key)
        -------------------------------------------------------
        Preconditions:
            key - a data object (?)
        Postconditions:
            returns
            pq2 - a priority queue that contains all values
                with priority less than key (PriorityQueue)
            pq3 - priority queue that contains all values with
                priority greater than or equal to key (PriorityQueue)
            The current priority queue is empty
        -------------------------------------------------------
        """

        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        count = 0
        n = len(self._values)

        while self._values[self._first] < key and count <= (n - 1):
            pq2._values.append(self._values.pop(self._first))
            for i in range(0, len(self._values)):
                if i == 0:
                    self._first = 0
                elif self._values[i] < self._values[self._first]:
                    self._first = i
            if pq2._first == None:
                pq2._first = len(pq2._values) - 1
            else:
                if pq2._values[count] < pq2._values[pq2._first]:
                    pq2._first = len(pq2._values) - 1
            count += 1

        while count <= (n - 1):
            pq3._values.append(self._values.pop(self._first))
            i = 0
            for i in range(0, len(self._values)):
                if i == 0:
                    self._first = 0
                elif self._values[i] < self._values[self._first]:
                    self._first = i

            if pq3._first == None:
                pq3._first = len(pq3._values) - 1
            else:
                if pq3._values[count - len(pq2._values)] < pq3._values[pq3._first]:
                    pq3._first = len(pq3._values) - 1
            count += 1

        return pq2, pq3

    def combine(self, pq2):
        """
        -------------------------------------------------------
        Combines contents of two priority queues into a new 
        priority queue.
        Use: pq3 = pq1.combine(pq2)
        -------------------------------------------------------
        Preconditions:
            q2 - an array-based queue (Queue)
        Postconditions:
            returns
            pq3 - Contents of self and q2 are interlaced 
                into pq3 (Queue)
        -------------------------------------------------------
        """

        pq3 = PriorityQueue()

        while len(self._values) > 0 and len(pq2._values) > 0:
            pq3._values.append(self._values.pop(self._first))
            for i in range(0, len(self._values)):
                if i == 0:
                    self._first = 0
                elif self._values[i] < self._values[self._first]:
                    self._first = i
            pq3._values.append(pq2._values.pop(pq2._first))
            for i in range(0, len(pq2._values)):
                if i == 0:
                    pq2._first = 0
                elif pq2._values[i] < pq2._values[pq2._first]:
                    pq2._first = i

        while len(self._values) > 0:
            pq3._values.append(self._values.pop(self._first))
            for i in range(0, len(self._values)):
                if i == 0:
                    self._first = 0
                elif self._values[i] < self._values[self._first]:
                    self._first = i

        while len(pq2._values) > 0:
            pq3._values.append(pq2._values.pop(pq2._first))
            for i in range(0, len(pq2._values)):
                if i == 0:
                    pq2._first = 0
                elif pq2._values[i] < pq2._values[pq2._first]:
                    pq2._first = i

        for i in range(0, len(pq3._values)):
            if i == 0:
                pq3._first = 0
            else:
                if pq3._values[i] < pq3._values[pq3._first]:
                    pq3._first = i

        return pq3

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
