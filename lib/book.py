from __init__ import CURSOR, CONN
from user import User

class Book:

  all = {}

  def __init__(self, title, genre, user_id, id=None):
    self.id = id
    self.title = title
    self.genre = genre
    self.user_id = user_id

  def __repr__(self):
    return (
      f"<Book {self.id}: {self.title}, {self.genre}, " +
      f"User ID: {self.user_id}>"
    )

  @property
  def title(self):
    return self._title

  @title.setter
  def title(self, title):
    if isinstance(title, str) and len(title):
      self._title = title
    else:
      raise ValueError("Title must be a non-empty string")

  @property
  def genre(self):
    return self._genre

  @genre.setter
  def genre(self, genre):
    if isinstance(genre, str) and len(genre):
      self._genre = genre
    else:
      raise ValueError("Genre must be a non-empty string")

  @property
  def user_id(self):
    return self._user_id

  @user_id.setter
  def user_id(self, user_id):
    if type(user_id) is int and User.find_by_id(user_id):
      self._user_id = user_id
    else:
      raise ValueError("user_id must reference a user in the database")

  @classmethod
  def create_table(cls):
    """ Create a new table to persist the attributes of Book instances """
    sql = """
      CREATE TABLE IF NOT EXISTS books (
      id INTEGER PRIMARY KEY,
      title TEXT,
      genre TEXT,
      user_id INTEGER,
      FOREIGN KEY (user_id) REFERENCES users(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    """ Drop the table that persists Book instances """
    sql = """
      DROP TABLE IF EXISTS books;
    """
    CURSOR.execute(sql)
    CONN.commit()

  def save(self):
    """ Insert a new row with the title, genre, and user id values of the current Book object.
    Update object id attribute using the primary key value of new row.
    Save the object in local dictionary using table row's PK as dictionary key"""
    sql = """
      INSERT INTO books (title, genre, user_id)
      VALUES (?, ?, ?)
    """

    CURSOR.execute(sql, (self.title, self.genre, self.user_id))
    CONN.commit()

    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self

  def update(self):
    """Update the table row corresponding to the current Book instance."""
    sql = """
      UPDATE books
      SET title = ?, genre = ?, user_id = ?
      WHERE id = ?
    """
    CURSOR.execute(sql, (self.title, self.genre, self.user_id, self.id))
    CONN.commit()

  def delete(self):
    """Delete the table row corresponding to the current Book instance,
    delete the dictionary entry, and reassign id attribute"""

    sql = """
      DELETE FROM books
      WHERE id = ?
    """

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    # Delete the dictionary entry using id as the key
    del type(self).all[self.id]

    # Set the id to None
    self.id = None

  @classmethod
  def create(cls, title, genre, user_id):
    """ Initialize a new Employee instance and save the object to the database """
    book = cls(title, genre, user_id)
    book.save()
    return book

  @classmethod
  def instance_from_db(cls, row):
    """Return an Book object having the attribute values from the table row."""

    # Check the dictionary for existing instance using the row's primary key
    book = cls.all.get(row[0])
    if book:
      # ensure attributes match row values in case local instance was modified
      book.title = row[1]
      book.genre = row[2]
      book.user_id = row[3]
    else:
      # not in dictionary, create new instance and add to dictionary
      book = cls(row[1], row[2], row[3])
      book.id = row[0]
      cls.all[book.id] = book
    return book  

  @classmethod
  def get_all(cls):
    """Return a list containing one Book object per table row"""
    sql = """
      SELECT *
      FROM books
    """

    rows = CURSOR.execute(sql).fetchall()
    return [cls.instance_from_db(row) for row in rows]
    
  @classmethod
  def find_by_id(cls, id):
    """Return Book object corresponding to the table row matching the specified primary key"""
    sql = """
      SELECT *
      FROM books
      WHERE id = ?
    """

    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None

  @classmethod
  def find_by_title(cls, title):
    """Return Book object corresponding to first table row matching specified title"""
    sql = """
      SELECT *
      FROM books
      WHERE title is ?
    """

    row = CURSOR.execute(sql, (title,)).fetchone()
    return cls.instance_from_db(row) if row else None
  

# print(Book.get_all())
  
 

