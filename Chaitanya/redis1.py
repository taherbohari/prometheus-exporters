from prometheus_client import start_http_server, Metric, Summary,REGISTRY
import sys
import redis
import os
class CustomCollector(object):
	def collect(self):
		print 'Go to localhost'
		matrices={'connected_slaves':'Total connected slaves',
'instantaneous_ops_per_sec':'Number of commands processed per second',
'keyspace_misses':'Number of failed lookup of keys',
'used_memory':'Amount Of memory used by redis',
'mem_fragmentation_ratio':'Ratio of memory allocated by operating system to memory requested by redis',
'connected_clients':'Number of clients connected to redis server',
'blocked_clients':'Clients blocked while waiting',
'rdb_last_save_time':'Unix timestamp to last save to disk',
'rdb_changes_since_last_save':'Number of changes to database since last dump',
'rejected_connections':'Number of connections rejected due to hitting maxclient limit',
'evicted_keys':'Number Of keys removed due to reaching maxmemory limit',
'keyspace_hits':'Number Of keys in database'}
		r=redis.StrictRedis()
		user1=r.info()
		for name,value in user1.iteritems():
			if name in matrices.keys():
				value1=value
				metric = Metric(name,matrices[name],'summary')
				metric.add_sample(name,value=value1,labels={})
				yield metric
			if name=='keyspace_hits':
				kh=value
			if name=='keyspace_misses':
				km=value
		try:
			hitrate=kh/(kh+km)
		except ZeroDivisionError:
			hitrate=0
		metric=Metric('hit_rate','keyspace_hits/(keyspace_hits+keyspace_misses)','summary')
		metric.add_sample('hit_rate',value=hitrate,labels={})
		yield metric
		
if __name__ == '__main__':
	#pass port number as argument
	start_http_server(int(sys.argv[1]))
	REGISTRY.register(CustomCollector())
	obj=CustomCollector()
	while True:
		obj.collect()
