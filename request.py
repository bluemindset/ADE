import requests





def createRequest(gT,gC,gH):
	URL= "http://localhost:8000/metrics"
	_PARAMS = {'gT':gT,'gC':gC,'gH':gH}
	#_PARAMS = {'registry': registry}
	r = requests.get(url = URL, params = _PARAMS)
	print r
