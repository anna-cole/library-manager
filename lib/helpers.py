from user import User
from book import Book

def exit_program():
    choice = input("\nAre you sure you want to exit? (y/n): ")
    if choice.lower() == "y":
        print("Goodbye!\n")
        exit()
       
def list_users():
    users = User.get_all()
    print("\nAll users:")
    i = 1
    for user in users:
        print(f"{i}. {user.name}")
        i += 1

def show_user_details():
    users = User.get_all()
    input_name = input("Please enter user's name: ")
    for user in users:
        if input_name == user.name:
            print(f"\nName: {user.name}\nAddress: {user.address}\nMembership: {user.membership}")
            list_books_per_user(user)
            return user 
    else: print(f"\nUser {input_name} not found.")
    show_user_details()
    
def list_books_per_user(user): 
    print(f"\n{user.name}'s books:")  
    books = user.books()
    i = 1
    for book in books:
        print(f"{i}. {book.title}")
        i += 1
    
   
#recomecar daqui
def show_book(num):
    books = user.books()
    book = books[num - 1]
    print(f"\nTitle: {book.title}\nGenre: {book.genre}") 




    
def create_user():
    name = input("Enter the user's name: ")
    address = input("Enter the user's address: ")
    membership = input("Enter user's membership level: ")
    try:
        user = User.create(name, address, membership)
        print(f'\nSuccess: {user.name} created.')
    except Exception as exc:
        print("Error creating user: ", exc)

def create_book(user):
    title = input("Enter the book's title: ")
    genre = input("Enter the book's genre: ")
    user_id = user.id
    try:
        book = Book.create(title, genre, user_id)
        print(f'\nSuccess: {book.title} book created for {user.name}.\n')
        list_books_per_user(user)
    except Exception as exc:
            print('Error creating book: ', exc)

def delete_user():
    input_user = input("Enter user's name to confirm: ")
    user = User.find_by_name(input_user)
    if user:
        user.delete()
        print(f'User {user.name} deleted')
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