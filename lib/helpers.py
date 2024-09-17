# lib/helpers.py

from models.actor import Actor
from models.movie import Movie

def welcome():
     print("🎬 Lights, Camera, Actors! 🎬")

def actor_list():
   
        actor_list = Actor.get_all()
        
        if actor_list:
            print("\n*** UDATED LIST! ***")
            for i, actor in enumerate(actor_list, start=1):
                print(f"{i}. {actor.name}")  
        
            while True:
                choice = input("Press 'a' to add an actor\n"
                                "Press 'b' for actor profile\n"
                                "Press 'c' to return to the main menu.\n"
                                "Press 'd' delete an actor.\n").lower()
                if choice == 'a':
                    add_actor()
                    break
                elif choice == 'b':
                    actor_profile()
                    break
                elif choice == 'c':
                    return
                elif choice == 'd':
                    delete_actor()
                    break
                else:
                    print("Invalid choice. Please try again.") 
        else:
            print("List empty!")
            while True:
                choice = input("Press 'a' or to add an actor\n"
                        "Press 'b' for main menu.\n").lower()
                if choice == 'a':
                    add_actor()
                    break
                elif choice == 'b':
                    return
                else:
                    print("Invalid choice. Please try again.") 

def add_actor():
    name = input("Enter actor name (or 'q' to cancel): ")

    actor = Actor.create(name)
    movie_name = input("Enter movie name: ")
    genre = input("Enter movie genre: ")
    film = Movie.create(movie_name, genre, actor.id)
    print(f"'{film.movie}' added successfully for {actor.name}")

    actor_list()
    
    if name.lower() == 'q':
        print("Actor addition canceled.")
        return
    elif name.strip() == '':
        print("Actor name cannot be an empty string. Please try again.")
    else:
        print("Error adding actor:")

def delete_actor():
    while True:
        actor_list = Actor.get_all()
    
        if not actor_list:
            print("No actors on your list to delete.")
            return
        
        print("\n*** CURRENT LIST ***")
        for i, actor in enumerate(actor_list, start=1):
                print(f"{i}. {actor.name}") 

        while True:
            num = input("Enter actor number to delete (or '0' to return to the main menu): \n")

            if num == '0':
                return
            elif not num.isdigit():
                print("INVALID NUMBER")
                continue

            num = int(num)
            if num <= 0 or num > len(actor_list):
                    print(f"No actor found matching the number '{num}'")
            else:
                actor_to_delete = actor_list[num - 1]
                confirm = input(f"Are you sure you want to delete '{actor_to_delete.name}'? (y/n): ").lower()
                if confirm == 'y':
                    actor_to_delete.delete()
                    print(f"{actor_to_delete.name} has been deleted.")
                    break
                else:
                    print("Deletion cancelled. Returning to main menu.")
                    return

def actor_profile():
    while True:
        actor_list = Actor.get_all()

        if actor_list:
            print("\n*** Actors Profile ***")
            for i, actor in enumerate(actor_list, start=1):
                print(f"{i}. {actor.name}")

            number_entered = input("enter actor number to view their work or 0 to return to the main menu\n")

            if not number_entered.isdigit():
                print("INVALID NUMBER")
                continue
            number_entered = int(number_entered)

            if number_entered == 0:
                return
            
            if 1 <= number_entered <= len(actor_list):
                actor = actor_list[number_entered - 1]
                actor_movies = actor.movies()

                if actor_movies:
                    print(f"🍿{actor.name}'s Movie List🍿")
                    for i, actors_film in enumerate(actor_movies, start=1):
                        print(f"  {i}. {actors_film.movie}")
                else:
                    print(f"No movies found for {actor.name}.")

                while True:
                    choice = input("enter 'a' to add a movie (enter 'm' for main menu)\n"
                                    "enter 'b' to delete a movie\n"
                                    "enter 'c' to return to Actors Profile.\n").lower()
                    if choice == 'a':
                        add_movie(actor)
                    elif choice == 'b':
                        delete_movie(actor)
                    elif choice == 'c':
                        break
                    elif choice == 'm':
                        return
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print(f"No actor found matching the number '{number_entered}'")

def add_movie(actor):
    movie_name = input("Enter the movie name: \n")
    genre = input("Enter the genre: \n")

    added_movie = Movie.create(movie_name, genre, actor.id)
    print(f"'{added_movie.movie}' added for {actor.name}!\n")
        
    actor_movies = actor.movies()
    if actor_movies:
        print(f"🍿{actor.name}'s Movie List🍿")
        for i, actors_film in enumerate(actor_movies, start=1):
            print(f"  {i}. {actors_film.movie}")

def delete_movie(actor):
    actor_movies = actor.movies()

    if not actor_movies:
        print("No movies found for this actor.")
        return

    print("\n*** Current List of Movies: ***")
    for i, film in enumerate(actor_movies, start=1):
        print(f"{i}. {film.movie}")

    while True:
        num = input("Enter movie number to delete (or '0' to return to the main menu): \n")

        if num == '0':
            break
        elif not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)
        if num <= 0 or num > len(actor_movies):
            print(f"No movie found matching the number '{num}'")
        else:
            film_to_delete = actor_movies[num - 1]
            confirm = input(f"Are you sure you want to delete '{film_to_delete.movie}'? (y/n): ").lower()
            if confirm == 'y':
                film_to_delete.delete()
                print(f"{film_to_delete.movie} has been deleted.\n")
                break
            else:
                print("Deletion cancelled. Returning to main menu.")
                return

def exit_program():
    print("Goodbye!")
    exit()
