from helpers import (
    exit_program,
    list_users,
    show_user_details,
    create_user,

    # find_user_by_name,
    # find_user_by_id,
    # update_user,
    # delete_user,
    # list_books,
    # find_book_by_title,
    # find_book_by_id,
    # create_book,
    # update_book,
    # delete_book,
    #list_user_books
)

def main():
    while True:
        choice = input("> ").lower()
        if choice == "e":
            exit_program()
        elif choice == "u":
            list_users()
            menu2()
        elif choice == "b":
            menu()
        elif isinstance(choice, str) and choice != 'a':
            show_user_details(choice)
            menu3()
        elif choice == "a":
            create_user()
            list_users()
            menu2()

 

        # elif choice == "2":
        #     find_user_by_name()
        # elif choice == "3":
        #     find_user_by_id()
        # elif choice == "5":
        #     update_user()
        # elif choice == "6":
        #     delete_user()
        # elif choice == "7":
        #     list_books()
        # elif choice == "8":
        #     find_book_by_title()
        # elif choice == "9":
        #     find_book_by_id()
        # elif choice == "10":
        #     create_book()
        # elif choice == "11":
        #     update_book()
        # elif choice == "12":
        #     delete_book()
        # elif choice == "13":
        #     list_user_books()
        else:
            print("Invalid choice")

def menu():
    print("\nPlease choose from the following:\n")
    print("Type U or u to see the users")
    print("Type E or e to exit\n")

menu()

def menu2():
    print("\n******************\n")
    print("Please select the number of the user to see their details\n    or")
    print("Type B or b to go back to the previous menu")
    print("Type A or a to add a new user")
    print("Or type E or e to exit\n")

def menu3():
    print("\n******************\n")
    print("Please choose from the following:\n")
    print("Type the number of the book to see its details\n    or")
    print("Type A or a to add a new book for this user")
    print("Type D or d to delete this user")
    print("Type B or b to go back to the previous menu")
    print("Or type E or e to exit\n")

    # print("Or type E or e to exit")
    # print("Type D or d do delete user")
    # print("Type B or b to see all books")
    # print("Type T or t to find book by title")
    # print("Type G or g to find book by gender")
    # print("Type C or c to add book")
    # print("Type H or h to find cheaper book")
    # print("Type T or t to delete book")
    # print("Type F or f to find books by user")

if __name__ == "__main__":
    main()
