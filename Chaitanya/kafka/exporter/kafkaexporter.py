#!/usr/bin/python
from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import subprocess
import commands
import sys
import os
import argparse
from kafka.commands import v100
EXPORTER_PORT = 9006
SERVICE_PORT = 2181

class KafkaExporter(object):
    def collect(self):
        try:
            for metrics in v100.kafka_metrices:
                status, val = commands.getstatusoutput(metrics['command'])
                # if val != '' and val != None:
                #     if metrics['name'] == 'number_of_partitions':
                #        val = val.split('\n')[0]
                #       arr = val.split('\t')
                #      val = arr[1].split(':')[1]
                #   if metrics['name'] == 'number_of_replications':
                #       val = val.split('\n')[0]
                #       arr = val.split('\t')
                #       val = arr[2].split(':')[1]
                metric = Metric(metrics['name'], metrics['desc'], metrics['type'])
                if metrics['data_type'] == 'float':
                    metric.add_sample(metrics['name'], value = float(val), labels = {})
                if metrics['data_type'] == 'integer':
                    metric.add_sample(metrics['name'], value = int(val), labels = {})
                yield metric
        except Exception as err:
            print err

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description = 'Kafka Exporter Arguments')
        parser.add_argument('-s','--service-port', type = int, default = SERVICE_PORT)
        parser.add_argument('-e','--exporter-port', type = int, default = EXPORTER_PORT)
        args = parser.parse_args()

        SERVICE_PORT = args.service_port
        EXPORTER_PORT = args.exporter_port
        start_http_server(EXPORTER_PORT)
        REGISTRY.register(KafkaExporter())
        obj = KafkaExporter()
        while True:
            obj.collect()
    except Exception as err:
        print err
