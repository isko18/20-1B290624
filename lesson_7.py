from database import Database

class Author:
    def __init__(self, name, bith_year):
        self.name = name 
        self.birth_year = bith_year
        
    def __str__(self):
        return f'Автор: {self.name}, год рождения: {self.birth_year}'
    
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        
    def __str__(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год публикации: {self.publication_year}'
    
class Library:
    def __init__(self, db: Database):
        self.db = db 
        
    def add_author(self, author):
        if not self.db.get_author(author.name):
            self.db.add_author(author.name, author.birth_year)
            
    def add_book(self, book):
        author = self.db.get_author(book.author.name)
        if author in None:
            self.add_author(book.author)
            author = self.db.get_author(book.author.name)