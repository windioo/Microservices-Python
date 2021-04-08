from pymongo import MongoClient
from models.books import database as db
from bson import ObjectId
import csv



def add_book():
    data = open("Hari 11/bestsellers-with-categories.csv",encoding='utf-8')
    books = csv.reader(data, delimiter=',')
    next(books)

    for book in books:
        try:
            data = {
                "nama": book[0],
                "pengarang": book[1],
                "tahun_terbit": book[5],
                "genre": book[6]
            }
            db.insertBook(data)
        except Exception as e:
            print("Kesalahan pada saat memasukan data: {}".format(e))
            break

def search_books(params):
    for book in db.searchBookByName(params):
        print(book)      

def search_all_books():
    for book in db.showBooks():
        print(book)

def search_books_by_id(params):
    for book in db.showBookById(params):
        print(book)

def update_books(key,values):
    for book in db.updateBookById(key,values):
        print(book)

def delete_books(key):
    for book in db.deleteBookById(key):
        print(book)

if __name__ == "__main__":
    db = db()
    add_book()
    # search_books("harry")
    # search_all_books()
    # search_books_by_id(ObjectId("606c46c963601a3fcc0c6778"))
    # update_books(ObjectId("606c46c963601a3fcc0c6779"),"11/22/63: A Novels")
    # delete_books(ObjectId("606c46c963601a3fcc0c6779"))
    db.nosql_db.close()        

