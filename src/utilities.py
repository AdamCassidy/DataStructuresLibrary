"""
-------------------------------------------------------
utilities.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-01-17
-------------------------------------------------------
"""
from food import Food
from list_array import List
from priority_queue_array import PriorityQueue
from queue_array import Queue
from stack_array import Stack


def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of a onto s.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    while len(a) > 0:
        s.push(a.pop())

    return


def stack_to_array(s, a):
    """
    -------------------------------------------------------
    Pops contents of s into a.
    Use: stack_to_array(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        Contents of s are moved into a, s is empty.
    -------------------------------------------------------
    """
    while s.peek() is not None:
        a.append(s.pop())

    return


def stack_test(a):
    """
    -------------------------------------------------------
    Tests 
    Use: stack_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Stack are tested for both empty and 
        non-empty stacks using the data in a:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    s = Stack()

    # tests for the stack methods go here
    # print the results of the method calls and verify by hand
    print("is_empty for an empty stack:")
    is_empty = s.is_empty()
    print("{}".format(is_empty))
    try:
        print("pop empty:")
        pop = s.pop()
        print("{}".format(pop))
    except:
        print("pop empty failed")
    try:
        print("peek empty:")
        peek = s.peek()
        print("{}".format(peek))
    except:
        print("peek empty failed")
    try:
        print("push:")
        for j in a:
            s.push(j)
        for i in s:
            print("{}".format(i))
    except:
        print("push failed")
    try:
        print("pop:")
        pop = s.pop()
        print("{}".format(pop))
    except:
        print("pop failed")
    try:
        print("peek:")
        peek = s.peek()
        print("{}".format(peek))
    except:
        print("peek failed")
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    print("Empty queue: {}".format(q.is_empty()))
    for i in a:
        q.insert(i)
    print("Items inserted into queue:")
    for j in q:
        print("{}".format(j))
    print()
    print("Remove: {}".format(q.remove()))
    print()
    if not q.is_empty():
        print("Peek: {}".format(q.peek()))
    else:
        print("Queue is empty.")

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of PriorityQueue are tested for both empty and 
        non-empty priority queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = PriorityQueue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    print("Empty pqueue: {}".format(pq.is_empty()))
    for i in a:
        pq.insert(i)
    print("Items inserted into pqueue:")
    for j in pq:
        print("{}".format(j))
    print()
    print("Remove: {}".format(pq.remove()))
    print()
    if not pq.is_empty():
        print("Peek: {}".format(pq.peek()))
    else:
        print("Pqueue is empty.")
    return


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
    m = Food("Butter Chicken", 2, None, None)

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print("Empty list: {}".format(l.is_empty()))
    for i in a:
        l.append(i)
    print("Items append to list:")
    print("Len: {}".format(len(l)))
    l.insert(5, m)
    print("Insert value copy of Butter Chicken to index 5")
    if not l.is_empty():
        print("Index of Butter Chicken: {}".format(l.index(m)))
        print("Contains 'Butter Chicken': {}".format(m in l))
        print("Remove Butter Chicken")
        print("Contains 'Butter Chicken': {}".format(m in l))
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
