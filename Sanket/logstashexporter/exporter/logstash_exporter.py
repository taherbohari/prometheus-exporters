#!/usr/bin/python

from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys, os
import json
import requests
import argparse
from logstashexporter.commands import v545
from pprint import pprint 

LOGSTASH_PORT = 9600
EXPORTER_PORT = 9011

class LogStash(object):
    def collect(self):
        ''' collect logstash metrices '''
        print 'Go to localhost:9011'
        
        #Metric for jvm stats
    	try:
            jvm_stat = json.loads(requests.get('http://localhost:9600/_node/stats/jvm').content.decode('utf-8'))

            for metrics in v545.jvm_metrices:                             
                 metric=Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = jvm_stat
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err
             
        #Metric for process stats
    	try:
            process_stat = json.loads(requests.get('http://localhost:9600/_node/stats/process').content.decode('utf-8'))

            for metrics in v545.process_metrices:                             
                 metric=Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = process_stat
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err

        #Metric for pipeline stats
        try:
            pipeline_stat = json.loads(requests.get('http://localhost:9600/_node/stats/pipeline').content.decode('utf-8'))

            for metrics in v545.pipeline_metrices:                             
                 metric=Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = pipeline_stat
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err
              
if __name__ == '__main__':
    # main
    parser = argparse.ArgumentParser(description='Logstash port arguments')
    parser.add_argument('-s', '--service-port', type=int, default = LOGSTASH_PORT)
    parser.add_argument('-e', '--exporter-port', type=int, default = EXPORTER_PORT)
    args = parser.parse_args()

    LOGSTASH_PORT = args.service_port 
    EXPORTER_PORT = args.exporter_port

    start_http_server(EXPORTER_PORT)
    REGISTRY.register(LogStash())
    obj=LogStash()
    while True:
        obj.collect()

