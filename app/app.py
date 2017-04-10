# -*- coding:utf-8 -*-
#import sys
import os
import json as json2
from datetime import date, time, datetime
from flask import Flask,request, Response, jsonify, url_for, json, make_response
from flask_httpauth import HTTPBasicAuth

from models.clientes import Cliente, User

from settings import EXPIRATION_TOKEN, JSON_AS_ASCII

auth = HTTPBasicAuth()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = JSON_AS_ASCII

@app.errorhandler(404)
def not_found(error=None):
        message = {"success":False,"error":"Not Found "+request.url}
        return make_response(jsonify(message),404)

@app.errorhandler(500)
def set_error(error=None):
        message = {"success":False,"error":"Internal Server Error "+request.url}
        return make_response(jsonify(message),500)

@auth.verify_password
def verify_password(username_or_token, password):
        user_id = Cliente.verificar_auth_token(username_or_token)
        if user_id:
                return True
        else:
                return False
                
@auth.error_handler
def unauthorized():
        message = {"success":False,"error":"Unauthorized access: "+request.url}
        message.update({"codigo":401})
        return make_response(jsonify(message),200)

@app.route("/",methods=["GET"])
def index():
        return jsonify({'api':u'Movilidad Escolar v0.1'})


@app.route("/api/signup", methods=["POST"])
def sign_up():
        signup_params = ("email","password","pasword_confirm")
        data = request.get_json()
        print data["email"]
        print data, "^"*20
        user = User(**data)
        message = {"success":True,"data":user.to_dict()}
        return make_response(jsonify(message),200)
        
@app.route("/api/login",methods=["POST"])
def login():
        login_params = ('username','password')
        credential = request.get_json()
        cliente = Cliente.login(credential["username"],credential["password"])
        if cliente:
                print "#"*20, EXPIRATION_TOKEN
                token = cliente.generar_token(expiration=EXPIRATION_TOKEN)
                status_code = 200
                message = {
                        "success":True,
                        "error":None,
                        "token":token.decode("ascii"),
                        "data":cliente.stringify()}
        else:
                status_code = 401
                message = {"success":False,"error":"Usuario y/o clave incorrecto(s)"}
        message.update({"codigo":status_code})
        return make_response(jsonify(message),200)
        
@app.route("/api/test/token",methods=["GET","POST"])   
@auth.login_required
def test_token():
        return jsonify({"success":"ok"},200)
        
@app.route("/api/cliente/<string:codigo>",methods=["GET"])
@auth.login_required
def get_cliente(codigo):
        if codigo.isdigit():
                cliente = Cliente.get(codigo)
                data = cliente.stringify()
                status_code = 200
                message = {"success":True,"error":"","data":data}
        else:
                status_code = 400 # bad request
                message = {"success":False,"error":"Bad Request"}
        message.update({"codigo":status_code})
        return make_response(jsonify(message),200)



if __name__ == "__main__":
        #reload(sys)
        #sys.setdefaultencoding('utf8')
        port = int(os.getenv("PORT", 8080))
        ip = os.getenv("IP", "0.0.0.0")
        print " %s:%s" % (ip,port)
        app.run(debug=True,host=ip,port=port)