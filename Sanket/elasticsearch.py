from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import os
import json
import requests
from pprint import pprint

class CustomCollector(object):
	def collect(self):
		print 'Go to localhost'
		
		response = json.loads(requests.get('http://localhost:9200/_cluster/health').content.decode('utf-8'))
		
		pprint (response)
		
		#Convert requests and duration to a summary in seconds
    
		metric = Metric('number_of_nodes','Number of nodes','summary')
		metric.add_sample('total_number_of_nodes',value=response[u'number_of_nodes'],labels={})
		metric.add_sample('total_active_shards',value=response[u'active_shards'],labels={})
		yield metric

	
if __name__ == '__main__':
	# pass port number as argument
    start_http_server(int(sys.argv[1]))
    REGISTRY.register(CustomCollector())
    obj=CustomCollector()
    while True:
    	obj.collect()

