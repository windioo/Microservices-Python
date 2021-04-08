from mongoengine import connect
from mongoengine import Document, StringField, DynamicDocument, ObjectIdField , IntField
from bson import ObjectId

connection = connect(db="perpustakaan",host="localhost",port=27017)

if connection:
    print("MongoDB Connected")

class books(Document):
    _id = ObjectIdField(primary_key=True) 
    nama = StringField(required=True, max_length=70)
    pengarang = StringField(required=True, max_length=20)
    tahun_terbit = StringField(required=True, max_length=20)
    genre = StringField(required=True, max_length=20)