#!/usr/bin/python

redis_metrices = [

    {
	'name': 'connected_clients',
    'command': "redis-cli info | awk -F: '/connected_clients/{print $2}'",
    'desc': 'Total connected clients to redis server',
    'type': 'summary',
	'data_type': 'integer'
    },
    {
	'name': 'connected_slaves',
    'command': "redis-cli info | awk -F: '/connected_slaves/{print $2}'",
    'desc': 'Total number of slaves connected to a master',
    'type': 'summary',
	'data_type': 'integer'
    },
    {
	'name': 'blocked_clients',
	'command': "redis-cli info | awk -F: '/blocked_clients/{print $2}'",
	'desc': 'Total number of blocked clients by redis server',
	'type': 'summary',
	'data_type': 'integer'
    },
    {	
    'name': 'mem_fragmentation_ratio',
	'command': "redis-cli info | awk -F: '/mem_fragmentation_ratio/{print $2}'",
	'desc': 'Ratio of memory allocated by operating system to memory requested by redis',
	'type': 'summary',
	'data_type': 'float'
    },

    {	
    'name': 'instantaneous_ops_per_sec',
	'command': "redis-cli info | awk -F: '/instantaneous_ops_per_sec/{print $2}'",
	'desc': 'Number of commands processed per second',
	'type': 'summary',
	'data_type': 'integer'
    },

    {
    'name': 'keyspace_misses',
	'command': "redis-cli info | awk -F: '/keyspace_misses/{print $2}'",
	'desc': 'number of failed lookups of keys',
	'type': 'summary',
	'data_type': 'integer'
    },

    {
	'name': 'used_memory',
	'command': "redis-cli info | awk -F: '$1 ~ /used_memory$/{print $2}'",
	'desc': 'Amount of memory used by Redis',
	'type': 'summary',
	'data_type': 'integer'
    },
    
    {
    'name': 'rdb_last_save_time',
    'command': "redis-cli info | awk -F: '$1 ~ /rdb_last_save_time$/{print $2}'",
    'desc': 'Unix timestamp to last save to disk',
    'type': 'summary',
    'data_type': 'integer'
    },

    {
    'name': 'rdb_changes_since_last_save',
    'command': "redis-cli info | awk -F: '$1 ~ /rdb_changes_since_last_save$/{print $2}'",
    'desc': 'Number of changes to database since last dump',
    'type': 'summary',
    'data_type': 'integer'
    },

    {
    'name': 'rejected_connections',
    'command': "redis-cli info | awk -F: '$1 ~ /rejected_connections$/{print $2}'",
    'desc': 'Number of connections rejected due to hitting maxclient limit',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'evicted_keys',
    'command': "redis-cli info | awk -F: '$1 ~ /evicted_keys$/{print $2}'",
    'desc': 'Number Of keys removed due to reaching maxmemory limit',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'keyspace_hits',
    'command': "redis-cli info | awk -F: '$1 ~ /keyspace_hits$/{print $2}'",
    'desc': 'Number Of keys in database',
    'type': 'summary',
    'data_type': 'integer',
    },
    {
    'name': 'master_link_down_since_seconds',
    'command': "redis-cli info | awk -F: '$1 ~ /master_link_down_since_seconds$/{print $2}'",
    'desc': 'Time since the master is been down',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'master_last_io_seconds_ago',
    'command': "redis-cli info | awk -F: '$1 ~ /master_last_io_seconds_ago$/{print $2}'",
    'desc': 'Time since last interaction between slave and master',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'used_cpu_sys',
    'command': "redis-cli info | awk -F: '$1 ~ /used_cpu_sys$/{print $2}'",
    'desc': 'System CPU consumed by Redis server',
    'type': 'summary',
    'data_type': 'float'
    },
    {
    'name': 'used_cpu_user',
    'command': "redis-cli info | awk -F: '$1 ~ /used_cpu_user$/{print $2}'",
    'desc': 'User CPU consumed by redis server',
    'type': 'summary',
    'data_type': 'float'
    },
    {
    'name': 'used_cpu_sys_children',
    'command': "redis-cli info | awk -F: '$1 ~ /used_cpu_sys_children$/{print $2}'", 
    'desc': 'System cpu consumed by background processes',
    'type': 'summary',
    'data_type': 'float'
    },
    {
    'name': 'used_cpu_user_children',
    'command': "redis-cli info | awk -F: '$1 ~ /used_cpu_user_children$/{print $2}'",
    'desc': 'User CPU consumed by the background processes',
    'type': 'summary',
    'data_type': 'float'
    },
    {
    'name': 'client_longest_output_list',
    'command': "redis-cli info | awk -F: '$1 ~ /client_longest_output_list$/{print $2}'",
    'desc': 'Longest output lists among current client connections',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'client_biggest_input_buf',
    'command': "redis-cli info | awk -F: '$1 ~ /client_biggest_input_buf$/{print $2}'",
    'desc': 'Biggest input buffers aong current client connections',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'used_memory_rss',
    'command': "redis-cli info | awk -F: '$1 ~ /used_memory_rss$/{print $2}'",
    'desc': 'Number of bytes that redis allocated as seen by operating system',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'used_memory_peak',
    'command': "redis-cli info | awk -F: '$1 ~ /used_memory_peak$/{print $2}'",
    'desc': 'Peak memory consumed by redis',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'rdb_bgsave_in_progress',
    'command': "redis-cli info | awk -F: '$1 ~ /rdb_bgsave_in_progress$/{print $2}'",
    'desc': 'Flag indiacting a rdb save is going on',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'aof_enabled',
    'command': "redis-cli info | awk -F: '$1 ~ /aof_enabled$/{print $2}'",
    'desc': 'Flag indicating AOF logging is activated',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'aof_rewrite_in_progress',
    'command': "redis-cli info | awk -F: '$1 ~ /aof_rewrite_in_progress$/{print $2}'",
    'desc': 'Flag indicating an aof rewrite is going on',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'aof_rewrite_scheduled',
    'command': "redis-cli info | awk -F: '$1 ~ /aof_rewrite_scheduled$/{print $2}'",
    'desc': 'Flag indicating AOF rewrite operation is going to be scheduled',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'total_connections_received',
    'command': "redis-cli info | awk -F: '$1 ~ /total_connections_received$/{print $2}'",
    'desc': 'Total number of connections accepted by redis server',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'total_commands_processed',
    'command': "redis-cli info | awk -F: '$1 ~ /total_commands_processed$/{print $2}'",
    'desc': 'Total number of commands processed by the server',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'expired_keys',
    'command': "redis-cli info | awk -F: '$1 ~ /expired_keys$/{print $2}'",
    'desc': 'Total number of key expiration events',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'latest_fork_usec',
    'command': "redis-cli info | awk -F: '$1 ~ /latest_fork_usec$/{print $2}'",
    'desc': 'Duration of latest fork operation in seconds',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'repl_backlog_size',
    'command': "redis-cli info | awk -F: '$1 ~ /repl_backlog_size$/{print $2}'",
    'desc': 'Capacity of a bufer holding data for PSYNC',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'repl_backlog_histlen',
    'command': "redis-cli info | awk -F: '$1 ~ /repl_backlog_histlen$/{print $2}'",
    'desc': 'Size of data which is in PSYNC buffer',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'repl_backlog_first_byte_offset',
    'command': "redis-cli info | awk -F: '$1 ~ /repl_backlog_first_byte_offset$/{print $2}'",
    'desc': 'Size of the PSYNC buffer',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'uptime_in_seconds',
    'command': "redis-cli info | awk -F: '$1 ~ /uptime_in_seconds$/{print $2}'",
    'desc': 'Number of seconds since redis server start',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'uptime_in_days',
    'command': "redis-cli info | awk -F: '$1 ~ /uptime_in_days$/{print $2}'",
    'desc': 'Number of days since redis server start',
    'type': 'summary',
    'data_type': 'integer',
    },
    {
    'name': 'lru_clock',
    'command': "redis-cli info | awk -F: '$1 ~ /lru_clock$/{print $2}'",
    'desc': 'Clock incrementing every minute for LRU management',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'total_net_input_bytes',
    'command': "redis-cli info | awk -F: '$1 ~ /total_net_input_bytes$/{print $2}'",  
    'desc': 'Total size of input in bytes',
    'type': 'summary',
    'data_type': 'integer'
    },
    {                                                                           
    'name': 'total_net_output_bytes',                                            
    'command': "redis-cli info | awk -F: '$1 ~ /total_net_output_bytes$/{print $2}'",
    'desc': 'Total size of output in bytes',                                     
    'type': 'summary',                                                           
    'data_type': 'integer'                                                       
    }          

]
