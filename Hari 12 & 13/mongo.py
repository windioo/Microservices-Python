from models.customers_mongo import customers

#CARI SEMUA DATA
# for doc in customers.objects:
#     print(doc.username,doc.fullname,doc.email)

#CARI DATA BERDASARKAN ID
# for doc in customers.objects(_id=2):
#     print (doc.username, doc.fullname, doc.email)

#INSERT
# data = {
#     "username" : 'Mary',
#     "fullname" : 'Mary Marijoa', 
#     "email" : 'mary@gmail.com'
# }

# customers(**data).save()
# for doc in customers.objects:
#     print (doc.username, doc.fullname, doc.email)

#UPDATE
# doc_1 = customers.objects(username='Mary').first()
# print (doc_1.to_json())

# doc_1.username = 'MM'
# doc_1.save()

# print (customers.objects().to_json())

#DELETE
doc_1 = customers.objects(username='Mary').first()
doc_1.delete()

print (customers.objects().to_json())