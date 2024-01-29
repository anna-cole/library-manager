# Fix:
# show book details not working get_all() function is the problem, need to grab user variable e use books = user.books() 
# delete the user without having to prompt for user name. Account for case insensivity. Fazer o mesmo pra criar books pro user
# erro qd aperto crtl C
# Each model class should include ORM methods (create, delete, get all, and find by id at minimum).
# For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
#The CLI should validate user input and object creations/deletions, providing informative errors to the user.
#The project should include a README.md that describes the application. More on this requirement in the project module in canvas.
#change the name of the project locally and in git
# when searching user by name, account for case insensivity

from helpers import (
    exit_program,
    list_users,
    show_user_details,
    create_user,
    update_user,
    delete_user,
    list_books,
    show_book_details,
    create_book,
    update_book,
    delete_book
)

def initial_loop():
    initial_menu()
    while True:
        choice = input("> ").lower()
        if choice == "u":
            list_users()
            users_menu()
            users_loop()
        elif choice == "b":
            list_books()
            books_menu()
            books_loop()
            pass
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice") 

def users_loop():
    while True:
        choice = input("> ").lower()
        if choice == "i":
            show_user_details()
            user_menu()
            user_loop()
        elif choice == "a":
            create_user()
            list_users()
            users_menu()
            pass
        elif choice == "b":
            initial_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def user_loop():
    while True:
        choice = input("> ").lower()
        if choice == "u":
            update_user()
            user_menu()
        elif choice == "d":
            delete_user() 
            list_users()
            users_menu()
            users_loop()
        elif choice == "b":
            list_users()
            users_menu()
            users_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def books_loop():
    while True:
        choice = input("> ").lower()
        if choice == "i":
            show_book_details()
            book_menu()
            book_loop()
        elif choice == "a":
            create_book()
            list_books()
            books_menu()
            pass
        elif choice == "b":
            initial_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def book_loop():
    while True:
        choice = input("> ").lower()
        if choice == "u":
            # update_book()
            print("make function update book")
        elif choice == "d":
            # delete_book()
            print("make function delete book")
        elif choice == "b":
            initial_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

        
def initial_menu():
    print("\nHello! Please choose from the following:\n")
    print("Type U or u to see all users")
    print("Type B or b to see all books")
    print("Type E or e to exit\n")

def users_menu():
    print("\n******************\n")
    print("Type I or i to see the user's details")
    print("Type A or a to add a new user")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

def user_menu():
    print("\n******************\n")
    print("Type U or u to update this user")
    print("Type D or d to delete this user")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

def books_menu():
    print("\n******************\n")
    print("Type I or i to see the book's details")
    print("Type A or a to add a new book")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

def book_menu():
    print("\n******************\n")
    print("Type U or u to update this book")
    print("Type D or d to delete this book")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

if __name__ == "__main__":
    initial_loop()