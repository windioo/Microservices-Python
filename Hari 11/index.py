from pymongo import MongoClient
# from bson import ObjectId  #kalau id = objectid
# <Koneksi>

nosql_db = MongoClient(host="localhost", port=27017)
print(nosql_db)
print("Berhasil Koneksi")
print("--------------------------------")
# <tutup koneksi>

# nosql_db.close()
# print("Koneksi Diputus")

# <Cek Database>
# print(nosql_db.list_database_names())
db = nosql_db.rentalFilm #pilih nama database
mongo_doc = db.bios #pilih table
# print(mongo_doc)

# <Membaca Data>
query =  {"_id": ObjectId("51df07b094c6acd67e492f41")}
result = mongo_doc.find(query)

for data in result:
    print(data)


# <Insert Data>
# satu data
# data = {} 
# mongo_doc.insert_one(data)

# # banyak data
# data = {[]}
# mongo_doc.insert_many(data)

# <Ubah Data>
# mongo_doc.update({query syarat}, {nilai pengganti})

# <Hapus Data>
# mongo_doc.delete({syarat})

nosql_db.close()