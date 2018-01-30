from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
from pymongo import MongoClient
import json
from pprint import pprint


class CustomCollector(object):
	

	def collect(self):
		statuses = {
			
			"collections" : "total number of collections",
			"objects" : "total number of objects",
			"avgObjSize" : "average size of object",
			"dataSize" : "size of the data",
			"storageSize" :"size of the storage",
			"numExtents" : "numextents",
			"indexes" : "number of indexes",
			"indexSize" : "size of index",
			"fileSize" : "size of the file",
			"ok" : "status"

			}

		client = MongoClient('localhost', 27017)
		# Get the sampleDB database
		db = client.test
		user=db.command("dbstats")
		for name,value in user.iteritems():
			if name in statuses.keys():
				value1=value
				metric = Metric(name,statuses[name],'summary')
				metric.add_sample(name,value=float(value1),labels={})
				yield metric
	    
        
if __name__ == '__main__':
	#pass port number as argument
	start_http_server(int(sys.argv[1]))
	REGISTRY.register(CustomCollector())
	obj=CustomCollector()
	while True:
		obj.collect()
