from helpers import (
    exit_program,
    list_users,
    show_user,
    create_user,
    delete_user,
    get_book_id, 
    create_book

    # find_user_by_name,
    # find_user_by_id,
    # update_user,
    # find_book_by_title,
    # find_book_by_id,
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
            users_overview_menu()
        elif choice == "b":
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
            user_menu()
        else:
            print("Invalid choice")

        # elif choice.isdigit():
        #     find_book_by_id(int(choice)) 
        # else:
        #     try:
        #         isinstance(int(choice), int)
        #         show_user(int(choice))
        #         user_menu()
        #     except:
        #         print("Invalid choice")


        # elif choice == "2":
        #     find_user_by_name()
        # elif choice == "5":
        #     update_user()
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
        
def initial_menu():
    print("\nHello! Please choose from the following:\n")
    print("Type U or u to see users")
    print("Type E or e to exit\n")

initial_menu()

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

    # print("Type B or b to see all books")
    # print("Type T or t to find book by title")
    # print("Type G or g to find book by gender")
    # print("Type C or c to add book")
    # print("Type H or h to find cheaper book")
    # print("Type T or t to delete book")
    # print("Type F or f to find books by user")

if __name__ == "__main__":
    main()
