from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import os

class CustomCollector(object):
	def collect(self):
		print 'Go to localhost'
		user=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $3}'").readline().strip()
		nice1=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $4}'").readline().strip()
		#syst=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $5}'").readline().strip()
		#iowait=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $6}'").readline().strip()
		irq=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $7}'").readline().strip()
		idle1=os.popen("mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[a-z]/ {print $12}'").readline().strip()
		
		metric = Metric('Utilization_at_user_level','Percentage of utilization at user level','summary')
		metric.add_sample('Utilization_at_user_level',value=user,labels={})
		yield metric
		
		metric = Metric('Utilization_at_user_level_nicepriority','Percentage of utilization at user level with nice priority','summary')
		metric.add_sample('Utilization_at_user_level_nicepriority',value=nice1,labels={})
		yield metric
		
		#metric = Metric('Utilization_at_kernel_level','Percentage of utilization at user level','summary')
		#metric.add_sample('Utilization_at_kernel_level',value=syst,labels={})
		#yield metric
		
		metric = Metric('time_when_cpu_idle','Time for which Cpu was idle','summary')
		metric.add_sample('time_when_cpu_idle',value=idle1,labels={})
		yield metric
		
		
	
if __name__ == '__main__':
	# pass port number as argument
	start_http_server(int(sys.argv[1]))
	REGISTRY.register(CustomCollector())
	obj=CustomCollector()
	while True:
		obj.collect()
