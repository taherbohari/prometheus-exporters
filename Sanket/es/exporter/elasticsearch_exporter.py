#!/usr/bin/python

from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys, os
import json
import requests
import argparse
import elasticsearch
from es.commands import v545

service_port=20
exporte_port=10

elasticsearch_port = 9200
host_ip = '127.0.0.1'
es = elasticsearch.Elasticsearch(host=host_ip, port=elasticsearch_port)


		
class ElasticSearch1(object):
    def collect(self):
	print 'hello' + str(service_port)
        ic = elasticsearch.client.IndicesClient(es)
        ic_stats = ic.stats()
	docs_count = ic_stats['_all']['total']['docs']['count']
	print docs_count

	docs_deleted = ic_stats['_all']['total']['docs']['deleted']
	print docs_deleted	
		
        for metrics in v545.elasticsearch_metrices:
            metric = Metric('number_of_nodes','Number of nodes','summary')
            metric.add_sample(metrics['name'],value=float(metrics['command']),labels={})
            yield metric
			#print metrics['name'],metrics['command']
			

if __name__ == '__main__':
    # pass port number as argument
    parser = argparse.ArgumentParser(description='Pass port numbers')
    parser.add_argument('-s', '--service-port', type=int, default=9200)
    parser.add_argument('-e', '--exporter-port', type=int, default=1234)
    args = parser.parse_args()

    print 'main'
    print args.service_port
    print args.exporter_port

    service_port=args.service_port 
    exporter_port=args.exporter_port

    start_http_server(exporter_port)
    REGISTRY.register(ElasticSearch1())
    obj=ElasticSearch1()
    while True:
        obj.collect()

