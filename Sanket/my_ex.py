#!/usr/bin/python

from prometheus_client import start_http_server, Metric, REGISTRY
import json
import requests
import sys
import time
import os

class JsonCollector(object):
  def __init__(self, endpoint, option):
    self._endpoint = endpoint
    self.option = option

  def collect(self):
    print "came here"
    #arg=requests.get(self._endpoint)

    #if self.option == 'ram':    #statistics of ram
    tot_m, used_m, free_m, s,b,c = map(int, os.popen('free -t -m').readlines()[1].split()[1:])
    print ''
    print 'total ram memory: ',tot_m, 'MB'
    print 'used ram memory: ',used_m, 'MB'
    print 'free ram memory: ',free_m, 'MB'
    print ''

    # Convert requests and duration to a summary in seconds
    metric = Metric('svc_requests_duration_seconds',
        'Requests time taken in seconds', 'summary')
    metric.add_sample('total_ram',
        value=tot_m, labels={})
    metric.add_sample('ram_used',
        value=used_m, labels={})
    yield metric

    # Counter for the failures
    metric = Metric('svc_requests_failed_total',
       'Requests failed', 'summary')
    metric.add_sample('ram_free',
       value=free_m, labels={})
    yield metric


if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2], sys.argv[3]))
  json_collector = JsonCollector(sys.argv[2], sys.argv[3])
  #json_collector.collect()
  while True:
    json_collector.collect()
