# install Flask and SQLAlchemy 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Silence the warning 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Table 
class Book (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

# CREATE NEW RECORD 
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# with app.app_context(): 
#     db.session.add(new_book)
#     db.session.commit()

# READ ALL RECORDS 
# with app.app_context():
#     book = Book.query.filter_by(title="Harry Potter").first()

# Update A Particular Record By Query
# with app.app_context():
#     book_to_update = Book.query.filter_by(title="Harry Potter").first()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()  

# Update A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = Book.query.get(book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()  

# Delete A Particular Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = Book.query.get(book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()