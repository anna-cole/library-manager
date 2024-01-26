# Fix:

# delete the user without having to prompt for user name. Account for case insensivity. Fazer o mesmo pra criar books pro user
# erro qd aperto crtl C

from helpers import (
    exit_program,
    list_users,
    show_user,
    create_user,
    delete_user,
    show_book, 
   
    # delete_book,
    # update_book
)

def initial_loop():
    initial_menu()
    while True:
        choice = input("> ").lower()
        if choice == "u":
            list_users()
            users_menu()
            users_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice") 

def users_loop():
    while True:
        choice = input("> ").lower()
        if choice.isdigit():
            show_user(int(choice))
            user_menu()
            user_loop()
        elif choice == "a":
            create_user()
            list_users()
            users_menu()
        elif choice == "b":
            initial_loop()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def user_loop():
    while True:
        choice = input("> ").lower()
        if choice.isdigit():
            show_book(int(choice))
            book_menu()
            book_loop()
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
    print("Type E or e to exit\n")

def users_menu():
    print("\n******************\n")
    print("Type the user's number to see their details")
    print("Type A or a to add a new user")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

def user_menu():
    print("\n******************\n")
    print("Type the book's number to see its details")
    print("Type D or d to delete this user")
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
