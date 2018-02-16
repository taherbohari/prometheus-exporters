#!/usr/bin/python

from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys, os
import json
import requests
import argparse
import elasticsearch
from elasticsearchexporter.commands import v545
from pprint import pprint 

EXPORTER_PORT = 9010

HOST_IP = '127.0.0.1'
ELASTICSEARCH_PORT = 9200

class ElasticSearch(object):

    def collect(self):
        ''' collect elasticsearch metrices '''
        print 'Go to '+HOST_IP+':'+str(EXPORTER_PORT)
        #Get Cluster health metrices
        try:
            cc = elasticsearch.client.ClusterClient(esObject)
            cc_health = cc.health()
            #pprint(cc_health) 
            for metrics in v545.cluster_health_metrices:                             
                 metric = Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = cc_health
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err

        #Get Cluster stats metrices
        try:
            cc = elasticsearch.client.ClusterClient(esObject)
            cc_stats = cc.stats()
            #pprint(cc_stats) 
            for metrics in v545.cluster_stats_metrices:                             
                 metric = Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = cc_stats
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err

        #Get Indices stats metrices
        try:
            ic = elasticsearch.client.IndicesClient(esObject)                             
            ic_stats = ic.stats()
            for metrics in v545.index_stats_metrices:                             
                 metric=Metric(metrics['name'],metrics['description'],metrics['type'])
                 temp = ic_stats
                 param = metrics['param']   
                 for index in range(len(metrics['param'])):
                     temp = temp[param[index]]
                    
                 metric.add_sample(metrics['name'],value=temp,labels={})
                 yield metric
        except Exception as err:
            print err
         
        #Get stats for Node
        try:
            nc = elasticsearch.client.NodesClient(esObject)
            nc_stats = nc.stats()
            for nodeID, node_stats in nc_stats['nodes'].iteritems():
                #pprint(node_stats)
                for metrics in v545.node_stats_metrices:                             
                    metric = Metric(metrics['name'],metrics['description'],metrics['type'])
                    temp = node_stats
                    param = metrics['param']   
                    for index in range(len(metrics['param'])):
                        temp = temp[param[index]]
                    
                    metric.add_sample(metrics['name'],value=temp,labels={})
                    yield metric
        except Exception as err:
            print err
             
        # Get Cat API stats
        try:
            cat = elasticsearch.client.CatClient(esObject)
            cat_stats = cat.allocation()
            #pprint(cat_stats)
            for metrics in v545.cat_metrices:                             
                 metric = Metric(metrics['name'],metrics['description'],metrics['type'])
                 metric.add_sample(metrics['name'],value=float(cat_stats.split(" ")[metrics['param']].rstrip('gb')),labels={})
                 yield metric
        except Exception as err:
            print err
             
if __name__ == '__main__':
    # main
    try:
        parser = argparse.ArgumentParser(description='Elasticsearch port arguments')
        parser.add_argument('-i', '--host-ip', type=str, default = HOST_IP)
        parser.add_argument('-e', '--elasticsearch-port',type=int, default = ELASTICSEARCH_PORT)
        args = parser.parse_args()

        HOST_IP = args.host_ip 
        ELASTICSEARCH_PORT = args.elasticsearch_port

        esObject = elasticsearch.Elasticsearch(host=HOST_IP, port=ELASTICSEARCH_PORT)

        start_http_server(EXPORTER_PORT)
        REGISTRY.register(ElasticSearch())
        obj=ElasticSearch()
        while True:
            obj.collect()
    except Exception as err:
        print err
