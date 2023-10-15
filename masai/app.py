from flask import Flask, make_response, jsonify, request
import configDb

app = Flask(__name__)

if __name__ == "__app__":
    app.run(debug=True)


@app.route("user/get", methods=["GET"])
def getData():
    return make_response(configDb.getAllData(), 200)


@app.route("/user/create", methods=["POST"])
def saveUser():  # save the user and return boolean value
    data = request.get_json()
    res = configDb.createUser(data)
    obj = {
        "result": res
    }
    if res:
        return make_response(obj, 201)
    else:
        return make_response(obj, 400)


@app.route("/user/checkMobile/<mobile>", methods=["GET"])
# check mobile number if it avliable in our db or not {return true/ false}
def checkMobileNumber(mobile):
    res = configDb.checkMobile(mobile)
    obj = {
        "result": res
    }
    if res:
        return make_response(obj, 201)
    else:
        return make_response(obj, 400)


@app.route("/user/checkEmail/<email>", methods=["GET"])
# check email if it avliable in our db or not {return true/ false}
def checkEmail(email):
    res = configDb.checkEmail(email)
    obj = {
        "result": res
    }
    if res:
        return make_response(obj, 201)
    else:
        return make_response(obj, 400)


@app.route("/user/login/UsingMobile", methods=["POST"])
def mobileLogin():   # we get user mobile and password in JSON formate
    data = request.get_json()
    res = configDb.loginUsingMobile(data)
    return make_response({"result": res}, 200)


@app.route("/user/login/UsingEmail", methods=["POST"])
def emailLogin():   # we get user email and password in JSON formate
    data = request.get_json()
    res = configDb.loginUsingEmail(data)
    return make_response({"result": res}, 200)
