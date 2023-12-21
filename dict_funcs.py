"""
Tulane University, CMPS 1500, Spring 2023

STUDENTS MUST FILL IN BELOW

Student name: Ivo Tomasovich
Student email address: itomasovich@tulane.edu

Collaborators:
None
"""
# Arguments for the below functions:
# 	- d: dictionary mapping an actor's name to a movie 
# 		 list in form {string: [string]}
#	- actor: string containing an actor's name
#	- movie: string containing an movies's name


# Add the given actor to the dictionary.
# Use an empty list as a default value.
# If it's already a key, do nothing.
def add_actor(d: dict, actor: str):  # Takes dictionary and actor as parameters
	if actor not in d:  # If the actor is not in dictionary already, add it to the dictionary and attach an empty list to it's value
		d[actor] = []
	return d

# Add the given movie to the actor's list within the given dictionary.
# If it's already in the list, do nothing
def add_movie(d: dict, actor: str, movie: str):  # takes a dictionary, name of actor, and movie name as aprameters
	points = 0  # used as a way for the if else statement to not self destruct while checking if the actor isn't in dictionary or if the movie is already listed for th actor
	if actor not in d or movie in d[actor]:
		points += 1
	else:  # if neither of the if conditions are met, append the movie to the actor's value in the dictionary
		d[actor].append(movie)
	return d  # return the dictionary

	# d[actor] = movie  # adds actor to dictionary and makes its value a movie name

# Delete the given actor from the dictionary.
# If it's not in the dictionary, do nothing.
def del_actor(d: dict, actor: str):  # takes a dictionary and an actor name as parameters
	if actor in d:
		del d[actor]  # deletes the actor from dictionary
	return d
# Delete the given movie from the actor's list within the given dictionary.
# If it's not in the list, do nothing.
def del_movie(d: dict, actor: str, movie: str):
	if movie in d[actor]:  # checks if movie is in dictionary for that actor
		d[actor].remove(movie)  # if so, remove it
	return d  # return the dictionary
# Display the movies of all actors in the 
# dictionary according to the following formatting:
# "actor" starred in "movie1", "movie2", "movie3"
# If "actor" has no movies associated with them, then use this:
# "actor" has not acted in any movies
def display(d: dict):
	listforwords = []  # Used to store list of movies if actor has multiple movies
	i = 0
	x = 0
	for key, value in d.items():
		if not value:  # checks to see if the actor doesn't have a movie, then prints the message
			print(f'{key} has not starred in any movies')
		elif len(value) == 1:  # If there's only one movie for the actor, prints he started it in
			for item in value:
				print(f'{key} has starred in {item}')
		else:
			print(key, "has starred in ", end="")  # for if there are multiple movies, this part only prints the actor with has starred in
			for item in value:
				listforwords.append(item)  # adds all the movies to the list
				i += 1  # counts how many movies there are
			for item in listforwords:
				x += 1  # adds 1 to x every time a movie loops through
				if x == i:  # if x equals to i, we are on the last movie, so print it with a newline
					print(f'{item}')
				else:  # if we aren't on the last movie, print the movie with no newline
					print(f'{item}, ', end="")


# Return the list of actors who starred in the given movie.
# If no actors were found to be associated with the movie,
# then return an empty list.
def find_actors(d: dict, movie: str):
	listofactors = []  # Used to store list of actors
	for key, value in d.items():  # if the movie given by user is in the value, add the actor to the list of actors
		if movie in value:
			listofactors.append(key)
	print(listofactors)  # Prints list of actors
	return listofactors

# Return the list of actors who starred in both given movies.
# If no actors were found to have starred in both movies,
# then return an empty list
def compare_movies(d: dict, mov1: str, mov2: str):
	listofactors = []  # used to store list of actors
	listofvalues = []  # used to store list of values
	for key, value in d.items():  # loops through all values in the dictionary
		for item in value:  # Appends all movies to a list
			listofvalues.append(item)
		if mov1 in listofvalues and mov2 in listofvalues:  # checks if the 2 movies given are both in the list of movies
			listofactors.append(key)
		listofvalues.clear()  # clears list of movies one at a time so the check isn't broken
	print(listofactors)  # prints list of actors that starred in both movies
	return listofactors

# Return the list of movies who starred both given actors.
# If no movies were found to have starred both actors,
# then return an empty list
def compare_actors(d: dict, act1: str, act2: str):
	act1movies = []  # Used to store all the movies actor one was in
	act2movies = []	 # Used to store all the movies actor two was in
	movielist = []   # used to store movies that had both actors in them
	for key, value in d.items():  # loops through each entry in the dictionary
		if key == act1:  # checks if the actor matches the first actor imputted
			act1movies.append(value)  # appends the actor to the act1movies list
	for key, value in d.items():  # same thing as previous for loop but for actor 2
		if key == act2:
			act2movies.append(value)
	for item in act1movies:  # nested loop to check the list of actor 1's movies and see if actor 2 was in them
		for movie in item:
			if movie in act2movies[0]:  # if so, add it to the movie list
				movielist.append(movie)
	print(movielist)  # print the movie list with both actors
	return movielist
