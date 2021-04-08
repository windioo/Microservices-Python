from mongoengine import connect
from mongoengine import Document, StringField, DynamicDocument

connection = connect(db="rentalFilm",host="localhost",port=27017)

if connection:
    print("MongoDB Connected")

class customers(Document):
    username = StringField(required=True, max_length=70)
    fullname = StringField(required=True, max_length=20)
    email = StringField(required=True, max_length=20)