#!/usr/bin/python
from prometheus_client import start_http_server, Metric, Summary, REGISTRY
import sys, os
import argparse
import commands

'''
ubuntu 14.04
root@BE-Project-Exporters:/home/ubuntu# service elasticsearch status
 * elasticsearch is running
root@BE-Project-Exporters:/home/ubuntu# 
root@BE-Project-Exporters:/home/ubuntu# service logstash status
logstash: unrecognized service
root@BE-Project-Exporters:/home/ubuntu# 
'''

SERVICE = 'all'
EXPORTER_PORT = 9012

class SuperVisor(object):
    def __init__(self, endpoint):
        self._endpoint = endpoint

    def collect(self):
        print 'Go to localhost:9012'
        
        SERVICE = self._endpoint
        
        ######### Supervisord Services ##########
        supervisor_status = (os.popen('sudo service supervisor status').readlines()[0]).strip()[0:11] 
        print supervisor_status
        if supervisor_status=='is running': 
            n = int(os.popen('sudo supervisorctl status | wc -l').readlines()[0])
        
            metric = Metric('supervisord_total_services', 'Total number of services in supervisor','gauge')
            metric.add_sample('supervisord_total_services', value=n, labels={})
            yield metric
        
            #print 'total_services '+str(n)
            stopped = 0
            running = 0
        
            for i in range(0,n):
                name,status = map(str, os.popen('sudo supervisorctl status').readlines()[i].split()[0:2])
                print name+status
                if status == 'STOPPED':
                    stopped = stopped+1
                else :
                    flag=1
                    running = running+1
                #print  name + '_running_status '+ str(flag)
                metric = Metric(name+'_running_status', 'Running status of service','gauge')
                metric.add_sample(name+'_running_status', value=flag, labels={})
                yield metric
            
            #print "total_running_services: " + str(r)
            metric = Metric('supervisord_running_services', 'Total number of running services','gauge')
            metric.add_sample('supervisord_running_services', value=running, labels={})
            yield metric
            
            #print "total_stopped_services: " + str(s)
            metric = Metric('supervisord_stopped_services', 'Total number of stopped services','gauge')
            metric.add_sample('supervisord_stopped_services', value=stopped, labels={})
            yield metric
            
        ################ system services part 
        os_release = (os.popen('lsb_release -r').readlines()[0]).strip()[9:14]
        
        ######## UBUNTU 14.04 #########
        if os_release=='14.04':
           if SERVICE!='all':
               l=len(SERVICE)
               for i in range(0,l):
                   status, loaded_status = commands.getstatusoutput("sudo service "+SERVICE[i]+" status | awk '{print $3 $4 $5}'")
                   print loaded_status
                   if loaded_status=='loaded':
                       lflag=1
                   else:
                       lflag=0 
                   metric = Metric(SERVICE[i]+'_exists_status', 'Service exists(1) or not(0)','gauge')
                   metric.add_sample(SERVICE[i]+'_exists_status', value=lflag, labels={})
                   yield metric

                   #print active_status
                   if loaded_status=='is running':
                       rflag=1
                   else:
                       rflag=0
                   metric = Metric(SERVICE[i]+'_running_status', 'Service running(1) or dead(0)','gauge')
                   metric.add_sample(SERVICE[i]+'_running_status', value=rflag, labels={})
                   yield metric

        ######## UBUNTU 16.04 #########
        if os_release=='16.04':
            if SERVICE!='all':
                l=len(SERVICE)
                for i in range(0,l):
                    #loaded_status = str(os.popen('service '+SERVICE[i]+' status').readlines()).strip()
                    status, loaded_status = commands.getstatusoutput("sudo service "+SERVICE[i]+" status | awk '/Loaded:/{print $2}'")
                    print loaded_status
                    if loaded_status=='loaded':
                        lflag=1
                    else:
                        lflag=0 
                    metric = Metric(SERVICE[i]+'_exists_status', 'Service exists(1) or not(0)','gauge')
                    metric.add_sample(SERVICE[i]+'_exists_status', value=lflag, labels={})
                    yield metric

                    status, active_status = commands.getstatusoutput("sudo service "+SERVICE[i]+" status | awk '/Active:/{print $2"+'" "'+"$3}'")
                    print active_status
                    if active_status=='active (running)':
                        rflag=1
                    else:
                        rflag=0
                    metric = Metric(SERVICE[i]+'_running_status', 'Service running(1) or dead(0)','gauge')
                    metric.add_sample(SERVICE[i]+'_running_status', value=rflag, labels={})
                    yield metric

if __name__ == '__main__':
    # main
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument('service', nargs='*', type=str, default=SERVICE)
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
