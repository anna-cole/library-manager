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

def show_user(num):
    users = User.get_all()
    try:
        user = users[num - 1]
        print(f"\nName: {user.name}\nAddress: {user.address}\nMembership: {user.membership}")
        print(f"\n{user.name}'s books:")
        books = user.books()
        i = 1
        for book in books:
            print(f"{i}. {book.title}")
            i += 1
        return user
    except Exception as exc: 
        print("Error finding user: ", exc)
    
def create_user():
    name = input("Enter the user's name: ")
    address = input("Enter the user's address: ")
    membership = input("Enter user's membership level: ")
    try:
        user = User.create(name, address, membership)
        print(f'\nSuccess: {user.name} created.')
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user(user):
    try:
        user.delete()
        print(f'User {user.name} deleted')
    except Exception as exc:
        print("Error deleting user ", exc)

def update_user(user):
    try:
        name = input("Enter the user's new name: ")
        if name == '':
            name = user.name
        else:
            user.name = name 
        address = input("Enter the user's new address: ")
        if address == '':
            address = user.address
        else:
            user.address = address
        membership = input("Enter the user's new membership: ")
        if membership == '':
            membership = user.membership
        else: 
            user.membership = membership
        user.update()
        print(f'\nSuccess: {user.name} updated')
    except Exception as exc: 
        print("Error updating user ", exc)

def show_book(num, user):
    try:
        books = user.books()
        book = books[num - 1]
        print(f"\nHere are the details of {user.name}'s selected book:")
        print(f"\nTitle: {book.title}\nGenre: {book.genre}")
        return book
    except Exception as exc:
        print('Error finding book ', exc)

def create_book_for_user(user):
    title = input("Enter the book's title: ")
    genre = input("Enter the book's genre: ")
    user_id = user.id
    try:
        book = Book.create(title, genre, user_id)
        print(f'\nSuccess: book {book.title} created for {user.name}.\n')
    except Exception as exc:
        print('Error creating book: ', exc) 

def delete_book(book):
    try:
        book.delete()
        print(f'\nBook {book.title} deleted.')
    except Exception as exc:
        print('Error deleting book: ', exc)

def update_book(book):
    try:
        title = input("Enter the book's new title: ")
        if title == '':
            title = book.title
        else:
            book.title = title
        genre = input("Enter the book's new genre: ")
        if genre == '':
            genre = book.genre
        else:
            book.genre = genre 
        new_user = input("Enter the book's new user name: ")
        if new_user == '':
            new_user = book.user_id
        else:
            new_user_id = (User.find_by_name(new_user)).id
            book.user_id = new_user_id
        book.update()
        print(f'\nSuccess: book {book.title} updated.')
    except Exception as exc:
        print('\nError updating book: ', exc)  
 
def find_book_by_title():
    # title = input("Enter the book's title: ")
    # book = Book.find_by_title(title)
    # print(book) if book else print(f'Book {title} not found.')
    pass