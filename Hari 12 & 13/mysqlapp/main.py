
from models import Customers,session



# <Melihat Semua Data>
def search_all_users():
    result =  session.query(Customers).all()
    for row in result:
        print(row.userid, row.username, row.namadepan, row.namabelakang, row.email)


# <Melihat Data id = 2>
def search_user_by_id(params):
    result = session.query(Customers).filter(Customers.userid==params)
    for row in result:
        print(row.userid, row.username, row.namadepan, row.namabelakang, row.email)

def add_users(params):
# param berasa dari list
    data = {
                "username": params[0],
                "namadepan": params[1],
                "namabelakang": params[2],
                "email": params[3]
            }
# # <Insert Data>
    session.add(Customers(**data))
    session.commit()
   
def update_username_by_id(id,value):
# <Ubah Data>
    result =  session.query(Customers).filter(Customers.userid==id).one()
    print(result.userid, result.username, result.namadepan, result.namabelakang, result.email)
    result.username = value
    session.commit()

    result =  session.query(Customers).filter(Customers.userid==id).one()
    print(result.userid, result.username, result.namadepan, result.namabelakang, result.email)

def delete_user_by_id(param):

    # <Hapus Data>
    result =  session.query(Customers).filter(Customers.userid==param).one()
    print(result.userid, result.username, result.namadepan, result.namabelakang, result.email)
    session.delete(result)
    session.commit()

    result =  session.query(Customers).all()
    for row in result:
       print(row.userid, row.username, row.namadepan, row.namabelakang, row.email)


