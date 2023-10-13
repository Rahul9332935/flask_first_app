from flask import Flask, make_response
from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://root:root@localhost:3306/masaiSED?charset=utf8mb4")

def getAllData():
    with engine.connect() as con:
        result = con.execute(text("select * from user"))
        #str-  "insert into user (name, mobile, email, password) values (:name, :mobile, :email, :password)"
        result_all = result.all()
        list =[]
        for data in result_all:
            obj= {
                "id": data[0],
                "name":data[1],
                "mobile":data[2],
                "email":data[3],
                "password": data[4]
            }
            list.append(obj)
        return list

def checkMobile(mobile):
    
    with engine.connect() as con:
        query = text(f"SELECT * FROM user WHERE mobile =  '{mobile}'")
        result = con.execute(query)
        result_all = result.fetchall()

    if result_all:
        # Mobile number exists in the database
        return True
    else:
        # Mobile number does not exist in the database
        return False
    
def checkEmail(email):
    
    with engine.connect() as con:
        query = text(f"SELECT * FROM user WHERE email =  '{email}'")
        result = con.execute(query)
        result_all = result.fetchall()

    if result_all:
        # email exists in the database
        return True
    else:
        # email does not exist in the database
        return False
    

def loginUsingEmail(obj):  #obj= { "email":"rahul1@gmail.com", "password":"password"};
    if checkEmail(obj["email"]) :
        with engine.connect() as con:
            query = text(f"SELECT * FROM user WHERE email =  '{obj["email"]}' && password = '{obj["password"]}'")
            result = con.execute(query)
            result_all = result.fetchall()
            print(result_all)
            if result_all:
                # email exists in the database
                return (result_all[0])[1] # return user name
            else:
                # email does not exist in the database
                return "wrong password!!"
    else:
        return "please signUp!!"

#mobile number should not be less then and  more than 10 digit
def loginUsingMobile(obj):  #obj= { "mobile":"5945451256", "password":"password"}; 
    if checkMobile(obj["mobile"]) :
        with engine.connect() as con:
            query = text(f"SELECT * FROM user WHERE mobile =  '{obj["mobile"]}' && password = '{obj["password"]}'")
            result = con.execute(query)
            result_all = result.fetchall()
            print(result_all)
            if result_all:
                # mobile exists in the database
                return (result_all[0])[1] # return user name
            else:
                # mobile does not exist in the database
                return "wrong password!!"
    else:
        return "please signUp!!"

#post request
"""
data = {
"name": "Rahul Kumar",
"mobile" : "8989564574",
"email": "rahul933295@gmail.com",
"password" : "password"
}"""

def createUser(obj):
    if checkEmail(obj["email"]):
        return "email already exist!!"
    elif checkMobile(obj["mobile"]):
        print(obj["mobile"])
        return "mobile already exist!!"
    else:
        with engine.connect() as con:
            query = text(f"INSERT INTO user (name, mobile, email, password) values ( '{obj["name"]}', '{obj["mobile"]}', '{obj["email"]}', '{obj["password"]}')")
            con.execute(query)
            con.commit()
            


# obj= { "mobile":"1234467890", "password":"password123"}
data = {
"name": "An4kit89",
"mobile" : "1454338996",
"email": "an45ekit4@ex1ample.com",
"password" : "passwo5rd132"
}
createUser(data)

# print(loginUsingMobile(obj))
