class Movie:
    def __init__(self, person, choice):
        self.name = person
        self.chooser = choice

    def __str__(self):
        return "The movie " + self.name + " was chosen by " + self.chooser


movie_list = []


# Function to add a movie to the list, movie_list
def add_movie(movie_name, choice_name):
    movie = Movie(movie_name, choice_name)
    movie_list.append(movie)


# Ask user if they want to add a movie. Create a new object and input the attributes.
while True:
    new_movie = input("Do you want add another movie?(Y|n):")
    if new_movie.lower() == "y" or new_movie == "":
        add_movie(input("Which movie?"), input("Who is choosing?"))
    else:
        print("Well then what do you want from me?")
        break

for m in movie_list:
    print(m)
