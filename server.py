from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry, Gauge
from pyramid.view import view_config
import insert
import database
import selectQ

def fetch_mysql():
	conn = database.createConn()
        cur = conn.cursor()
	sql = "SELECT * FROM WHERE "
	cur.execute(sql)

def __initRegistry(T,C,H):
	registry = CollectorRegistry()
	for temps in T:
		gT = Gauge("RealT"+str(temps[0]), "Temperature Of Solar Panel", registry=registry)
	#gC = Gauge("Current", "Current Of Solar Panel0", registry=registry)
	#gH = Gauge("Humidity", "Temperature Of Solar Panel0", registry=registry)
		gT.set(temps[1])
	#gC.set(C)
	#gH.set(H)
	return registry 

def prometheus_values(t,c,h,ID):    
    strID = str(ID)
    gT.set(t)
    gC.set(c)

@view_config(
	route_name = "expose"	
)
def expose_metrics(request):
	T,C,H = selectQ.select()
	print T
	registry = __initRegistry(T,C,H)
	return Response(generate_latest(registry),
                    content_type=CONTENT_TYPE_LATEST)

@view_config(
        route_name = 'store'
)
def store_metrics(request):
	if 'metric' in request.params and 'value' in request.params and 'ID' in request.params:
		print request.params['metric']
		print request.params['value']
		print request.params['ID']
		metric =  request.params['metric']
      	        value =  int(request.params['value'])
		ID = int(request.params['ID'])
		insert.insert(value,metric,ID)
		return Response(body = "Stored to database",
                    content_type=CONTENT_TYPE_LATEST)
	else:
		print "NO"
		return Response(body = "Not stored to database")

	return Response(status="OK")
def config():
	config = Configurator()
	config.add_route('expose','/expose_metrics')
	config.add_route('store','/store_metrics')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('127.0.0.1', 8000, app)
	return server

def serve():
	config().serve_forever()

