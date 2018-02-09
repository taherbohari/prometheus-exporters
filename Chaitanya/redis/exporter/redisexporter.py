#!/usr/bin/python

from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import subprocess
import sys
import os
import argparse
from redis.commands import v2821

SERVICE_PORT = 6379
EXPORTER_PORT = 9004

class RedisExporter(object):
    def collect(self):
        dict_metrices={}
        try:
            for metrics in v2821.redis_metrices:
                val = subprocess.check_output(metrics['command'], stderr = subprocess.STDOUT, shell = True)
                dict_metrices.update({metrics['name']: val.strip()})
                if  val != '' and  val != None :
                    metric = Metric(metrics['name'], metrics['desc'], metrics['type'])
                    if metrics['data_type'] == 'float':
                        metric.add_sample(metrics['name'], value = float(val.strip()), labels = {})
                    if metrics['data_type'] == 'integer':
                        metric.add_sample(metrics['name'], value = int(val.strip()), labels = {})
                    yield metric
            kh=int(dict_metrices['keyspace_hits'])                           
            km=int(dict_metrices['keyspace_misses'])
            for metrics in v2821.redis_metrices:
                if metrics['name'] not in dict_metrices:
                    print metrics['name']+' is not available'
            try:                       
                val=kh/(kh+km)
            except ZeroDivisionError:
                val=0
            metric = Metric('hit_rate', 'Cache hit rate', 'summary')
            metric.add_sample('hit_rate', value = float(val), labels = {})
            yield metric
        except Exception as err:
            print err

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description = 'Redis Exporter Arguments')
        parser.add_argument('-s','--service-port', type = int, default = SERVICE_PORT)
        parser.add_argument('-e','--exporter-port', type = int, default = EXPORTER_PORT)
        args = parser.parse_args()

        SERVICE_PORT = args.service_port
        EXPORTER_PORT = args.exporter_port
        start_http_server(EXPORTER_PORT)
        REGISTRY.register(RedisExporter())
        obj = RedisExporter()
        while True:
            obj.collect()
    except Exception as err:
        print err
