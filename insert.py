import database


def insert(value, metric, id, time):
	conn = database.createConn()	
	cur = conn.cursor()
	sql = "INSERT INTO metrics (ID,value,metric,time) VALUES (%s, %s, %s, %s)"
	value = (id,value,metric,time)
	cur.execute(sql,value)
	conn.commit()
	print(cur.rowcount, "record inserted.")
