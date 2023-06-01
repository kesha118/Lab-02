"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me ={
        # TODO: Put full name into data structure
        'fullname' : 'Keshaben Kanubhai Patel',
       
        # TODO: Put student ID into data structure
        'studentid': 10286667 ,
        # TODO: Put list of 3 pizza toppings into data structure
        'toppings': [
            'green pepper',
            'red onions',
            'hot peppers'
        ],
        
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': '3-Idiots',
                'genre': 'comedy'
            },
            # TODO: Add one more movie
            {
                'title': 'hum saath saath hain',
                'genre': 'family drama'
            }    
    ]
}

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['red pepper', 'pineapple'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'Maayavan', 'Action')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID
    

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    print(f"My name is {my_info['fullname']}, but you can call me Sir {my_info['fullname'].split()[0]}.")
    # Print sentence containing student ID
    print(f"My student ID is {my_info['studentid']}.")
    

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print("My favourite pizza toppings are:") 
    # Print bullet list of favourite pizza toppings
    for toppings in my_info['toppings']:
      print(f"-{toppings}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    my_info['toppings'] = [toppings.lower()for toppings in my_info['toppings']]
    # Sort toppings list alphabetically
    my_info['toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    movie = {
        'title': title,
        'genre': genre.lower()
    }
    my_info['movies'].append(movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    genres = [movie['genre'] for movie in my_info['movies']]
    genre_list = ', '.join(genres)
    if len(genre_list) > 1:
        genre_list = genre_list.rsplit(', ', 1)
        genre_list = ' and '.join(genre_list)
    print(f"I like to watch {genre_list} movies.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    titles = [movie['title'].title() for movie in movie_list]
    title_list = ', '.join(titles)

    print(f"Some of my favourite movies are: {title_list}!")

if __name__ == '__main__':
    main()


