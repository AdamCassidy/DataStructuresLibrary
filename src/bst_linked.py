"""
-------------------------------------------------------
bst_linked.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-03-07
-------------------------------------------------------
"""

from copy import deepcopy

from queue_array import Queue


class _BSTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _BSTNode( value )
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes a BST node containing value. Child pointers are None,
            height is 1.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Postconditions:
            _height is 1 plus the maximum of the node's (up to) two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Prints node height and value - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty bst.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - data to be inserted into the bst (?)
        Postconditions:
            returns
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - a bst node (_BSTNode)
            value - data to be inserted into the node (?)
        Postconditions:
            returns
            node - the current node (_BSTNode)
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BSTNode(value)
            self._count += 1
            inserted = True
        elif node._value > value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._value < value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve( key )
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot retrieve from an empty BST"

        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                value = deepcopy(node._value)

        return value

    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another bst (BST)
        Postconditions:
            returns
            is_identical - True if this bst contains the same values
            in the same order as rs, otherwise returns False (boolean)
        -------------------------------------------------------
        """

        node = self._root._left
        rnode = rs._root

        is_identical = self.identical_aux(rs, node, rnode)
        return is_identical

    def identical_aux(self, rs, node, rnode):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another bst (BST)
        Postconditions:
            returns
            is_identical - True if this bst contains the same values
            in the same order as rs, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        if node is None:
            is_identical = True
        elif node._value == rnode._value:
            if (node._left._value == rnode._left._value) and (node._right._value == rnode._right._value):
                is_identical = (node._right.identical(rnode._right) is True) and (
                    node._left.identical(rnode._left) is True)
        else:
            is_identical = False
        return is_identical

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root
        value = self.max_r_aux(node)

        return value

    def max_r_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        if node._right is None:
            value = node._value
        else:
            self.max_r_aux(node._right)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root

        while node is not None:
            value = node._value
            node = node._left

        return value

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Postconditions:
            returns
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        node = self._root
        if node is None:
            zero, one, two = 0, 0, 0
        else:
            zero, one, two = self.node_counts_aux(node, 0, 0, 0)

        return zero, one, two

    def node_counts_aux(self, node, zero, one, two):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts_aux()
        -------------------------------------------------------
        Postconditions:
            returns
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        if node is None:
            pass
        else:
            if node._height == 1:
                zero, one, two = self.node_counts_aux(None, zero + 1, one, two)
            elif node._left is not None and node._right is not None:
                lzero, lone, ltwo = self.node_counts_aux(
                    node._left, zero, one, two + 1)
                zero, one, two = self.node_counts_aux(
                    node._right, lzero, lone, ltwo)
            elif node._left is not None:
                zero, one, two = self.node_counts_aux(
                    node._left, zero, one + 1, two)
            elif node._right is not None:
                zero, one, two = self.node_counts_aux(
                    node._right, zero, one + 1, two)
        return zero, one, two

    def balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.balanced()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """

        if self._root is None:
            is_balanced = True
        else:
            left_tree = self._root._left
            right_tree = self._root._right

            is_balanced = self.balanced_aux(left_tree, right_tree)

        return is_balanced

    def balanced_aux(self, left_tree,  right_tree):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.balanced()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if left_tree is None and right_tree is None:
            is_balanced = True
        elif left_tree is None:
            is_balanced = self.balanced_aux(
                right_tree._left, right_tree._right)
        elif right_tree is None:
            is_balanced = self.balanced_aux(
                left_tree._left, left_tree._right)
        elif abs(left_tree._height - right_tree._height) <= 1:
            if self.balanced_aux(left_tree._left, left_tree._right) and self.balanced_aux(right_tree._left, right_tree._right):
                is_balanced = True
        else:
            is_balanced = False
        return is_balanced

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Postconditions:
            returns
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        number = self._count_aux(self._root)
        return number

    def _count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST subtree.
        -------------------------------------------------------
        Preconditions:
            node - a BST node (_BSTNode)
        Postconditions:
            returns
            number - count of nodes in the current subtree (int)
        ----------------------------------------------------------
        """
        if node is None:
            # Base case: node does not exist
            number = 0
        else:
            # General case: node exists.
            number = 1 + self._count_aux(node._left) + \
                self._count_aux(node._right)
        return number

    def valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.valid()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._root is None:
            is_valid = True
        else:

            is_valid = self.valid_aux(self._root)

        return is_valid

    def valid_aux(self, node):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.valid_aux()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node._left is None and node._right is None:
            is_valid = True
        elif node._left is None and node._right.valid_aux():
            if node._height is (1 + node._right._height):
                is_valid = True
        elif self.valid_aux(node._left) and node._right is None:
            if node._height is (1 + node._left._height):
                is_valid = True
        elif self.valid_aux(node._left) and self.valid_aux(node._right):
            if (node._height is (1 + node._left._height)) or (node._height is (1 + node._right._height)):
                is_valid = True
        else:
            is_valid = False

        return is_valid

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: bst.inorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """

        node = self._root
        a = []

        if node is not None:
            self.inorder_aux(node, a)

        return a

    def inorder_aux(self, node, a):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: bst.inorder_aux()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        if node is not None:
            if node._value is not None:
                if node._left is not None:
                    if node._left._value is not None:
                        if node._left._height == 1:
                            a.append(node._left._value)
                        else:
                            self.inorder_aux(node._left, a)
                a.append(node._value)
                if node._right is not None:
                    if node._right._value is not None:
                        if node._right._height == 1:
                            a.append(node._right._value)
                        else:
                            self.inorder_aux(node._right, a)
        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: bst.preorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        node = self._root
        a = []

        if node is not None:
            self.preorder_aux(node, a)

        return a

    def preorder_aux(self, node, a):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: bst.preorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        if node is not None:
            if node._value is not None:
                a.append(node._value)
                if node._left is not None:
                    if node._left._value is not None:
                        self.preorder_aux(node._left, a)
                if node._right is not None:
                    if node._right._value is not None:
                        self.preorder_aux(node._right, a)
        return a

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: bst.postorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        node = self._root
        a = []

        if node is not None:
            self.postorder_aux(node, a)

        return a

    def postorder_aux(self, node, a):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: bst.postorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """

        if node is not None:
            if node._value is not None:

                if node._left is not None:
                    if node._left._value is not None:
                        self.postorder_aux(node._left, a)
                if node._right is not None:
                    if node._right._value is not None:
                        self.postorder_aux(node._right, a)
                a.append(node._value)
        return a

        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a 2D list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Postconditions:
            returns
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        a = []
        q = Queue()
        node = self._root

        if node is not None:
            q.insert(node)
            while not q.is_empty():
                temp = q.remove()
                a.append(temp._value)
                if temp._left is not None:
                    q.insert(temp._left)
                if temp._right is not None:
                    q.insert(temp._right)

        return a

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value matching key if found,
            otherwise returns None. Update structure of bst as required.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove from an empty BST"

        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
            node - a bst node to search for key (_BSTNode)
            key - data to search for (?)
        Postconditions:
            returns
            node - the current node or its replacement (_BSTNode)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            # Replace this node with another node.
            if node._left is None:
                # node has no left child or has no children.
                if node._right is None:
                    node = None
                else:
                    node = node._right

            elif node._right is None:
                # node has no right child.
                node = node._left
            else:
                # Node has two children
                if node._left._right is None:
                    # left child is replacement node
                    repl_node = node._left
                else:
                    # find replacement node in right subtree of left node
                    repl_node = self._delete_node_left(
                        node._left, node._left._right)
                    repl_node._left = node._left

                repl_node._right = node._right
                node = repl_node
                node._update_height()

            self._count -= 1

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent, child):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
            child - the right node of parent (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """

        repl_node = self._delete_node_left_aux(child)
        parent._update_height()
        return repl_node

    def _delete_node_left_aux(self, child):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
            child - the right node of parent (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """
        if child._right is None:
            repl_node = child
        else:
            print(child._right)
            repl_node = self._delete_node_left_aux(child._right)

        return repl_node

    def count_apply(self, func):
        """
        ---------------------------------------------------------
        Returns the number of values in a BST where func(value) is True.
        Use: number = bst.count_apply(func)
        -------------------------------------------------------
        Preconditions:
            func - a function that given a value in the bst returns
                True for some condition, otherwise returns False.
        Postconditions:
            returns
            number - count of nodes in tree where func(value) is True (int)
        ----------------------------------------------------------
        """
        number = 0
        node = self._root

        number = self.count_apply_aux(node, number, func)

        return number

    def count_apply_aux(self, node, number, func):
        """
        ---------------------------------------------------------
        Returns the number of values in a BST where func(value) is True.
        Use: number = bst.count_apply(func)
        -------------------------------------------------------
        Preconditions:
            func - a function that given a value in the bst returns
                True for some condition, otherwise returns False.
        Postconditions:
            returns
            number - count of nodes in tree where func(value) is True (int)
        ----------------------------------------------------------
        """
        if node is not None:
            if func(node._value) == True:
                number += (1 + self.count_apply_aux(node._left, number,
                                                    func) + self.count_apply_aux(node._right, number, func))
            else:
                number += (self.count_apply_aux(node._left, number,
                                                func) + self.count_apply_aux(node._right, number, func))

        return number
