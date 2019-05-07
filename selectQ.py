import database

def select():
	conn = database.createConn()
	cur = conn.cursor()

	sqlCurrent = 'SELECT * FROM current INNER JOIN(SELECT id, MAX(time) AS Maxtime FROM current GROUP BY id) toptime  ON current.id = toptime.id  AND current.time = toptime.maxtime'	
	sqlTemp = 'SELECT * FROM temperature INNER JOIN(SELECT id, MAX(time) AS Maxtime FROM temperature GROUP BY id) toptime  ON temperature.id = toptime.id  AND temperature.time = toptime.maxtime;'
	sqlHumidity = 'SELECT * FROM humidity INNER JOIN(SELECT id, MAX(time) AS Maxtime FROM humidity GROUP BY id) toptime  ON humidity.id = toptime.id  AND humidity.time = toptime.maxtime;'

	cur.execute(sqlCurrent)
	current = cur.fetchall()

	cur.execute(sqlTemp)
	temp = cur.fetchall()

	cur.execute(sqlHumidity)
	humidity = cur.fetchall()
	print temp 
	print temp[0][0]
	return temp,current,humidity 

