import requests

def createRequest(value,metric,ID,time):
	URL= "http://localhost:8000/xbee"
	_PARAMS = {'value':value,'metric':metric,'ID':ID,'time':time}
	r = requests.get(url = URL, params = _PARAMS)
	print r
