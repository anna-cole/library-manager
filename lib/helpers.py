from user import User
from book import Book

def exit_program():
    print("Goodbye!\n")
    exit()
       
def list_users():
    users = User.get_all()
    i = 1
    while i <= len(users):
        for user in users:
            print(f"{i}. {user.name}")
            i += 1

def show_user(num):
    users = User.get_all()
    user = users[num - 1]
    print(f"\nName: {user.name}\nAddress: {user.address}\nMembership: {user.membership}\n{user.name}'s books:")
    list_books_per_user(user)
    
def list_books_per_user(user):   
    books = user.books()
    i = 1
    while i <= len(books):
        for book in books:
            print(f"{i}. {book.title}")
            i += 1

def create_book():
    input_user = input("Enter user's name: ")
    title = input("Enter the book's title: ")
    genre = input("Enter the book's genre: ")
    user = User.find_by_name(input_user)
    user_id = user.id
    try:
        if user_id := User.find_by_id(user_id).id:
            book = Book.create(title, genre, user_id)
            print(f'Success: {book.title} created.')
        else:
            print(f'User {user_id} not found.')
    except Exception as exc:
            print('Error creating book: ', exc)

def show_book(num):
    books = Book.get_all()
    book = books[num - 1]
    print(f"\nTitle: {book.title}\nGenre: {book.genre}")

def create_user():
    name = input("Enter the user's name: ")
    address = input("Enter the user's address: ")
    membership = input("Enter user's membership level: ")
    try:
        user = User.create(name, address, membership)
        print(f'Success: {user.name} created.')
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user():
    input_user = input("Enter user's name: ").lower()
    user = User.find_by_name(input_user)
    if user:
        user.delete()
        print(f'User {user.name} deleted\n')
    else:
        print(f"User {input_user} not found")

   
           
        
def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(f'Book {title} not found.')

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