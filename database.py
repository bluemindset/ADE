import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def createConn():
 	connection = mysql.connector.connect(host='localhost',
                             database='nodes',
                             user='root',
                             password='root')
	return connection 
