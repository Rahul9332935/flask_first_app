from flask import Flask, make_response
from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ["DB_CONN_STR"]
engine = create_engine(db_conn_str,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })


def getAllData():
    with engine.connect() as con:
        result = con.execute(text("select * from user1"))
        # str-  "insert into user (name, mobile, email, password) values (:name, :mobile, :email, :password)"
        result_all = result.all()
        list = []
        for data in result_all:
            obj = {
                "id": data[0],
                "name": data[1],
                "mobile": data[2],
                "email": data[3]
            }
            list.append(obj)
        return list


def checkMobile(mobile):

    with engine.connect() as con:
        query = text(f"SELECT * FROM user1 WHERE mobile = '{mobile}'")
        result = con.execute(query)
        result_all = result.fetchall()

    if len(result_all):
        # Mobile number exists in the database
        return True
    else:
        # Mobile number does not exist in the database
        return False


def checkEmail(email):

    with engine.connect() as con:
        query = text(f"SELECT * FROM user1 WHERE email = '{email}'")
        result = con.execute(query)
        result_all = result.fetchall()

    if len(result_all):
        # email exists in the database
        return True
    else:
        # email does not exist in the database
        return False


# obj= { "email":"rahul1@gmail.com", "password":"password"};
def loginUsingEmail(obj):
    if checkEmail(obj["email"]):
        with engine.connect() as con:
          query = text(
                "SELECT * FROM user1 WHERE email = :e && password = :pas")
            result = con.execute(query, e=obj['email'], pas=obj['password'])
            result_all = result.fetchall()
            if len(result_all):
                # email exists in the database
                return (result_all[0])[1]  # return user name
            else:
                # email does not exist in the database
                return "wrong password!!"
    else:
        return "please signUp!!"


# mobile number should not be less then and  more than 10 digit
# obj= { "mobile":"5945451256", "password":"password"};
def loginUsingMobile(obj):
    if checkMobile(obj["mobile"]):
        with engine.connect() as con:
            query = text(
                f"SELECT * FROM user1 WHERE mobile = '{obj["mobile"]}' && password = '{obj["password"]}'")
            result = con.execute(query)
            result_all = result.fetchall()
            if len(result_all):
                # mobile exists in the database
                return (result_all[0])[1]  # return user name
            else:
                # mobile does not exist in the database
                return "wrong password!!"
    else:
        return "please signUp!!"


def createUser(obj):
    if checkEmail(obj["email"]):
        return "email already exist!!"
    elif checkMobile(obj["mobile"]):
        print(obj["mobile"])
        return "mobile already exist!!"
    else:
        with engine.connect() as con:
            query = text(f"INSERT INTO user1 (name, mobile, email, password) values ('{
                         obj["name"]}', '{obj["mobile"]}', '{obj["email"]}', '{obj["password"]}')")
            con.execute(query)
            con.commit()
            if checkEmail(obj["email"]) & checkMobile(obj["mobile"]):
                return "successfully registered!! "
            else:
                return "try again!!"


# obj= { "mobile":"1234467890", "password":"password123"}
# data = {
#     "name": "Ashish",
#     "mobile": "9648472430",
#     "email": "Ashish@gmail.com",
#     "password": "password123"
# }
# print(createUser(data))
# """""create table user1(
# id INT NOT NULL AUTO_INCREMENT,
# name varchar(50) NOT NULL,
# mobile varchar(10) NOT NULL,
# email varchar(100) NOT NULL UNIQUE,
# password varchar(100) NOT NULL,
# PRIMARY KEY(id)
# )"""""
