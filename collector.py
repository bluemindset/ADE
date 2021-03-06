import time
import datetime
import server
import request
import serial
import re
import time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry, Gauge
_CURRENT = "C"
_TEMPERATURE = "T"
_HUMIDITY = "H"
_VOLTAGE = "V"
#Number of Static Nodes
#This list can append according with the gathering nodes 
#that are assigned on the specific router node.
#For this example we use three nodes althought only the
#first is used.
# index = ID 
# 0 = Temperature value
# 1 = Humidity value
# 2 = Current value
# 3 = Timing value 


#Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5);



while True:
        incoming = ser.readline().strip()

        searchID =re.search(r'ID(\d*)',incoming,re.I) 
        searchC = re.search(r'(\d*)'+_CURRENT,incoming,re.I)
        searchT = re.search(r'(\d*)'+_TEMPERATURE,incoming,re.I)
        searchH = re.search(r'(\d*)'+_HUMIDITY,incoming,re.I)
        searchV = re.search(r'(\d*)'+_VOLTAGE,incoming,re.I)
	if searchID is not None:
		ID = int(str(searchID.group(1)))
		print incoming	
                if searchT is not None:
			request.createRequest(int(str(searchT.group(1))),_TEMPERATURE, ID)
                elif searchH is not None:
			request.createRequest(int(str(searchH.group(1))),_HUMIDITY, ID)
                elif searchC is not None:
                	request.createRequest(int(str(searchC.group(1))),_CURRENT, ID)                
		elif searchV is not None:
			request.createRequest(int(str(searchV.group(1))),_VOLTAGE, ID)
	time.sleep(0.5)

#Start the server with the prometheus values 
updateTables.update__(gatherNodes)


 
