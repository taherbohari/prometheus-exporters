cluster_health_metrices=[
    {
        "name": "active_primary_shards",
        "param": ['active_primary_shards'],
        "description": "Number of active primary shards",
        "type": "summary"
    },
    {
        "name": "active_shards",
        "param": ['active_shards'],
        "description": "Number of active shards",
        "type": "summary"
    },
    {
        "name": "active_shards_percent_as_number",
        "param": ['active_shards_percent_as_number'],
        "description": "Percentage of active shards",
        "type": "summary"
    },
    {
        "name": "delayed_unassigned_shards",
        "param": ['delayed_unassigned_shards'],
        "description": "Number of delayed unassigned shards",
        "type": "summary"
    },
    {
        "name": "initializing_shards",
        "param": ['initializing_shards'],
        "description": "Number of initializing shards",
        "type": "summary"
    },
    {
        "name": "number_of_data_nodes",
        "param": ['number_of_data_nodes'],
        "description": "Number of data nodes",
        "type": "summary"
    },
    {
        "name": "number_of_in_flight_fetch",
        "param": ['number_of_in_flight_fetch'],
        "description": "Number of in flight fetch",
        "type": "summary"
    },
    {
        "name": "number_of_nodes",
        "param": ['number_of_nodes'],
        "description": "Total number of nodes",
        "type": "summary"
    },
    {
        "name": "number_of_pending_tasks",
        "param": ['number_of_pending_tasks'],
        "description": "Number of pending tasks",
        "type": "summary"
    },
    {
        "name": "relocating_shards",
        "param": ['relocating_shards'],
        "description": "Number of relocating shards",
        "type": "summary"
    },
    {
        "name": "unassigned_shards",
        "param": ['unassigned_shards'],
        "description": "Number of unassigned shards",
        "type": "summary"
    },
    {
        "name": "task_max_waiting_in_queue_millis",
        "param": ['task_max_waiting_in_queue_millis'],
        "description": "Waiting time of task in queue",
        "type": "summary"
    }
]

cluster_status_metrices=[
    {
        "name": "cluster_status",
        "param": ['cluster_status'],
        "description": "Status of cluster",
        "type": "summary"
    }
]

cluster_stats_metrices=[
    {
        "name": "total_indices_count",
        "param": ['indices', 'count'],
        "description": "Total number of indices in cluster",
        "type": "summary"
    },
    {
        "name": "total_docs_count",
        "param": ['indices', 'docs', 'count'],
        "description": "Total number of docs in cluster",
        "type": "summary"
    },
    {
        "name": "total_docs_deleted",
        "param": ['indices', 'docs', 'deleted'],
        "description": "Number of docs deleted",
        "type": "summary"
    }
]

index_stats_metrices=[
#u'flush':  {u'total':  5,
#           u'total_time_in_millis':  2},
    {
        "name": "flush_total",
        "param": ['_all', 'total', 'flush', 'total'],
        "description": "Total number of flush",
        "type": "summary"
    },
    {
        "name": "flush_total_time_in_millis",
        "param": ['_all', 'total', 'flush', 'total_time_in_millis'],
        "description": "Time taken to flush",
        "type": "summary"
    },

#u'get':  {u'current':  0,
#         u'exists_time_in_millis':  0,
#         u'exists_total':  0,
#         u'missing_time_in_millis':  0,
#         u'missing_total':  0,
#         u'time_in_millis':  0,
#         u'total':  0},
    {
        "name": "get_current",
        "param": ['_all', 'total', 'get', 'current'],
        "description": "Total number of get requests",
        "type": "summary"
    },
    {
        "name": "get_exists_time_in_millis",
        "param": ['_all', 'total', 'get', 'exists_time_in_millis'],
        "description": "Total time get requests exists",
        "type": "summary"
    },
    {
        "name": "get_exists_total",
        "param": ['_all', 'total', 'get', 'exists_total'],
        "description": "Total number of get request exists",
        "type": "summary"
    },
    {
        "name": "get_missing_time_in_millis",
        "param": ['_all', 'total', 'get', 'missing_time_in_millis'],
        "description": "Total time get requests missing",
        "type": "summary"
    },
    {
        "name": "get_missing_total",
        "param": ['_all', 'total', 'get', 'missing_total'],
        "description": "Total number of get request missing",
        "type": "summary"
    },
    {
        "name": "get_time_in_millis",
        "param": ['_all', 'total', 'get', 'time_in_millis'],
        "description": "Time spent on geting requests",
        "type": "summary"
    },
    {
        "name": "get_total",
        "param": ['_all', 'total', 'get', 'total'],
        "description": "Total number of get requests",
        "type": "summary"
    },


#u'indexing':  {u'delete_current':  0,
#              u'delete_time_in_millis':  0,
#              u'delete_total':  0,
#              u'index_current':  0,
#              u'index_failed':  0,
#              u'index_time_in_millis':  0,
#              u'index_total':  0,
#              u'is_throttled':  False,
#              u'noop_update_total':  0,
#              u'throttle_time_in_millis':  0},

    {
        "name": "indexing_delete_current",
        "param": ['_all', 'total', 'indexing', 'delete_current'],
        "description": "Number of deleted current index",
        "type": "summary"
    },
    {
        "name": "indexing_delete_time_in_millis",
        "param": ['_all', 'total', 'indexing', 'delete_time_in_millis'],
        "description": "Time taken to delete index",
        "type": "summary"
    },
    {
        "name": "indexing_delete_total",
        "param": ['_all', 'total', 'indexing', 'delete_total'],
        "description": "Number of deleted index",
        "type": "summary"
    },
    {
        "name": "indexing_index_current",
        "param": ['_all', 'total', 'indexing', 'index_current'],
        "description": "Number of current index",
        "type": "summary"
    },
    {
        "name": "indexing_index_failed",
        "param": ['_all', 'total', 'indexing', 'index_failed'],
        "description": "Number of index failed",
        "type": "summary"
    },
    {
        "name": "indexing_index_time_in_millis",
        "param": ['_all', 'total', 'indexing', 'index_time_in_millis'],
        "description": "Total time spent on indexing",
        "type": "summary"
    },
    {
        "name": "indexing_index_total",
        "param": ['_all', 'total', 'indexing', 'index_total'],
        "description": "Total number of index",
        "type": "summary"
    },
    {
        "name": "indexing_noop_update_total",
        "param": ['_all', 'total', 'indexing', 'noop_update_total'],
        "description": "Total noop updates",
        "type": "summary"
    },
    {
        "name": "indexing_throttle_time_in_millis",
        "param": ['_all', 'total', 'indexing', 'throttle_time_in_millis'],
        "description": "Indexing throttle time in millis",
        "type": "summary"
    },

#u'refresh':  {u'listeners':  0,
#             u'total':  25,
#             u'total_time_in_millis':  9},
    {
        "name": "refresh_total",
        "param": ['_all', 'total', 'refresh', 'total'],
        "description": "Total number of refreshesh",
        "type": "summary"
    },
    {
        "name": "refresh_total_time_in_millis",
        "param": ['_all', 'total', 'refresh', 'total_time_in_millis'],
        "description": "Time taken by refresh",
        "type": "summary"
    },

#u'search':  {u'fetch_current':  0,
#            u'fetch_time_in_millis':  0,
#            u'fetch_total':  0,
#            u'open_contexts':  0,
#            u'query_current':  0,
#            u'query_time_in_millis':  0,
#            u'query_total':  0,
#            u'scroll_current':  0,
#            u'scroll_time_in_millis':  0,
#            u'scroll_total':  0,
#            u'suggest_current':  0,
#            u'suggest_time_in_millis':  0,
#            u'suggest_total':  0},

    {
        "name": "search_fetch_current",
        "param": ['_all', 'total', 'search', 'fetch_current'],
        "description": "Total number of current fetch queries",
        "type": "summary"
    },
    {
        "name": "search_fetch_time_in_millis",
        "param": ['_all', 'total', 'search', 'fetch_time_in_millis'],
        "description": "Time spent on fetch queries",
        "type": "summary"
    },
    {
        "name": "search_fetch_total",
        "param": ['_all', 'total', 'search', 'fetch_total'],
        "description": "Total number of fetch queries",
        "type": "summary"
    },
    {
        "name": "search_open_contexts",
        "param": ['_all', 'total', 'search', 'open_contexts'],
        "description": "Number of open context",
        "type": "summary"
    },
    {
        "name": "search_query_current",
        "param": ['_all', 'total', 'search', 'query_current'],
        "description": "Total number of current search queries",
        "type": "summary"
    },
    {
        "name": "search_query_time_in_millis",
        "param": ['_all', 'total', 'search', 'query_time_in_millis'],
        "description": "Time spent on search queries",
        "type": "summary"
    },
    {
        "name": "search_query_total",
        "param": ['_all', 'total', 'search', 'query_total'],
        "description": "Total number of search queries",
        "type": "summary"
    },
    {
        "name": "search_scroll_current",
        "param": ['_all', 'total', 'search', 'scroll_current'],
        "description": "Total number of current scroll",
        "type": "summary"
    },
    {
        "name": "search_scroll_time_in_millis",
        "param": ['_all', 'total', 'search', 'scroll_time_in_millis'],
        "description": "Time spent on scroll",
        "type": "summary"
    },
    {
        "name": "search_scroll_total",
        "param": ['_all', 'total', 'search', 'scroll_total'],
        "description": "Total number of scroll",
        "type": "summary"
    },
    {
        "name": "search_suggest_current",
        "param": ['_all', 'total', 'search', 'suggest_current'],
        "description": "Total number of current suggest",
        "type": "summary"
    },
    {
        "name": "search_suggest_time_in_millis",
        "param": ['_all', 'total', 'search', 'suggest_time_in_millis'],
        "description": "Time spent on suggest",
        "type": "summary"
    },
    {
        "name": "search_suggest_total",
        "param": ['_all', 'total', 'search', 'suggest_total'],
        "description": "Total number of suggest",
        "type": "summary"
    },

#u'store':  {u'size_in_bytes':  474958,
#           u'throttle_time_in_millis':  0},

    {
        "name": "store_size_in_bytes",
        "param": ['_all', 'total', 'store', 'size_in_bytes'],
        "description": "Store size in bytes",
        "type": "summary"
    },
    {
        "name": "store_throttle_time_in_millis",
        "param": ['_all', 'total', 'store', 'throttle_time_in_millis'],
        "description": "Throttle time in millis",
        "type": "summary"
    },

#u'translog':  {u'operations':  0,
#              u'size_in_bytes':  430},
    {
        "name": "translog_operations",
        "param": ['_all', 'total', 'translog', 'operations'],
        "description": "Number of translog operations",
        "type": "summary"
    },
    {
        "name": "translog_size_in_bytes",
        "param": ['_all', 'total', 'translog', 'size_in_bytes'],
        "description": "Translog size in bytes",
        "type": "summary"
    },

]

node_stats_metrices=[
    {
        "name": "jvm_buffer_pools_direct_count",
        "param": ['jvm', 'buffer_pools', 'direct', 'count'],
        "description": "Direct buffer pools count ",
        "type": "summary"
    },
    {
        "name": "jvm_buffer_pools_direct_total_capacity_in_bytes",
        "param": ['jvm', 'buffer_pools', 'direct', 'total_capacity_in_bytes'],
        "description": "Direct buffer pools total capacity ",
        "type": "summary"
    },
    {
        "name": "jvm_buffer_pools_direct_used_in_bytes",
        "param": ['jvm', 'buffer_pools', 'direct', 'used_in_bytes'],
        "description": "Direct buffer pools used",
        "type": "summary"
    },
    {
        "name": "jvm_buffer_pools_mapped_count",
        "param": ['jvm', 'buffer_pools', 'mapped', 'count'],
        "description": "mapped buffer pools count ",
        "type": "summary"
    },
    {
        "name": "jvm_buffer_pools_mapped_total_capacity_in_bytes",
        "param": ['jvm', 'buffer_pools', 'mapped', 'total_capacity_in_bytes'],
        "description": "mapped buffer pools total capacity ",
        "type": "summary"
    },
    {
        "name": "jvm_buffer_pools_mapped_used_in_bytes",
        "param": ['jvm', 'buffer_pools', 'mapped', 'used_in_bytes'],
        "description": "mapped buffer pools used",
        "type": "summary"
    },
    {
        "name": "jvm_classes_current_loaded_count",
        "param": ['jvm', 'classes', 'current_loaded_count'],
        "description": "Current loaded classes",
        "type": "summary"
    },
    {
        "name": "jvm_classes_total_loaded_count",
        "param": ['jvm', 'classes', 'total_loaded_count'],
        "description": "Total loaded classes",
        "type": "summary"
    },
    {
        "name": "jvm_classes_total_unloaded_count",
        "param": ['jvm', 'classes', 'total_unloaded_count'],
        "description": "Total unloaded classes",
        "type": "summary"
    },
#gc collector
    {
        "name": "jvm_gc_collectors_old_collection_count",
        "param": ['jvm', 'gc', 'collectors', 'old', 'collection_count'],
        "description": "Old gc collection count",
        "type": "summary"
    },
    {
        "name": "jvm_gc_collectors_old_collection_time_in_millis",
        "param": ['jvm', 'gc', 'collectors', 'old', 'collection_time_in_millis'],
        "description": "Old gc collection time in millis",
        "type": "summary"
    },
    {
        "name": "jvm_gc_collectors_young_collection_count",
        "param": ['jvm', 'gc', 'collectors', 'young', 'collection_count'],
        "description": "young gc collection count",
        "type": "summary"
    },
    {
        "name": "jvm_gc_collectors_young_collection_time_in_millis",
        "param": ['jvm', 'gc', 'collectors', 'young', 'collection_time_in_millis'],
        "description": "young gc collection time in millis",
        "type": "summary"
    },
#mem
    {
        "name": "jvm_mem_heap_committed_in_bytes",
        "param": ['jvm', 'mem', 'heap_committed_in_bytes'],
        "description": "Heap memory commited in bytes",
        "type": "summary"
    },
    {
        "name": "jvm_mem_heap_max_in_bytes",
        "param": ['jvm', 'mem', 'heap_max_in_bytes'],
        "description": "Max heap memory in bytes",
        "type": "summary"
    },
    {
        "name": "jvm_mem_heap_used_in_bytes",
        "param": ['jvm', 'mem', 'heap_used_in_bytes'],
        "description": "Used heap memory in bytes",
        "type": "summary"
    },
    {
        "name": "jvm_mem_heap_used_percent",
        "param": ['jvm', 'mem', 'heap_used_percent'],
        "description": "Used heap memory percent",
        "type": "summary"
    },
    {
        "name": "jvm_mem_non_heap_committed_in_bytes",
        "param": ['jvm', 'mem', 'non_heap_committed_in_bytes'],
        "description": "Non heap memory commited in bytes",
        "type": "summary"
    },
    {
        "name": "jvm_mem_non_heap_used_in_bytes",
        "param": ['jvm', 'mem', 'non_heap_used_in_bytes'],
        "description": "Non heap memory used in bytes",
        "type": "summary"
    },
    {
        "name": "jvm_mem_heap_used_in_bytes",
        "param": ['jvm', 'mem', 'heap_used_in_bytes'],
        "description": "Used heap memory in bytes",
        "type": "summary"
    },
#mem pool old
    {
        "name": "jvm_mem_pools_old_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'max_in_bytes'],
        "description": "Max old memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_old_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'peak_max_in_bytes'],
        "description": "Peak max old memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_old_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'peak_used_in_bytes'],
        "description": "Peak used old memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_old_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'used_in_bytes'],
        "description": "Used old memory pool",
        "type": "summary"
    },
#mem pool young
    {
        "name": "jvm_mem_pools_young_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'max_in_bytes'],
        "description": "Max young memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_young_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'peak_max_in_bytes'],
        "description": "Peak max young memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_young_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'peak_used_in_bytes'],
        "description": "Peak used young memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_young_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'used_in_bytes'],
        "description": "Used young memory pool",
        "type": "summary"
    },
#mem pool survivor
    {
        "name": "jvm_mem_pools_survivor_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'max_in_bytes'],
        "description": "Max survivor memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_survivor_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'peak_max_in_bytes'],
        "description": "Peak max survivor memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_survivor_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'peak_used_in_bytes'],
        "description": "Peak used survivor memory pool",
        "type": "summary"
    },
    {
        "name": "jvm_mem_pools_survivor_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'used_in_bytes'],
        "description": "Used survivor memory pool",
        "type": "summary"
    }
]

cat_metrices=[
    {
        "name": "node_disk_used",
        "param": 2,
        "description": "Total disk used by node",
        "type": "summary"
    },
    {
        "name": "node_disk_available",
        "param": 3,
        "description": "Total disk available",
        "type": "summary"
    }
]
