#!/usr/bin/python
import sys
import argparse
import subprocess
import json
from pymongo import MongoClient
from prometheus_client import start_http_server, Metric, Summary, REGISTRY
from mongodb.commands import ver3


SERVICE_PORT = 27017
EXPORTER_PORT = 9001
DB_NAME = 'test'

class MongodbExporter(object):
	def __init__(self, db_name):
		self._db_name = db_name

	def collect(self):
		db_name = self._db_name
		client = MongoClient('localhost', 27017)
		# Get the sampleDB database
		db = client.dbname
		result2 = db.command("dbstats")
		result1 = db.command("serverStatus")
	
		try:
			for metrics in ver3.mongodb1:
				temp = result1
				param = metrics['param']
				for index in range(len(metrics['param'])):
					temp = temp[param[index]]
				metric = Metric(metrics['name'], metrics['description'], 'summary')
				if metrics['datatype'] == 'float':
					metric.add_sample(metrics['name'], value = float(temp), labels = {})
				if metrics['datatype'] == 'int':
					metric.add_sample(metrics['name'], value = int(temp), labels = {})
				yield metric

			for metrics in ver3.mongodb2:
				temp = result2
				param = metrics['param']
				for index in range(len(metrics['param'])):
					temp = temp[param[index]]
				metric = Metric(metrics['name'], metrics['description'], 'summary')
				if metrics['datatype'] == 'float':
					metric.add_sample(metrics['name'], value = float(temp), labels = {})
				if metrics['datatype'] == 'int':
					metric.add_sample(metrics['name'], value = int(temp), labels = {})
				yield metric
		except Exception as err:
			print type(err)
			print err

if __name__ == '__main__':
	try:
		parser=argparse.ArgumentParser(description = 'pass port number')
		parser.add_argument('-s', '--service-port', type = int, default = SERVICE_PORT)
		parser.add_argument('-e', '--exporter-port', type = int, default = EXPORTER_PORT)
		parser.add_argument('-d', '--db_name', type = str, default = DB_NAME)
		args=parser.parse_args()

		print args.service_port
		print args.exporter_port
		print args.db_name
	
		SERVICE_PORT = args.service_port
		EXPORTER_PORT = args.exporter_port
		DB_NAME=args.db_name

		start_http_server(EXPORTER_PORT)
		
		REGISTRY.register(MongodbExporter(DB_NAME))
		obj = MongodbExporter(DB_NAME)
		while True:
			obj.collect()
	except Exception as err:
		print type(err)
		print err
