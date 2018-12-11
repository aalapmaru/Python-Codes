movies=[]


def menu():
    user_input =input("Enter 'a' to add a new movie, 'l' to see your movies, 'f' to find movies and 'q' to quit:   ")

    while user_input!='q':
        if user_input== 'a':
            add_movie()

        elif user_input=='l':
            show_movie(movies) 

        elif user_input== 'f':
            find_movie()

        else:
            print("Invalid Command - Please enter a valid command")

        user_input=input("\nEnter 'a' to add a new movie, 'l' to see your movies, 'f' to find movies and 'q' to quit:   ")



def add_movie():
    name=input('Enter the name of the movie: ')
    director=input('Enter the director of the movie: ')
    year=input('Enter the year of the movie: ')

   
    movie={
        'name': name,
        'director': director,
        'year': year
    }
    movies.append(movie)


def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)
        
       

def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year Released: {movie['year']}\n")


def find_movie():
    find_by=input("What property of a movie you want to use to find that movie: ")
    looking_for= input("Enter the property's value: ")

    found_movies= find_by_attributes(movies,looking_for, lambda x: x[find_by])

    show_movie(found_movies)

def find_by_attributes(items,expected,finder):
    found=[]

    for i in items:
        if finder(i)==expected:
            found.append(i)

    return found  
menu() 

print(movies)
            

         

