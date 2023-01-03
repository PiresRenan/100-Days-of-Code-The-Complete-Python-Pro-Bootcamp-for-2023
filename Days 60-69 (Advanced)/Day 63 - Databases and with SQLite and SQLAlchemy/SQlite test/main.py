# Just using sqlite 
import sqlite3

# create database
db = sqlite3.connect("books-collection.db")
# create cursor
cursor = db.cursor()
# create tables
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )
# ADD INFO INTO DATABASE
cursor.execute(
    "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')"
)
db.commit()

