#!/usr/bin/python
from prometheus_client import start_http_server, Metric, Summary, REGISTRY
import sys, os
import argparse

SERVICE = 'all'
EXPORTER_PORT = 9012

class SuperVisor(object):
    def __init__(self, endpoint):
        self._endpoint = endpoint

    def collect(self):
        print 'Go to localhost:9012'
        SERVICE=self._endpoint

############################## supervisor part ############################
        n = int(os.popen('sudo supervisorctl status all | wc -l').readlines()[0])

        metric = Metric('supervisord_total_services', 'Total number of services in supervisor','summary')
        metric.add_sample('supervisord_total_services', value=n, labels={})
        yield metric

        #print 'total_services '+str(n)
        stopped = 0
        running = 0
        
        for i in range(0,n):
            name,status = map(str, os.popen('sudo supervisorctl status all').readlines()[i].split()[0:2])
            if status == 'STOPPED':
	            stopped = stopped+1
            else :
                flag=1
                running = running+1
            #print  name + '_running_status '+ str(flag)
            metric = Metric(name+'_running_status', 'Running status of service','summary')
            metric.add_sample(name+'_running_status', value=flag, labels={})
            yield metric
        
        #print "total_running_services: " + str(r)
        metric = Metric('supervisord_running_services', 'Total number of running services','summary')
        metric.add_sample('supervisord_running_services', value=running, labels={})
        yield metric
        
        #print "total_stopped_services: " + str(s)
        metric = Metric('supervisord_stopped_services', 'Total number of stopped services','summary')
        metric.add_sample('supervisord_stopped_services', value=stopped, labels={})
        yield metric
		
################################## system services part #############################

        if SERVICE!='all':
            loaded_status = (os.popen('service '+SERVICE+' status').readlines()[1]).strip()[8:14]
            #print loaded_status
            if loaded_status=='loaded':
                lflag=1
            else:
                lflag=0
 
            metric = Metric(SERVICE+'_exists_status', 'Service exists(1) or not(0)','summary')
            metric.add_sample(SERVICE+'_exists_status', value=lflag, labels={})
            yield metric

            active_status = (os.popen('service '+SERVICE+' status').readlines()[2]).strip()[8:24]
            #print active_status
            if active_status=='active (running)':
                rflag=1
            else:
                rflag=0

            metric = Metric(SERVICE+'_running_status', 'Service running(1) or dead(0)','summary')
            metric.add_sample(SERVICE+'_running_status', value=rflag, labels={})
            yield metric

if __name__ == '__main__':
    # main
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument('service', nargs='?', const=1, type=str, default=SERVICE)
    args = parser.parse_args()
    SERVICE=args.service
    try:
        start_http_server(EXPORTER_PORT)
    except:
        print 'Error in exporter port'

    REGISTRY.register(SuperVisor(SERVICE))
    obj=SuperVisor(SERVICE)
    while True:
        obj.collect()
