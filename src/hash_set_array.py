"""
-------------------------------------------------------
hash_set_array.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2017-11-17
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from list_linked import List, _ListNode
# Define the new_slot slot creation function.
new_slot = List

# Constants
SEP = '-' * 40


class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Precondition:
            size - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []

        for i in range(self._slots):
            self._table.append(new_slot())
        self._count = 0
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        hashkey = hash(key) % self._slots

        return self._table[hashkey]

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
        Calls _rehash if the hashset _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """

        inserted = False
        slot = self._find_slot(value)

        if slot.index(value) == -1:
            slot.insert(0, value)
            self._count += 1

        if self._count > self._LOAD_FACTOR * self._slots:
            self._rehash()

        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """

        value = None
        slot = self._find_slot(key)

        if slot.find(key) is not None:
            value = slot.remove(key)

        self._table[hash(key) % self._slots] = slot

        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates the
        existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """

        new_table = []
        temp = []
        old_slots = self._slots

        for i in self._table:
            for j in i:
                temp.append(j)
        self._table = []
        self._slots = 0
        self._count = 0
        for i in range(0, 2 * old_slots + 1):
            self._table.append(new_slot())
            self._slots += 1
        for i in temp:
            self.insert(i)
        return

    def debug(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed and the slots identified.
        -------------------------------------------------------
        """
        slot = 0
        count = 0

        print("Amount of slots: {}".format(self._slots))
        print()

        for i in self._table:
            print("Slot {}:".format(slot))
            print("----------------------------------------")
            for j in i:
                print("{}".format(j))
                print()
                count += 1
            print()
            slot += 1
        print()
        print("Total elements: {}".format(count))
        return
