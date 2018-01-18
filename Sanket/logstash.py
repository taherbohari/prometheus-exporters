from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import os
import json
import requests

class CustomCollector(object):
	def collect(self):
		print 'Go to http://localhost:1235'
		
		#Metric for jvm stats
    		response = json.loads(requests.get('http://localhost:9600/_node/stats/jvm').content.decode('utf-8'))
		
		metric = Metric('threads_count','Count of jvm threads','summary')
		metric.add_sample('threads_count',value=response['jvm']['threads']['count'],labels={})
		yield metric

############################# HEAP
		metric = Metric('threads_peak_count','Peak count of jvm threads','summary')
		metric.add_sample('threads_peak_count',value=response['jvm']['threads']['peak_count'],labels={})
		yield metric

		metric = Metric('mem_heap_used_percent','Used heap memory percentage','summary')
		metric.add_sample('mem_heap_used_percent',value=response['jvm']['mem']['heap_used_percent'],labels={})
		yield metric

		metric = Metric('mem_heap_committed_in_bytes','Heap committed in bytes','summary')
		metric.add_sample('mem_heap_committed_in_bytes',value=response['jvm']['mem']['heap_committed_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_heap_max_in_bytes','Max heap size in bytes','summary')
		metric.add_sample('mem_heap_max_in_bytes',value=response['jvm']['mem']['heap_max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_heap_used_in_bytes','Used heap size in bytes','summary')
		metric.add_sample('mem_heap_used_in_bytes',value=response['jvm']['mem']['heap_used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_non_heap_used_in_bytes','Not used heap size in bytes','summary')
		metric.add_sample('mem_non_heap_used_in_bytes',value=response['jvm']['mem']['non_heap_used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_non_heap_committed_in_bytes','Non heap committed in bytes','summary')
		metric.add_sample('mem_non_heap_committed_in_bytes',value=response['jvm']['mem']['non_heap_used_in_bytes'],labels={})
		yield metric

############################# SURVIVOR 
		metric = Metric('mem_pools_survivor_peak_used_in_bytes','Peak memory used by survivor pools in bytes','summary')
		metric.add_sample('mem_pools_survivor_peak_used_in_bytes',value=response['jvm']['mem']['pools']['survivor']['peak_used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_survivor_used_in_bytes','Memory used by survivor pools in bytes','summary')
		metric.add_sample('mem_pools_survivor_used_in_bytes',value=response['jvm']['mem']['pools']['survivor']['used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_survivor_peak_max_in_bytes','Max peak Memory for survivor pools in bytes','summary')
		metric.add_sample('mem_pools_survivor_peak_max_in_bytes',value=response['jvm']['mem']['pools']['survivor']['peak_max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_survivor_max_in_bytes','Total Max memory for survivor pools in bytes','summary')
		metric.add_sample('mem_pools_survivor_max_in_bytes',value=response['jvm']['mem']['pools']['survivor']['max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_survivor_committed_in_bytes','Memory committed by survivor pools in bytes','summary')
		metric.add_sample('mem_pools_survivor_committed_in_bytes',value=response['jvm']['mem']['pools']['survivor']['committed_in_bytes'],labels={})
		yield metric

############################# OLD 
		metric = Metric('mem_pools_old_peak_used_in_bytes','Peak memory used by old pools in bytes','summary')
		metric.add_sample('mem_pools_old_peak_used_in_bytes',value=response['jvm']['mem']['pools']['old']['peak_used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_old_used_in_bytes','Memory used by old pools in bytes','summary')
		metric.add_sample('mem_pools_old_used_in_bytes',value=response['jvm']['mem']['pools']['old']['used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_old_peak_max_in_bytes','Max peak Memory for old pools in bytes','summary')
		metric.add_sample('mem_pools_old_peak_max_in_bytes',value=response['jvm']['mem']['pools']['old']['peak_max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_old_max_in_bytes','Total Max memory for old pools in bytes','summary')
		metric.add_sample('mem_pools_old_max_in_bytes',value=response['jvm']['mem']['pools']['old']['max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_old_committed_in_bytes','Memory committed by old pools in bytes','summary')
		metric.add_sample('mem_pools_old_committed_in_bytes',value=response['jvm']['mem']['pools']['old']['committed_in_bytes'],labels={})
		yield metric

############################# YOUNG   
		metric = Metric('mem_pools_young_peak_used_in_bytes','Peak memory used by young pools in bytes','summary')
		metric.add_sample('mem_pools_young_peak_used_in_bytes',value=response['jvm']['mem']['pools']['young']['peak_used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_young_used_in_bytes','Memory used by young pools in bytes','summary')
		metric.add_sample('mem_pools_young_used_in_bytes',value=response['jvm']['mem']['pools']['young']['used_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_young_peak_max_in_bytes','Max peak Memory for young pools in bytes','summary')
		metric.add_sample('mem_pools_young_peak_max_in_bytes',value=response['jvm']['mem']['pools']['young']['peak_max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_young_max_in_bytes','Total Max memory for young pools in bytes','summary')
		metric.add_sample('mem_pools_young_max_in_bytes',value=response['jvm']['mem']['pools']['young']['max_in_bytes'],labels={})
		yield metric

		metric = Metric('mem_pools_young_committed_in_bytes','Memory committed by young pools in bytes','summary')
		metric.add_sample('mem_pools_young_committed_in_bytes',value=response['jvm']['mem']['pools']['young']['committed_in_bytes'],labels={})
		yield metric

########################## GARBAGE COLLECTION

		metric = Metric('gc_collectors_old_collection_count','Total count of old generation garbage collections','summary')
		metric.add_sample('gc_collectors_old_collection_count',value=response['jvm']['gc']['collectors']['old']['collection_count'],labels={})
		yield metric

		metric = Metric('gc_collectors_old_collection_time_in_millis','Time spent on old generation garbage collections','summary')
		metric.add_sample('gc_collectors_old_collection_time_in_millis',value=response['jvm']['gc']['collectors']['old']['collection_time_in_millis'],labels={})
		yield metric

		metric = Metric('gc_collectors_young_collection_count','Total count of young generation garbage collections','summary')
		metric.add_sample('gc_collectors_young_collection_count',value=response['jvm']['gc']['collectors']['young']['collection_count'],labels={})
		yield metric

		metric = Metric('gc_collectors_young_collection_time_in_millis','Time spent on young generation garbage collections','summary')
		metric.add_sample('gc_collectors_young_collection_time_in_millis',value=response['jvm']['gc']['collectors']['young']['collection_time_in_millis'],labels={})
		yield metric

############################ JVM UPTIME
		metric = Metric('jvm_uptime_in_millis','Total running time of jvm in millis','summary')
		metric.add_sample('jvm_uptime_in_millis',value=response['jvm']['uptime_in_millis'],labels={})
		yield metric


		#Metric for Process stats
    		response = json.loads(requests.get('http://localhost:9600/_node/stats/process').content.decode('utf-8'))
		metric = Metric('process_open_file_descriptors','Number of open file discriptors','summary')
		metric.add_sample('process_open_file_descriptors',value=response['process']['open_file_descriptors'],labels={})
		yield metric

		metric = Metric('process_peak_open_file_descriptors','Number of peak open file discriptors','summary')
		metric.add_sample('process_peak_open_file_descriptors',value=response['process']['peak_open_file_descriptors'],labels={})
		yield metric

		metric = Metric('process_max_file_descriptors','Number of max file discriptors','summary')
		metric.add_sample('process_max_file_descriptors',value=response['process']['max_file_descriptors'],labels={})
		yield metric

		metric = Metric('process_mem_total_virtual_in_bytes','Total virtual memory in bytes','summary')
		metric.add_sample('process_mem_total_virtual_in_bytes',value=response['process']['mem']['total_virtual_in_bytes'],labels={})
		yield metric

		metric = Metric('process_cpu_total_in_millis','Total running time of cpu','summary')
		metric.add_sample('process_cpu_total_in_millis',value=response['process']['cpu']['total_in_millis'],labels={})
		yield metric

		metric = Metric('process_cpu_percent','Percentage of cpu used','summary')
		metric.add_sample('process_cpu_percent',value=response['process']['cpu']['percent'],labels={})
		yield metric

		#Metrics for pipeline stats
		response = json.loads(requests.get('http://localhost:9600/_node/stats/pipeline').content.decode('utf-8'))
		metric = Metric('pipeline_events_duration_in_millis','Total event duration in millis','summary')
		metric.add_sample('pipeline_events_duration_in_millis',value=response['pipeline']['events']['duration_in_millis'],labels={})
		yield metric

		metric = Metric('pipeline_events_in','Number of event in','summary')
		metric.add_sample('pipeline_events_in',value=response['pipeline']['events']['in'],labels={})
		yield metric

		metric = Metric('pipeline_events_out','Number of event out','summary')
		metric.add_sample('pipeline_events_out',value=response['pipeline']['events']['out'],labels={})
		yield metric

		metric = Metric('pipeline_events_filtered','Number of event filtered','summary')
		metric.add_sample('pipeline_events_filtered',value=response['pipeline']['events']['filtered'],labels={})
		yield metric

		metric = Metric('pipeline_events_queue_push_duration_in_millis','Time taken to push events in queue in millis','summary')
		metric.add_sample('pipeline_events_queue_push_duration_in_millis',value=response['pipeline']['events']['queue_push_duration_in_millis'],labels={})
		yield metric

		#Metrics for reload stats
		response = json.loads(requests.get('http://localhost:9600/_node/stats/pipeline').content.decode('utf-8'))
		metric = Metric('pipeline_reloads_successes','Number of config reload successes','summary')
		metric.add_sample('pipeline_reload_successes',value=response['pipeline']['reloads']['successes'],labels={})
		yield metric

		metric = Metric('pipeline_reloads_failures','Number of config reload failures','summary')
		metric.add_sample('pipeline_reloads_failures',value=response['pipeline']['reloads']['failures'],labels={})
		yield metric



if __name__ == '__main__':
	# pass port number as argument
    start_http_server(1235)
    REGISTRY.register(CustomCollector())
    obj=CustomCollector()
    while True:
    	obj.collect()

