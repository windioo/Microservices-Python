from pymongo import MongoClient

class database:
    def __init__ (self):
        try:
            self.nosql_db =MongoClient(host="localhost",port=27017)
            self.db = self.nosql_db.perpustakaan
            self.mongo_col = self.db.books
            print("database connected")
        except Exception as e:
            print(e)

    def showBooks(self):
        result = self.mongo_col.find()
        return result

    def showBookById(self,key):
        query = {"_id":key} 
        result = self.mongo_col.find(query)
        return result

    def searchBookByName(self,key):
        query = {"nama":{"$regex":key,"$options":"i"}} 
        #options digunakan untuk melakukan konfigurasi pada regex kita, opsi "i" melambangkan case insensitive, artinya "indonesia" dan "INDONESIA" akan dianggap kata yang sama.
        result = self.mongo_col.find(query)
        return result

    def insertBook(self,document):
        self.mongo_col.insert_one(document)


    def updateBookById(self,key,values):
        query = {"_id":key}
        new_values = {"$set" : {"nama" : values}}
        result = self.mongo_col.update(query,new_values)
        return result

    def deleteBookById(self,key):
        query = {"_id":key}
        result = self.mongo_col.remove(query)
        return result 
