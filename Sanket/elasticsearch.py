from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import os
import json
import requests
from pprint import pprint

class CustomCollector(object):
	def collect(self):
		print 'Go to http://localhost:1234'
		
		#Metric for cluster health
    		response = json.loads(requests.get('http://localhost:9200/_cluster/health').content.decode('utf-8'))
		
		metric = Metric('number_of_nodes','Number of nodes','summary')
		metric.add_sample('number_of_nodes',value=response['number_of_nodes'],labels={})
		yield metric

		metric = Metric('number_of_data_nodes','Number of data nodes','summary')
		metric.add_sample('number_of_data_nodes',value=response['number_of_data_nodes'],labels={})
		yield metric

		metric = Metric('active_primary_shards','Number of active primary shards','summary')
		metric.add_sample('active_primary_shards',value=response['active_primary_shards'],labels={})
		yield metric

		metric = Metric('active_shards','Number of active shards','summary')
		metric.add_sample('active_shards',value=response['active_shards'],labels={})
		yield metric

		metric = Metric('relocating_shards','Number of relocating shards','summary')
		metric.add_sample('relocating_shards',value=response['relocating_shards'],labels={})
		yield metric

		metric = Metric('initializing_shards','Number of initializing shards','summary')		
		metric.add_sample('initializing_shards',value=response['initializing_shards'],labels={})
		yield metric

		metric = Metric('unassigned_shards','Number of unassigned shards','summary')
		metric.add_sample('unassigned_shards',value=response['unassigned_shards'],labels={})
		yield metric
		
		metric = Metric('delayed_unassigned_shards','Number of delayed unassigned shards','summary')
		metric.add_sample('delayed_unassigned_shards',value=response['delayed_unassigned_shards'],labels={})
		yield metric

		metric = Metric('number_of_pending_tasks','Number of pending tasks','summary')
		metric.add_sample('number_of_pending_tasks',value=response['number_of_pending_tasks'],labels={})
		yield metric
	
		metric = Metric('number_of_in_flight_fetch','Number of in flight fetch','summary')
		metric.add_sample('number_of_in_flight_fetch',value=response['number_of_in_flight_fetch'],labels={})
		yield metric

		metric = Metric('task_max_waiting_in_queue_millis','Task max waiting in queue in milli seconds','summary')
		metric.add_sample('task_max_waiting_in_queue_millis',value=response['task_max_waiting_in_queue_millis'],labels={})
		yield metric

		metric = Metric('active_shards_percent_as_number','Percentage of active shards','summary')
		metric.add_sample('active_shards_percent_as_number',value=response['active_shards_percent_as_number'],labels={})
		yield metric

		#metric for cluster stat
		response = json.loads(requests.get('http://localhost:9200/_cluster/stats?pretty').content.decode('utf-8'))	
		
		print response['indices']['shards']['total']

		metric = Metric('indices_count','Number of indices','summary')
		metric.add_sample('indices_count',value=response['indices']['count'],labels={})
		yield metric

		metric = Metric('indices_docs_count','Total number of documents','summary')
		metric.add_sample('indices_docs_count',value=response['indices']['docs']['count'],labels={})
		yield metric

		metric = Metric('indices_docs_deleted','Number of documents deleted','summary')
		metric.add_sample('indices_docs_deleted',value=response['indices']['docs']['deleted'],labels={})
		yield metric

		metric = Metric('indices_store_size_bytes','Total size aqupied by indices in bytes','summary')
		metric.add_sample('indices_store_size_bytes',value=response['indices']['store']['size_in_bytes'],labels={})
		yield metric

		metric = Metric('indices_fielddata_memory_size_in_bytes','Fielddata memory size in bytes','summary')
		metric.add_sample('indices_fielddata_memory_size_in_bytes',value=response['indices']['fielddata']['memory_size_in_bytes'],labels={})
		yield metric

		metric = Metric('nodes_count_total','Number of nodes','summary')
		metric.add_sample('nodes_count_total',value=response['nodes']['count']['total'],labels={})
		yield metric	

		metric = Metric('nodes_count_master_only','Number of master only nodes','summary')
		metric.add_sample('nodes_count_master_only',value=response['nodes']['count']['master_only'],labels={})
		yield metric

		metric = Metric('nodes_count_data_only','Number of data only nodes','summary')
		metric.add_sample('nodes_count_data_only',value=response['nodes']['count']['data_only'],labels={})
		yield metric

		metric = Metric('nodes_count_master_data','Number of master data nodes','summary')
		metric.add_sample('nodes_count_master_data',value=response['nodes']['count']['master_data'],labels={})
		yield metric

		metric = Metric('nodes_count_client','Number of clients','summary')
		metric.add_sample('nodes_count_client',value=response['nodes']['count']['client'],labels={})
		yield metric

		#metric for search performnace
		response = json.loads(requests.get('http://localhost:9200/bank/_stats?pretty=true').content.decode('utf-8'))	
		
		print response['_all']['primaries']['search']['fetch_time_in_millis']

		metric = Metric('search_query_total','Number of queries','summary')
		metric.add_sample('search_query_total',value=response['_all']['primaries']['search']['query_total'],labels={})
		yield metric

		metric = Metric('search_query_time_in_milis','Total time spent on queries','summary')
		metric.add_sample('search_query_time_in_milis',value=response['_all']['primaries']['search']['query_time_in_millis'],labels={})
		yield metric

		metric = Metric('search_query_current','Number of queries currently in progress','summary')
		metric.add_sample('search_query_current',value=response['_all']['primaries']['search']['query_current'],labels={})
		yield metric

		metric = Metric('search_fetch_total','Number of fetches','summary')
		metric.add_sample('search_fetch_total',value=response['_all']['primaries']['search']['fetch_total'],labels={})
		yield metric

		metric = Metric('search_fetch_time_in_milis','Total time spent on fetches','summary')
		metric.add_sample('search_fetch_time_in_milis',value=response['_all']['primaries']['search']['fetch_time_in_millis'],labels={})
		yield metric

		metric = Metric('search_fetch_current','Number of fetches currently in progress','summary')
		metric.add_sample('search_fetch_current',value=response['_all']['primaries']['search']['fetch_current'],labels={})
		yield metric

		'''metric = Metric('query_latency','Number of queries vs time spent on queries','summary')
		metric.add_sample('query_latency',value=response['_all']['primaries']['search']['query_total']/response['_all']['primaries']['search']['query_time_in_millis'],labels={})
		yield metric'''

		#metrics for index performance
		metric = Metric('indexed_docs_count','Number of documents indexed','summary')
		metric.add_sample('indexed_docs_count',value=response['_all']['primaries']['indexing']['index_total'],labels={})
		yield metric

		metric = Metric('index_time_in_millis','Time spent indexing documents','summary')
		metric.add_sample('index_time_in_millis',value=response['_all']['primaries']['indexing']['index_time_in_millis'],labels={})
		yield metric
		
		metric = Metric('index_current','Documents currently being indexed','summary')
		metric.add_sample('index_current',value=response['_all']['primaries']['indexing']['index_current'],labels={})
		yield metric

		metric = Metric('refresh_total','Number of index refreshes','summary')
		metric.add_sample('refresh_total',value=response['_all']['primaries']['refresh']['total'],labels={})
		yield metric
		
		metric = Metric('refresh_total_time_in_millis','Time spent refreshing indices','summary')
		metric.add_sample('refresh_total_time_in_millis',value=response['_all']['primaries']['refresh']['total_time_in_millis'],labels={})
		yield metric

		metric = Metric('flush_total','Number of index flushes to disk','summary')
		metric.add_sample('flush_total',value=response['_all']['primaries']['flush']['total'],labels={})
		yield metric

		metric = Metric('flush_total_time_in_millis','Time spent flushing indices','summary')
		metric.add_sample('flush_total_time_in_millis',value=response['_all']['primaries']['flush']['total_time_in_millis'],labels={})
		yield metric

		#Garbage collection metrics 
		'''response = json.loads(requests.get('http://localhost:9200/_nodes/_all/stats/jvm?pretty').content.decode('utf-8'))	
		metric = Metric('gc_collectors_young_collection_count','Count of young-generation garbage collections','summary')
		metric.add_sample('gc_collectors_young_collection_count',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['gc']['collectors']['young']['collection_count'],labels={})
		yield metric

		metric = Metric('gc_collectors_young_collection_time_in_millis','Time spent on young-generation garbage collections','summary')
		metric.add_sample('gc_collectors_young_collection_time_in_millis',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['gc']['collectors']['young']['collection_time_in_millis'],labels={})
		yield metric

		metric = Metric('gc_collectors_old_collection_count','Count of old-generation garbage collections','summary')
		metric.add_sample('gc_collectors_old_collection_count',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['gc']['collectors']['old']['collection_count'],labels={})
		yield metric

		metric = Metric('gc_collectors_old_collection_time_in_millis','Time spent on old-generation garbage collections','summary')
		metric.add_sample('gc_collectors_old_collection_time_in_millis',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['gc']['collectors']['old']['collection_time_in_millis'],labels={})
		yield metric

		metric = Metric('jvm_mem_heap_used_in_bytes','Percent of JVM heap currently in use','summary')
		metric.add_sample('jvm_mem_heap_used_in_bytes',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['mem']['heap_used_in_bytes'],labels={})
		yield metric

		metric = Metric('jvm_mem_heap_committed_in_bytes','Amount of JVM heap committed ','summary')
		metric.add_sample('jvm_mem_heap_committed_in_bytes',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['mem']['heap_committed_in_bytes'],labels={})
		yield metric

		metric = Metric('jvm_mem_heap_committed_in_bytes','Amount of JVM heap committed ','summary')
		metric.add_sample('jvm_mem_heap_committed_in_bytes',value=response['nodes']['o8oEi4i3TnGGhuUJXaUFxg']['jvm']['mem']['heap_committed_in_bytes'],labels={})
		yield metric'''

if __name__ == '__main__':
	# pass port number as argument
    start_http_server(1234)
    REGISTRY.register(CustomCollector())
    obj=CustomCollector()
    while True:
    	obj.collect()

