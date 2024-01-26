# Fix:
# 1 - choice for showing book details
# 2 - choice for adding book for that user needs to be A or a
# 3 - function to add book have to add book for that user without promptinh user for user name
# 4 - choice for deleting book has to be D or d
# delete the user without having to prompt for user name

from helpers import (
    exit_program,
    list_users,
    show_user,
    create_user,
    delete_user,
    show_book, 
    create_book,
    # delete_book,
    # update_book
)

def user_loop():
    print("user_loop")
    while True:
        choice = input("> ").lower()
        if choice == "b":
            main()


def main():
    initial_menu()
    while True:
        choice = input("> ").lower()
        if choice == "e":
            exit_program()
        elif choice == "u":
            list_users()
            users_overview_menu()
        elif choice == "b":
            user_loop()
            initial_menu()
        elif choice == "a":
            create_user()
            list_users()
            users_overview_menu()
        elif choice == "d":
            delete_user()
            list_users()
            users_overview_menu()
        elif choice == "c":
            create_book()
        elif choice.isdigit():
            show_user(int(choice))
            # show_book(int(choice))
            user_menu()
        else:
            print("Invalid choice")


        # else:
        #     try:
        #         isinstance(int(choice), int)
        #         show_user(int(choice))
        #         user_menu()
        #     except:
        #         print("Invalid choice")
        
def initial_menu():
    print("\nHello! Please choose from the following:\n")
    print("Type U or u to see users")
    print("Type E or e to exit\n")

def users_overview_menu():
    print("\n******************\n")
    print("Type the user's number to see their details")
    print("Type A or a to add a new user")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

def user_menu():
    print("\n******************\n")
    print("Type the book's number to see its details")
    print("Type C or c to add a new book for this user")
    print("Type D or d to delete this user")
    print("Type B or b to go back to previous menu")
    print("Type E or e to exit\n")

# def book_menu():
#     print("\n******************\n")
#     print("Type the book's number to see its details")
#     print("Type C or c to add a new book for this user")
#     print("Type D or d to delete this user")
#     print("Type B or b to go back to previous menu")
#     print("Type E or e to exit\n")

if __name__ == "__main__":
    main()
