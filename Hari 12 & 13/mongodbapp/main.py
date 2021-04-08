from models import books
from bson.objectid import ObjectId

def add_book(params):
    data = {
        "nama": params[0],
        "pengarang": params[1],
        "tahun_terbit": params[2],
        "genre": params[3]
    }

    books(**data).save()
    for doc in books.objects:
        print(doc.to_json())

def search_books_by_name(param):
    for doc in books.objects(nama=param):
        print(doc.to_json())

def search_all_books():
    for doc in books.objects:
         print(doc.to_json())

def search_books_by_id(param):
    for doc in books.objects(_id=param):
        print(doc.to_json())

def update_books(key,value):
    doc_1 = books.objects(_id=key).first()
    print (doc_1.to_json())

    doc_1.nama = value
    doc_1.save()

    print (books.objects().to_json())

def delete_book_by_id(key):
    doc_1 = books.objects(_id=key).first()
    doc_1.delete()

    print (books.objects().to_json())



# search_books_by_id(ObjectId("606dc67dade2ba97e1579acb"))
a = ["awan","dio","2020","fantasi"]
add_book(a)