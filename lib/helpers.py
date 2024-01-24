from user import User
from book import Book

def exit_program():
    print("Goodbye!\n")
    exit()

# User functions
    
def list_users():
    users = User.get_all()
    for user in users:
        print(f"{user.id}. {user.name}")

def show_user_details(input_id):
    user = User.find_by_id(input_id)
    if user:
        print(f"\nName: {user.name}\nAddress: {user.address}\nMembership: {user.membership}\n{user.name}'s books:")
        books = user.books()
        for book in books:
            print(f"{book.id}. {book.title}")
    else:
        print(f'User {input_id} not found')

def find_user_by_name():
    name = input("Enter the user's name: ")
    user = User.find_by_name(name)
    print(user) if user else print(f'User {name} not found')

def find_user_by_id():
    id_ = input("Enter the user's id: ")
    user = User.find_by_id(id_)
    print(user) if user else print(f'User {id_} not found')

def create_user():
    name = input("Enter the user's name: ")
    address = input("Enter the user's address: ")
    membership = input("Enter the user's membership level: ")
    try:
        user = User.create(name, address, membership)
        print(f'Success: {user.name} user created.')
    except Exception as exc:
        print("Error creating user: ", exc)

def update_user():
    id_ = input("Enter the user's id: ")
    if user := User.find_by_id(id_):
        try:
            name = input("Enter the user's new name: ")
            user.name = name
            address = input("Enter the user's new address: ")
            user.address = address

            user.update()
            print(f'Success: {user} updated.')
        except Exception as exc:
            print("Error updating user: ", exc)
    else:
        print(f'User {id_} not found')

def delete_user():
    id_ = input("Enter the user's id: ")
    if user := User.find_by_id(id_):
        user.delete()
        print(f'User {id_} deleted')
    else:
        print(f'User {id_} not found')


# Book functions

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)
  
def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(f'Book {title} not found.')
    
def find_book_by_id():
    id_ = input("Enter the book's id ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f"Book {id_} not found.")

def create_book():
    title = input("Enter the book's title: ")
    genre = input("Enter the book's genre: ")
    user_id = input("Enter the user's id: ")
    try:
        if user_id := User.find_by_id(user_id).id:
            book = Book.create(title, genre, user_id)
            print(f'Success: {book} created.')
        else:
            print(f'User {user_id} not found.')
    except Exception as exc:
            print('Error creating book: ', exc)

def update_book():
    book_id = input("Enter the book's id: ") 
    if book := Book.find_by_id(book_id):
        try:
            title = input("Enter the book's new title: ")
            book.title = title
            genre = input("Enter the book's new genre: ")
            book.genre = genre
            user_id = input("Enter the book's new user id: ")   
            if user_id := User.find_by_id(user_id).id:
                book.user_id = user_id
                book.update()
                print(f'Success: {book} updated.')
        except Exception as exc:
            print('Error updating book: ', exc)
    else:
        print(f'Book {book_id} not found.')

def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted.')
    else:
        print(f'Book {id_} not found.')

# def list_user_books(input_id):
#     user = User.find_by_id(input_id)
#     if user:
#         books = user.books()
#         for book in books:
#             print(f"{book.id}. {book.title}")
#     else:
#         print(f'User not found.')

# list_books()