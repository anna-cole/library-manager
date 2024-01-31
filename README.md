# Library Manager application

## Description
Welcome to our project! Library Manager is a python app with an user-friendly command-line interface that allows library staff to efficiently manage books and customers. 

This CLI utilizes an SQLite database to store records, making it easier to see, search, add, update and delete books and customers data. We hope you enjoy and we look forward to your contributions!

## Directory and file structure

- The program files are located inside the /lib folder: book.py and user.py (which respectively contains the model classes Book and User), debug.py (seeding database with mock data), helpers.py (helper functions) and cli.py (menu choices and logic). 
  
- Database, README.md and other files are in the root directory.

## Intructions to run the application

- Step 1: Assuming you already have python installed in your computer, run the command python lib/debug.py in the terminal, to populate the database with fake data. At any time, run this script again if you need to reset the database. 

- Step 2: Run python lib/cli.py to execute the command line program. 

## Library Manager app functionalities

- The functions located in lib/helper.py (which, in turn, reference functions in user.py and book.py) allow the application user to perform basic CRUD operations on books and customers. Those functions are: 

VIEW STAFF USERS - view(): Displays all staff members' first and last names, staff ID number, and position ID.
ADD A STAFF MEMBER - add(): Adds a user to the database. Requires the user's first and last name, along with their position designation.
EDIT A STAFF MEMBER - edit(): Allows you to select a staff member based on their staff ID and choose which attributes to edit, such as their first name, last name, or position ID.
DELETE A STAFF MEMBER - delete(): Allows you to select a staff member based on their staff ID and permanently delete them from the database.




```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
