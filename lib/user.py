from __init__ import CURSOR, CONN

class User:
  
    all = {}

    def __init__(self, name, address, membership, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.membership = membership

    # def __repr__(self):
    #     return f"<User {self.id}: {self.name}, {self.address}, {self.membership}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address
        else:
            raise ValueError("Address must be a non-empty string")
        
    @property
    def membership(self):
        return self._membership

    @membership.setter
    def membership(self, membership):
        if isinstance(membership, str) and len(membership):
            self._membership = membership
        else:
            raise ValueError("Membership must be a non-empty string")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of User instances """
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            membership TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists User instances """
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and address values of the current User instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO users (name, address, membership)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.address, self.membership))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address, membership):
        """ Initialize a new User instance and save the object to the database """
        user = cls(name, address, membership)
        user.save()
        return user

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE users
            SET name = ?, address = ?, membership = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.address, self.membership, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        user = cls.all.get(row[0])
        if user:
            # ensure attributes match row values in case local instance was modified
            user.name = row[1]
            user.address = row[2]
            user.membership = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            user = cls(row[1], row[2], row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM users
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a User object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM users
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def books(self):
        """Return list of books associated with current user"""
        from book import Book
        sql = """
            SELECT * FROM books
            WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Book.instance_from_db(row) for row in rows]