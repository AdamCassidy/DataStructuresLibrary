from sorts_array import Sorts
from test_sorts_array import test_sort
from food import Food
from food_utilities import read_foods
from list_linked import List
from hash_set_array import HashSet
from linked_list_test import list_test
from movie_utilities import read_movies
from utilities import priority_queue_test, stack_test


SORTS = []

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort),
)


print("n: 100            Comparisons                Swaps")
print("Algorithm    In Order Reversed Random    In order Reversed Random")
for i in SORTS:
    print("{}".format(i[0]))
    test_sort(i[0], i[1])
    


count = 0
food_hashset = HashSet(3)

file_name = "foods.txt"
fv = open(file_name, "r")

a = read_foods(fv)

for i in a:
    food_hashset.insert(i)

food_hashset.debug()

fv.close()




file_name = "movies.txt"
fv = open(file_name, "r")

a = read_movies(fv)

list_test(a)

fv.close()



file_name = "movies.txt"
fv = open(file_name, "r")

movies = read_movies(fv)
a = []
for i in movies:
    a.append(i)

priority_queue_test(a)

fv.close()


file_name = "movies.txt"
fv = open(file_name, "r")

movies = read_movies(fv)
titles = []
for i in movies:
    titles.append(i.title)

# Output
print("File name: {}".format(file_name))
stack_test(titles)

fv.close()