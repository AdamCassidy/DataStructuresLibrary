"""
-------------------------------------------------------
movie_utilities.py
-------------------------------------------------------
Author:  Adam Cassidy
ID:      161818720
Email:   cass8720@mylaurier.ca
__updated__ = "2017-09-21"
-------------------------------------------------------
Utilities functions for movie handling
-------------------------------------------------------
"""
from movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Postconditions:
        returns
        movie - a completed movie object (Movie).
    -------------------------------------------------------
    """

    title = input("Title: ")
    release_year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    movie = Movie(title, release_year, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Postconditions:
        returns
        movie - contains the data from line (Movie)
    -------------------------------------------------------
    """

    formatted_line = line.split("|")
    title = formatted_line[0]
    year = int(formatted_line[1])
    director = formatted_line[2]
    rating = float(formatted_line[3])
    genre_codes = formatted_line[4].split(",")
    genre_codes = list(map(int, genre_codes))
    movie = Movie(title, year, director, rating, genre_codes)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of movie objects into a list.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Preconditions:
        fv - a already open file of movie data (file)
    Postconditions:
        returns
        movies - a list of movie objects (list of Movie)
    -------------------------------------------------------
    """

    movies = []
    for line in fv:
        movie_objects = line.strip()
        movie_objects = movie_objects.split("|")
        movie_objects[4] = list(map(int, movie_objects[4].split(",")))
        movies.append(Movie(movie_objects[0], int(
            movie_objects[1]), movie_objects[2], float(movie_objects[3]), movie_objects[4]))
    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Postconditions:
        Menu of genres is printed.
    -------------------------------------------------------
    """
    count = 0
    for genre in Movie.GENRES:
        if count == 0:
            print("Genres")
        print(" " + str(count) + ": " + genre)
        count += 1
    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Postconditions:
        returns
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    user_genre = int()
    genres = []

    menu()
    while user_genre != "":
        user_genre = input("Enter a genre number (Press Enter to quit): ")
        if user_genre == "":
            break
        elif user_genre.isdigit():
            user_genre = int(user_genre)
            if user_genre in genres:
                print("Error: Genre already entered.")
            elif user_genre >= 0 and user_genre <= 9:
                genres.append(user_genre)
            else:
                print("Error: Input must be an integer in the range 0-9.")
        else:
            print("Error: Input must be an integer in the range 0-9.")
            user_genre = input("Enter a genre number (Press Enter to quit): ")
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Preconditions:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        fv contains the contents of movies
    -------------------------------------------------------
    """

# Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Postconditions:
        returns
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """

# Your code here
    ymovies = []

    for i in movies:
        if i.year == year:
            ymovies.append(i)
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Postconditions:
        returns
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

# Your code here
    rmovies = []

    for i in movies:
        if i.rating >= rating:
            rmovies.append(i)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """

# Your code here
    gmovies = []

    for i in movies:
        for j in i.genres:
            if j == genre:
                gmovies.append(i)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

# Your code here
    gmovies = []

    for i in movies:
        if set(genres) == set(i.genres):
            gmovies.append(i)

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        returns
        counts - the number of movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    movies_with_genre = []

    for i in range(0, 10):
        movies_with_genre = []
        for movie in movies:
            if i in movie.genres:
                movies_with_genre.append(movie)

        counts.append(len(movies_with_genre))
    return counts
