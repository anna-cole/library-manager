# Library Manager 

## Description
Welcome to our project! Library manager is a Python app with a user-friendly command line interface for efficiently managing book inventory and customer’s information, organizing data and performing basic CRUD operations. My passion for books inspired me to create this app.

This app has a SQLite database and two classes to store books and users’ data. It also has a complete CLI menu and Python methods to read, search, add, update and delete data. An ORM – Object Relational Mapping was implemented to manipulate data to and from the database. 

We hope you enjoy and we look forward to your contributions!

## Directory and file structure
The program files are located inside the /lib folder: 
- cli.py: The CLI script, with menu choices and user prompts. It calls the helper functions exit_program, list_users, show_user, create_user, delete_user, update_user, show_book, create_book_for_user, delete_book and update_book, according to the user prompts. 
- helpers.py: This file contains the helper functions above mentioned, with logic to perform basic CRUD operations. You can find a complete description of those functions further below.    
- book.py and user.py: Those files respectively contain the data model classes Book and User, both with functions for data persistence, like creating and deleting data tables, creating and deleting data table rows, properties for data validation, functions that return object per row, etc.
- debug.py: This file can be used for debugging and is also reponsible for seeding the database with mock data and resetting the database.
- __init__.py: This file creates the necessary database constants.
  
README.md and other files are in the root directory. After seeding the database, a database file called library.db will be created in the root directory.

## Installing and running the application
To install and run Library Manager, ensure that you have Python 3 and pip installed on your system.
1. Clone this repository to your local machine and navigate to its directory.
2. Run pipenv install to install all the necessary package dependencies.
3. Run pipenv shell to enter the virtual environment.
4. Run python lib/debug.py to populate the database with mock data (at any time you can run this script again if you need to reset the database).
5. Run python lib/cli.py to start the command line program.

## Library Manager app functionalities
The functions located in lib/helper.py (which, in turn, reference functions in user.py and book.py) allow library staff to perform basic CRUD operations on books and customers. Those functions are: 

EXIT PROGRAM - exit_program(): It closes the application.

VIEW ALL USERS - list_users(): Displays an ordered list with all users' names. 

SHOW USER DETAILS - show_user(): Displays details of a selected user, like its address, membership level and a list of borrowed books.

ADD USER - create_user(): It adds a new library user to the database. Requires the user's name, address and membership level. 

DELETE USER - delete_user(): It permanentely deletes a selected user from the database.

EDIT AN USER - update_user(): Allows the staff member to update details of a selected library user, like name, address and membership level. This function allows it to enter an empty string in the options that are not to be updated.

SHOW BOOK DETAILS - show_book(): Displays details of a selected book, like its title, genre and user who borrowed it. 

ADD BOOK TO USER - create_book_for_user(): It adds a new book to a selected user. It requires the book's title and genre. 

DELETE BOOK - delete_book(): It permanentely deletes a selected book from the database.

EDIT A BOOK - update_book(): Allows the staff member to update details of a selected book, like title, genre and user who borrowed it. This function allows it to enter an empty string in the options that are not to be updated.

## Video explaining the app functionalities
[Video showing features](https://www.loom.com/share/bc09cf99e91a486fb75a8806b29bd58a?sid=d2448a63-d8bf-4f8a-9f03-d6835d162f5b)

## Check my blog post about how to create a python CLI app and how to connect it to Github. 
[A beginner’s guide on how to build a simple Python application with a command line interface](https://medium.com/@anna-cole/a-beginners-guide-on-how-to-build-a-simple-python-application-with-a-command-line-interface-6d7fb187789b)

## Contributing
We welcome any and all contributions! Here are some ways you can get started:
1. Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
2. Contribute code: If you are a developer and want to contribute, open a pull request with your contributions and wait for pull request to be merged, if approved. 
3. Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or improvements you would like to see!
4. Documentation: If you see the need for some additional documentation, feel free to add some!

## License
At the moment, licensing is not being offered. For any questions, please contact our support team.

## Support
For any questions or support, please email acrrj123@gmail.com


