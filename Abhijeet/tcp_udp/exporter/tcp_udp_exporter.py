#!/usr/bin/python
import sys
import argparse
import subprocess
from prometheus_client import start_http_server, Metric, Summary,REGISTRY
from tcp_udp.commands import tcp_commands

SERVICE_PORT = 27017
EXPORTER_PORT = 9008

class Tcp_UdpExporter(object):
	def collect(self):
		try:
			for metrics in tcp_commands.tcp_udp_metrics:
				metric = Metric(metrics['name'], metrics['description'], 'summary')
				metric.add_sample(metrics['name'], value = float(subprocess.check_output(metrics['command'],stderr = subprocess.STDOUT, shell = True)), labels = {})
				yield metric
		except Exception as err:
			print type(err)
			print err
if __name__ == '__main__':
	try:
		parser=argparse.ArgumentParser(description = 'pass port number')
		parser.add_argument('-s', '--service-port', type = int, default = SERVICE_PORT)
		parser.add_argument('-e', '--exporter-port', type = int, default = EXPORTER_PORT)
		args=parser.parse_args()

		print args.service_port
		print args.exporter_port
		
	
		SERVICE_PORT = args.service_port
		EXPORTER_PORT = args.exporter_port
		

		start_http_server(EXPORTER_PORT)
		REGISTRY.register(Tcp_UdpExporter())
		obj = Tcp_UdpExporter()
		while True:
			obj.collect()
	except Exception as err:
		print type(err)
		print err
