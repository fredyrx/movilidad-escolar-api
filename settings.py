# -*- coding:utf-8 -*-

SECRET_KEY = "!&nq(vhsj^mskm)ja3qow9_r_=sm)!1aka9^_$r#z!ua+@3vel"
EXPIRATION_TOKEN = 60*60*24 #  (1 min) * 60*24 = 1 dia
JSON_AS_ASCII = False

# DataBase settings
CONFIG_DB = {
	'host': '127.0.0.1',
	'port': 5432,
	'database': "movilidadDB", 
	'user': "postgres", 
	'password': "postgres"
}

def config_db():
	return CONFIG_DB
