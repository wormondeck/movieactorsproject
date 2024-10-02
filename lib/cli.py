# lib/cli.py

from helpers import (
    welcome,
    actor_list,
    add_actor,
    delete_actor,
    exit_program,
)

def main():
    while True:
        welcome()
        menu()
        choice = input("> ").strip()
        if choice == "1":
            actor_list()
        elif choice == "2":
            add_actor()
        elif choice == "3":
            delete_actor()
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid choice. Try again.\n")

def menu():
    print("\n****  Select an option:  ****\n")
    print("1. Current list of actors")
    print("2. Add an Actor")
    print("3. Delete an Actor")
    print("4. Exit the program\n")

if __name__ == "__main__":
    main() 