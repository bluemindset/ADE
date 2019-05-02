from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry, Gauge
from pyramid.view import view_config
import insert


def fetch_mysql

def __initRegistry():
	registry = CollectorRegistry()
	id,temperature,humidity,current = fetch_mysql()
	gT = Gauge("Temperature", "Temperature Of Solar Panel0", registry=registry)
	gC = Gauge("Current0", "Current Of Solar Panel0", registry=registry)
	gH = Gauge("Humidity0", "Temperature Of Solar Panel0", registry=registry)
	return registry , gT,gC,gH

def prometheus_values(t,c,h,ID):    
    strID = str(ID)
    gT.set(t)
    gC.set(c)

@view_config(
	route_name = "expose"	
)
def expose_metrics(request):
	registry = __initRegistry()
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
                print request.params['time']
		metric =  request.params['metric']
      	        value =  int(request.params['value'])
		ID = int(request.params['ID'])
        	time =  request.params['time']
		insert.insert(value,metric,ID,time)
		return Response(body = "Stored to database",
                    content_type=CONTENT_TYPE_LATEST)
	else:
		return Response(body = "Not stored to database")

def config():
	config = Configurator()
	config.add_route('metrics','/expose_metrics')
	config.add_route('store','/store_metrics')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('127.0.0.1', 8000, app)
	return server

def serve():
	config().serve_forever()

