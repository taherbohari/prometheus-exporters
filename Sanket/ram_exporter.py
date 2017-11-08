from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import os

class CustomCollector(object):
	def collect(self):
		print 'Go to localhost'
		tot_m, used_m, free_m= map(int, os.popen('free -t -m').readlines()[1].split()[1:4])
		metric = Metric('total_ram_memory','Total ram memory size in MB','summary')
		metric.add_sample('total_ram_memory',value=tot_m,labels={})
		yield metric
		
		metric = Metric('used_ram_memory','Used ram memory size in MB','summary')
		metric.add_sample('used_ram_memory',value=used_m,labels={})
		yield metric
		
		metric = Metric('free_ram_memory','Free ram memory size in MB','summary')
		metric.add_sample('free_ram_memory',value=free_m,labels={})
		yield metric
	
if __name__ == '__main__':
	# pass port number as argument
    start_http_server(int(sys.argv[1]))
    REGISTRY.register(CustomCollector())
    obj=CustomCollector()
    while True:
    	obj.collect()
  
'''
shivam@shivam-desktop:~/GS$ python ram_exporter.py 8003&
[4] 4290
shivam@shivam-desktop:~/GS$ Go to localhost
Go to localhost
Go to localhost

shivam@shivam-desktop:~/GS$ 



on another terminal


shivam@shivam-desktop:~/GS$ curl http://localhost:8003
# HELP total_ram_memory Total ram memory size in MB
# TYPE total_ram_memory summary
total_ram_memory 1842.0
# HELP used_ram_memory Used ram memory size in MB
# TYPE used_ram_memory summary
used_ram_memory 1415.0
# HELP free_ram_memory Free ram memory size in MB
# TYPE free_ram_memory summary
free_ram_memory 427.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 203382784.0
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 14094336.0
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1510123055.45
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 29.42
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="6",version="2.7.6"} 1.0
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ 
shivam@shivam-desktop:~/GS$ curl http://localhost:8003
# HELP total_ram_memory Total ram memory size in MB
# TYPE total_ram_memory summary
total_ram_memory 1842.0
# HELP used_ram_memory Used ram memory size in MB
# TYPE used_ram_memory summary
used_ram_memory 1418.0
# HELP free_ram_memory Free ram memory size in MB
# TYPE free_ram_memory summary
free_ram_memory 424.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 203382784.0
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 14159872.0
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1510123055.45
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 54.35
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="6",version="2.7.6"} 1.0
shivam@shivam-desktop:~/GS$ 


'''  
    
