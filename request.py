import requests

def createRequest(value,metric,ID):
	URL= "http://localhost:80/store_metrics"
	_PARAMS = {'value':value,'metric':metric,'ID':ID}
	r = requests.get(url = URL, params = _PARAMS)
	print r
