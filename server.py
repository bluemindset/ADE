from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry, Gauge
from pyramid.view import view_config





def __initRegistry():
	registry = CollectorRegistry()
	gT = Gauge("Temperature0", "Temperature Of Solar Panel0", registry=registry)
	gC = Gauge("Current0", "Current Of Solar Panel0", registry=registry)
	gH = Gauge("Humidity0", "Temperature Of Solar Panel0", registry=registry)

	return registry , gT,gC,gH
def prometheus_values(t,c,h,ID):    
    strID = str(ID)
    gT.set(t)
    gC.set(c)

def metrics_web(registry,gT,gC,gH,t,h,c,ID):
    gT.set(t)
    gC.set(c)
    gH.set(h)    
    metrics
    return Response(generate_latest(registry),
                    content_type=CONTENT_TYPE_LATEST)
@view_config(
        route_name = 'metrics'
)
def metrics_(request):
	if 'gT' in request.params:
		registry,gT,gC,gH =__initRegistry()
		gC.set(request.params['gC'])
		gT.set(request.params['gT'])		    
		gH.set(request.params['gH'])
	else:
		registry = CollectorRegistry()
	return Response(generate_latest(registry),
                    content_type=CONTENT_TYPE_LATEST)
#	else:
#		 return Response(body = "no registry found")
def config():
	config = Configurator()
	config.add_route('metrics','/metrics')
#	config.add_view(metrics_, route_name='metrics')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('127.0.0.1', 8000, app)
	return server

def serve():
	config().serve_forever()

