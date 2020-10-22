"""
-------------------------------------------------------
food_utilities.py
-------------------------------------------------------
Author:  Adam Cassidy
__updated__ = 2018-01-10
-------------------------------------------------------
"""
from food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Postconditions:
        returns
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Name: ")
    print("Origin")
    print(Food.origins())
    origin = int(input(": "))
    s = input("Vegetarian (Y/N): ")
    # Accept a range of values for vegetarian
    is_vegetarian = s.upper() in ('Y', 'TRUE', '1', 'T', 'YES')
    calories = int(input("Calories: "))
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Postconditions:
        returns
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    data = line.strip().split("|")
    food = Food(data[0], int(data[1]), data[2] == "True", int(data[3]))
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file of food data (file)
    Postconditions:
        returns
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    file_variable.seek(0)
    foods = []

    for line in file_variable:
        food = read_food(line)
        foods.append(food)
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Preconditions:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Postconditions:
        file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    -------------------------------------------------------
    """
    for food in foods:
        food.write(file_variable)
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []

    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Postconditions:
        returns
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []

    for food in foods:
        if food.origin == origin:
            origins.append(food)
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total = 0
    count = len(foods)

    for food in foods:
        total += food.calories

    if count > 0:
        avg = total // count
    else:
        avg = 0
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Postconditions:
        returns
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    total = 0
    count = 0

    for food in foods:
        if food.origin == origin:
            total += food.calories
            count += 1

    if count > 0:
        avg = total // count
    else:
        avg = 0
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    Use: food_table(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        prints
        a table of the foods sorted by name
    -------------------------------------------------------
    """
    foods.sort()
    print("{:35s} {:12s} {:10s} {:8s}".format(
        "Food", "Origin", "Vegetarian", "Calories"))
    print("{} {} {} {}".format("-" * 35, "-" * 12, "-" * 10, "-" * 8))

    for food in foods:
        print("{:35s} {:12s} {:>10} {:8,d}".format(
            food.name, Food.ORIGIN[food.origin], str(food.is_vegetarian), food.calories))
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Postconditions:
        returns
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []

    for food in foods:
        if (origin == -1 or food.origin == origin) and (max_cals == 0 or food.calories <= max_cals) and (not is_veg or food.is_vegetarian):
            result.append(food)
    return result


def food_test():

    fv = open('foods.txt', 'r', encoding='utf-8')
    foods = read_foods(fv)
    fv.close()

    print("Length: {}".format(len(foods)))
    r = food_search(foods, -1, 300, True)
    print("Length: {}".format(len(r)))

    for f in r:
        print(f)
    return
