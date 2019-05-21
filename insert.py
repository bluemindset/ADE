import database
import time 
import datetime
def insert(value, metric, id):
	conn = database.createConn()	
	cur = conn.cursor()
	ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	if metric == 'C':
		sql = "INSERT INTO current (ID,value,time) VALUES (%s, %s, %s)"
	elif metric == 'H':
		sql = "INSERT INTO humidity (ID,value,time) VALUES (%s, %s, %s)"
	elif metric == 'T':
		sql = "INSERT INTO temperature (ID,value,time) VALUES (%s, %s, %s)"
	elif metric == 'V':
		sql = "INSERT INTO voltage (ID,value,time) VALUES (%s, %s, %s)"
	value = (id,value,timestamp)
	cur.execute(sql,value)
	conn.commit()
	print(cur.rowcount, "record inserted.")
