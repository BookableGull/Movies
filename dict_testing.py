"""
Tulane University, CMPS 1500, Spring 2023

STUDENTS MUST FILL IN BELOW

Student name: Ivo Tomasovich
Student email address: itomasovich@tulane.edu

Collaborators:
None
"""

# NOTE: you MUST write your own code. You may discuss the assignment with
#       professors, TAs, other students, or family members. But you MUST
#       list anyone you collaborated with in the space above.

import os
import dict_funcs

### 1500 Lab assignment part 0: rules and display() function

# Students: you must re-affirm that you will only hand in your own
# work, you will list all collaborators above, and you understand
# that simply listing collaborators does not mean you can copy.
# Furthermore, you understand that you must explain your code in
# comments, in your own words, or you will not receive credit.

i_agree_to_the_rules = True  # read the text above, then change this line

if not i_agree_to_the_rules: # students: do not modify this line
    exit() # program will exit unless student agrees to rules

# The function get_menu_choice() is provided to students and should
# not be modified unless for extra credit challenges.
def get_menu_choice():
    menu = """Actor data storage
---------------------------
A: Add an actor
B: Add a movie
C: Delete an actor
D: Delete a movie
E: Display all actors
F: Find actors of a movie
G: Compare two movies
H: Compare two actors
Q: Quit the program
"""
    print(menu)
    choice = input("Enter your choice: ").upper()
    while choice not in "ABCDEFGHQ" or len(choice) != 1:
        choice = input("Enter a valid choice: ")
    return choice

## The main loop of your program is below, students
## should focus on implementing the functions in 
## dict_funcs.py

# Defining a dictionary: here is an empty actors dictionary to begin with
actors = {"Tom Hanks":["Big", "Sully"], "Ke Huy Quan":["The Goonies"]}

choice = ""

print('hello!')
while choice != "Q":

    choice = get_menu_choice()
    if choice == "A":
        actor = input('Enter an actor\'s name: ')
        dict_funcs.add_actor(actors,actor)
    elif choice == "B":
        actor = input('Enter an actor\'s name: ')
        movie = input('Enter a movie: ')
        dict_funcs.add_movie(actors,actor,movie)
    elif choice == "C":
        actor = input('Enter an actor\'s name: ')
        dict_funcs.del_actor(actors,actor)
    elif choice == "D":
        actor = input('Enter an actor\'s name: ')
        movie = input('Enter a movie: ')
        dict_funcs.del_movie(actors,actor,movie)
    elif choice == "E":
        dict_funcs.display(actors)
    elif choice == "F":
        movie = input('Enter a movie: ')
        dict_funcs.find_actors(actors,movie)
    elif choice == "G":
        first_movie = input('Enter a movie: ')
        second_movie = input('Enter another movie: ')
        dict_funcs.compare_movies(actors,first_movie,second_movie)
    elif choice == "H":
        first_actor = input('Enter a actor: ')
        second_actor = input('Enter another actor: ')
        dict_funcs.compare_actors(actors,first_actor,second_actor)
            
print("Goodbye!")

print(actors)