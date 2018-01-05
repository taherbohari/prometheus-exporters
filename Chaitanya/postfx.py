import os
from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys

class CustomCollector(object):
	def collect(self):
		print 'Go to localhost'
		total_mails=os.popen("pqshell --summary |awk '/Total mails in queue:/ {print $5}'").readline().strip()
		metric = Metric('total_mails','Number Of mails in the queue','summary')
		metric.add_sample('total_mails',value=float(total_mails),labels={})
		yield metric

		total_size=os.popen("pqshell --summary |awk '/Total queue size:/ {print $4}'").readline().strip()
		metric = Metric('total_queue_size','Size Of the queue','summary')
		metric.add_sample('total_queue_size',value=float(total_size),labels={})
		yield metric


		actv=os.popen("pqshell --summary |awk '/Active/ {print $2}'").readline().strip()
		metric = Metric('active_mails','Number of mails with active status','summary')
		metric.add_sample('active_mails',value=float(actv),labels={})
		yield metric

		defered=os.popen("pqshell --summary |awk '/Deferred/ {print $2}'").readline().strip()
		metric = Metric('defered_mails','Number of mails with defered status','summary')
		metric.add_sample('defered_mails',value=float(defered),labels={})
		yield metric

if __name__ == '__main__':
	# pass port number as argument
	start_http_server(int(sys.argv[1]))
	REGISTRY.register(CustomCollector())
	obj=CustomCollector()
	while True:
		obj.collect()
