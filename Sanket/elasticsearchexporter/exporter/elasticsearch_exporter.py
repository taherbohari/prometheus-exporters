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
ELASTICSEARCH_PORT = 9200
HOST_IP = '127.0.0.1'

esObject = elasticsearch.Elasticsearch(host=HOST_IP, port=ELASTICSEARCH_PORT)

class ElasticSearch(object):

    def collect(self):
        ''' collect elasticsearch metrices '''
        print 'Go to localhost:9010'
        #Get Cluster health metrices
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

        #Get Cluster stats metrices
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

        #Get Indices stats metrices
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
        
        #Get stats for Node
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
        
        # Get Cat API stats
        cat = elasticsearch.client.CatClient(esObject)
        cat_stats = cat.allocation()
        #pprint(cat_stats)
        for metrics in v545.cat_metrices:                             
             metric = Metric(metrics['name'],metrics['description'],metrics['type'])
             metric.add_sample(metrics['name'],value=float(cat_stats.split(" ")[metrics['param']].rstrip('gb')),labels={})
             yield metric
              
if __name__ == '__main__':
    # main
    parser = argparse.ArgumentParser(description='Elasticsearch port arguments')
    parser.add_argument('-s', '--service-port', type=int, default = ELASTICSEARCH_PORT)
    parser.add_argument('-e', '--exporter-port', type=int, default = EXPORTER_PORT)
    args = parser.parse_args()

    ELASTICSEARCH_PORT = args.service_port 
    EXPORTER_PORT = args.exporter_port

    start_http_server(EXPORTER_PORT)
    REGISTRY.register(ElasticSearch())
    obj=ElasticSearch()
    while True:
        obj.collect()

