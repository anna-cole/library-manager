from helpers import (
    exit_program,
    list_users,
    show_user,
    create_user,
    delete_user,
    update_user,
    show_book,
    create_book_for_user,
    delete_book,
    update_book 
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
        user_choice = input("> ").lower()
        if user_choice.isdigit():
            user = show_user(int(user_choice))
            if user:
                user_menu()
                user_loop(user, user_choice)
            else:
                users_menu()
        elif user_choice == "a":
            create_user()
            list_users()
            users_menu()
        elif user_choice == "b":
            initial_loop()
        elif user_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def user_loop(user, user_choice):
    while True:
        book_choice = input("> ").lower()
        if book_choice.isdigit():
            book = show_book(int(book_choice), user)
            if book:
                book_menu()
                book_loop(user_choice, user, book, book_choice)
            else:
                user_menu()
        elif book_choice == "a":
            create_book_for_user(user)
            show_user(int(user_choice))
            user_menu()
        elif book_choice == "d":
            delete_user(user) 
            list_users()
            users_menu()
            users_loop()
        elif book_choice == "u":
            update_user(user)
            show_user(int(user_choice))
            user_menu()
            user_loop(user, user_choice)
        elif book_choice == "b":
            list_users()
            users_menu()
            users_loop()
        elif book_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def book_loop(user_choice, user, book, book_choice):
    while True:
        choice = input("> ").lower()
        if choice == "d":
            delete_book(book)
            show_user(int(user_choice))
            user_menu()
            user_loop(user, user_choice)
        elif choice == "u":
            update_book(book)
            book = show_book(int(book_choice), user)
            book_menu()
        elif choice == "b":
            show_user(int(user_choice))
            if user:
                user_menu()
                user_loop(user, user_choice)
            else:
                users_menu()
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
    print("Type A or a to add a new book for this user")
    print("Type D or d to delete this user")
    print("Type U or u to update this user")
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