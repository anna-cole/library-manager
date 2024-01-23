from helpers import (
    exit_program,
    list_users,
    find_user_by_name,
    find_user_by_id,
    create_user,
    update_user,
    delete_user,
    list_books,
    find_book_by_title,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
    list_user_books
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            find_user_by_name()
        elif choice == "3":
            find_user_by_id()
        elif choice == "4":
            create_user()
        elif choice == "5":
            update_user()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            list_books()
        elif choice == "8":
            find_book_by_title()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            create_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            list_user_books()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all users")
    print("2. Find user by name")
    print("3. Find user by id")
    print("4: Create user")
    print("5: Update user")
    print("6: Delete user")
    print("7. List all books")
    print("8. Find book by title")
    print("9. Find book by id")
    print("10: Create book")
    print("11: Update book")
    print("12: Delete book")
    print("13: List all books of a user")

if __name__ == "__main__":
    main()
