# -*- coding:utf-8 -*-
#import sys
import os
import json as json2
from datetime import date, time, datetime
from flask import Flask,request, Response, jsonify, url_for, json, make_response
from flask_httpauth import HTTPBasicAuth

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
	return True

@auth.error_handler
def unauthorized():
        message = {"success":False,"error":"Unauthorized access: "+request.url}
        message.update({"codigo":401})
        return make_response(jsonify(message),200)

@app.route("/",methods=["GET"])
def index():
        return jsonify({'api':u'Movilidad Escolar v0.1'})

if __name__ == "__main__":
        #reload(sys)
        #sys.setdefaultencoding('utf8')
        port = os.getenv("PORT", 8080)
        ip = os.getenv("IP", "0.0.0.0")
        print " %s:%s" % (ip,port)
        app.run(debug=True,host=ip,port=port)