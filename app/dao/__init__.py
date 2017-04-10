import psycopg2
from settings import config_db

class QueryResponse(object):
	def __init__(self,data=[],error=False,message=""):
		self.data = data
		self.error = error
		self.message = message

	def set_data(self,data):
		self.data = data

	def set_error(self):
		self.error = True

	def set_message(self, message):
		self.message = message

	def get_dict(self):
		return self.__dict__

def get_connection():
	params = config_db()
	return psycopg2.connect(**params)

def basic_callproc(sp_name,params=list()):
	conn = None
	result = QueryResponse()
	try:
		conn = get_connection()
		cur = conn.cursor()
		cur.callproc(sp_name,params)
		# Procesamos el resultado
		rows = cur.fetchall()
		result.set_data(rows)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		result.set_error()
		result.set_message(error)
	finally:
		if conn is not None:
			conn.close()

	return result.get_dict()

def execute(query,params=list(),has_result=True):
	conn = None
	result = QueryResponse()
	try:
		conn = get_connection()
		cur = conn.cursor()
		cur.execute(query,params)
		# Procesamos el resultado
		if has_result:
			rows = cur.fetchall()
			result.set_data(rows)
		else:
			conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		result.set_error()
		result.set_message(error)
	finally:
		if conn is not None:
			conn.close()

	return result.get_dict()

def exec_query(query,params=list()):
	return execute(query,params,has_result=True)

def exec_save(query,params=list()):
	return execute(query,params,has_result=False)

