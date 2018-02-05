#!/usr/bin/python
from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import subprocess
import sys
import os
import argparse
from postfix.commands import v2113

SERVICE_PORT = 25
EXPORTER_PORT = 9004

class RedisExporter(object):
    def collect(self):
        print 'Go to http://localhost/'
        for metrics in v2113.postfix_metrices:
            val = subprocess.check_output(metrics['command'],stderr=subprocess.STDOUT,shell=True)
            if val!='':
                metric = Metric(metrics['name'],metrics['desc'],'summary')
                if metrics['data_type'] == 'float':
                    metric.add_sample(metrics['name'],value=float(val.strip()),labels={})
                if metrics['data_type'] == 'integer':
                    metric.add_sample(metrics['name'],value=int(val.strip()),labels={})
                yield metric

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Redis Exporter Arguments')
    parser.add_argument('-s','--service-port', type=int, default=SERVICE_PORT)
    parser.add_argument('-e','--exporter-port', type=int, default=EXPORTER_PORT)
    args=parser.parse_args()

    SERVICE_PORT = args.service_port
    EXPORTER_PORT = args.exporter_port
    start_http_server(EXPORTER_PORT)
    REGISTRY.register(RedisExporter())
    obj = RedisExporter()
    while True:
        obj.collect()




