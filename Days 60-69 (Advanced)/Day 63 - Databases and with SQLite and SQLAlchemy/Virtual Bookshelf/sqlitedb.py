import sqlite3

db = sqlite3.connect("books-colletionSQLite.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(256) NOT NULL UNIQUE, author varchar(256) NOT NULL, rating FLOAT NOT NULL);")
cursor.execute("INSERT INTO books (id, title, author, rating) VALUES (1, 'Harry Potter', 'J. K. Rowling', '9.3');")
db.commit()
