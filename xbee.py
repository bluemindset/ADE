import server
import request
import serial
import re
import time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry, Gauge
import updateTables
_CURRENT = "C"
_TEMPERATURE = "T"
_HUMIDITY = "H"

strc = "8CID0"
strh= "30HID0"
strt ="25TID0"
registry = CollectorRegistry()
gT = Gauge("Temperature0", "Temperature Of Solar Panel0", registry=registry)
gC = Gauge("Current0", "Current Of Solar Panel0", registry=registry)
gH = Gauge("Humidity0", "Temperature Of Solar Panel0", registry=registry)
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

gatherNodes =[[0,0,0,0],[0,0,0,0]]



def clear_line(index):
	for i in range(len(gatherNodes[index])-1):
		gatherNodes[index][i]=0
                       
   
def evaluate_line(index):
	for i in range(len(gatherNodes[index])-1):
		if gatherNodes[index][i]==0:
                        return False
        return True       

#Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5);
while True:
        incoming = ser.readline().strip()
        searchID =re.search(r'ID(\d*)',incoming,re.I) 
        searchC = re.search(r'(\d*)'+_CURRENT,incoming,re.I)
        searchT = re.search(r'(\d*)'+_TEMPERATURE,incoming,re.I)
        searchH = re.search(r'(\d*)'+_HUMIDITY,incoming,re.I)
	print incoming	
	if searchID is not None:
		print searchID.group(1)
        if searchID is not None:
		ID = int(str(searchID.group(1)))
                if searchT is not None:
                        print searchT.group(1)
                        gatherNodes[ID][0]= int(str(searchT.group(1)))
                if searchH is not None:
                        print searchH.group(1)
			gatherNodes[ID][1]= int(str(searchH.group(1)))
                if searchC is not None:
                        gatherNodes[ID][2]= int(str(searchC.group(1)))                
                if evaluate_line(ID):
			gT.set(gatherNodes[ID][0])
			gH.set(gatherNodes[ID][1])
			gC.set(gatherNodes[ID][2])
	                request.createRequest(gatherNodes[ID][0],gatherNodes[ID][1],gatherNodes[ID][2])#        server.metrics_web(registry,gT,gH,gC,gatherNodes[ID][0],gatherNodes[ID][1],gatherNodes[ID][2],str(ID))
                        clear_line(ID)
       # time.sleep(0.5)

#Start the server with the prometheus values 
updateTables.update__(gatherNodes)


 
