#!/usr/bin/env python3
# python lib/debug.py

from __init__ import CONN, CURSOR
from user import User
from book import Book

def reset_database():
  Book.drop_table()
  User.drop_table()
  User.create_table()
  Book.create_table()
  print('Database resetted')

  # Create seed data
  arya = User.create("Arya", "13 Winterfell blvd", "Gold")
  loras = User.create("Loras", "14 Highgarden st", "Silver")
  syrio = User.create("Syrio", "15 Braavos rd", "Platinum")
  daenerys = User.create("Daenerys", "16 Dragonstone blvd", "Silver")
  Book.create("A Song Of Ice And Fire", "Fantasy", arya.id)
  Book.create("The Other Side Of Midnight", "Thriller", arya.id)
  Book.create("Ramses: The Son Of Light", "Biography", syrio.id)
  Book.create("It", "Horror", loras.id)
  Book.create("The Da Vinci Code", "Thriller", loras.id)
  Book.create("The Secret", "Self-help", syrio.id)
  Book.create("Stardust", "Fantasy", daenerys.id)

breakpoint()
#reset_database()







