## MOVIEACTORSPROJECT

*** A simple project built to collect your favorite actors and their memorable films! ***

This project has a database created and modified with Python ORM methods:

- __init__.py : file w/ init method that connects to the movieactors.db SQLite database and creates a cursor object (CURSOR) execute SQL commands. The CONN object represents the connection to the database, for data transactions.

- actor.py: file where our Actor class is built to interact with a SQLite database, representing an actor entity. Includes methods for creating, saving, and deleting actor records in the database. The class uses a class-level dictionary (all_actors) to keep track of actor instances by their IDs. It also includes methods for finding actors by ID or name, managing relationships with movies, and handling database operations such as creating or dropping the actor table.

- movie.py: file where our Movie class is built to manage movie records in the SQLite movie table. Includes methods for creating, saving, and deleting movies, while ensuring each movie is linked to an actor w/ actor_id. It also has a class-level dictionary (all_movies) which stores instances for quick reference. The class also provides methods to create or drop the movie table, fetch all movies, or find them by ID or name.

- cli.py: file script providing a CLI to manage actors. Provides a menu with options to list, add, or delete actors, and exit the program. It also has a  main() function that continuously loops, prompting the user for input and invoking the appropriate helper functions based on their choice. Program exits when the user selects the exit option.

- debug.py: file script sets a debugging session using the ipdb library, connects to the SQLite database through the CONN and CURSOR objects from the models.__init__ module and pauses execution where ipdb.set_trace() is called for a step-by-step inspection of code and database interactions.

- helpers.py: file contains functions to manage actors and movies in the CLI. Includes functions to display a welcome message, list all actors, add or delete actors, and view an actor's profile along with their movies. Users can also add or delete movies linked to actors. It also includes an exit_program function to exit the application.

The directory structure is as follows:

└── lib
    ├── models
    │   ├── __init__.py
    │   └── actor.py
    |   └── movie.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
├── Pipfile
├── Pipfile.lock
├── README.md

## Generate Environment

 Then run the following commands to generate the project environment:

pipenv install
pipenv shell

## Generating The CLI

You can run the template CLI with `python lib/cli.py`


