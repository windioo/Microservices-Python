from models.customers import Customers,session



# <Melihat Semua Data>

result =  session.query(Customers).all()
for row in result:
    print(row.id, row.username, row.namaLengkap, row.email)

# <Melihat Data id = 2>

# result = session.query(Customers).filter(Customers.id==2)
# for row in result:
#     print(row.id, row.username, row.namaLengkap, row.email)

# data = {
#     "username" : 'RK',
#     "namaLengkap" : 'Ravi Kumar', 
#     "email" : 'ravi@gmail.com'
# }

# <Insert Data>

# session.add(Customers(**data))
# session.commit()

# <Ubah Data>

# result =  session.query(Customers).filter(Customers.id==3).one()
# print(result.id, result.username, result.namaLengkap, result.email)
# result.username = "RaviK"
# session.commit()

# result =  session.query(Customers).filter(Customers.id==3).one()
# print(result.id, result.username, result.namaLengkap, result.email)

# <Hapus Data>
# result =  session.query(Customers).filter(Customers.id==3).one()
# print(result.id, result.username, result.namaLengkap, result.email)
# session.delete(result)
# session.commit()

# result =  session.query(Customers).all()
# for row in result:
#     print(row.id, row.username, row.namaLengkap, row.email)