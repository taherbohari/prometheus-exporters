#!/usr/bin/python

#----------------------------------- JVM metrics ------------------------
jvm_metrices=[
    {
        "name": "threads_count",
        "param": ['jvm', 'threads', 'count'],
        "description": "Count of jvm threads",
        "type": "counter"
    },
    {
        "name": "threads_peak_count",
        "param": ['jvm', 'threads', 'peak_count'],
        "description": "Peak count of jvm threads",
        "type": "counter"
    },
    ############################# HEAP
    {
        "name": "mem_heap_used_percent",
        "param": ['jvm', 'mem', 'heap_used_percent'],
        "description": "Used heap memory percentage",
        "type": "gauge"
    },

    {
        "name": "mem_heap_committed_in_bytes",
        "param": ['jvm', 'mem', 'heap_committed_in_bytes'],
        "description": "Heap committed in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_heap_max_in_bytes",
        "param": ['jvm', 'mem', 'heap_max_in_bytes'],
        "description": "Max heap size in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_heap_used_in_bytes",
        "param": ['jvm', 'mem', 'heap_used_in_bytes'],
        "description": "Used heap size in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_non_heap_used_in_bytes",
        "param": ['jvm', 'mem', 'non_heap_used_in_bytes'],
        "description": "Not used heap size in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_non_heap_committed_in_bytes",
        "param": ['jvm', 'mem', 'non_heap_used_in_bytes'],
        "description": "Non heap committed in bytes",
        "type": "gauge"
    },
    ############################# SURVIVOR
    {
        "name": "mem_pools_survivor_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'peak_used_in_bytes'],
        "description": "Peak memory used by survivor pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_survivor_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'used_in_bytes'],
        "description": "Memory used by survivor pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_survivor_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'peak_max_in_bytes'],
        "description": "Max peak Memory for survivor pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_survivor_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'max_in_bytes'],
        "description": "Total Max memory for survivor pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_survivor_committed_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'survivor', 'committed_in_bytes'],
        "description": "Memory committed by survivor pools in bytes",
        "type": "gauge"
    },
    ############################# OLD
    {
        "name": "mem_pools_old_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'peak_used_in_bytes'],
        "description": "Peak memory used by old pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_old_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'used_in_bytes'],
        "description": "Memory used by old pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_old_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'peak_max_in_bytes'],
        "description": "Max peak Memory for old pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_old_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'max_in_bytes'],
        "description": "Total Max memory for old pools in bytes",
        "type": "gauge"
    },

    {
        "name": "mem_pools_old_committed_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'old', 'committed_in_bytes'],
        "description": "Memory committed by old pools in bytes",
        "type": "gauge"
    },
    ############################# YOUNG
    {
        "name": "mem_pools_young_peak_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'peak_used_in_bytes'],
        "description": "Peak memory used by young pools in bytes",
        "type": "gauge"
    },
    {
        "name": "mem_pools_young_used_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'used_in_bytes'],
        "description": "Memory used by young pools in bytes",
        "type": "gauge"
    },
    {
        "name": "mem_pools_young_peak_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'peak_max_in_bytes'],
        "description": "Max peak Memory for young pools in bytes",
        "type": "gauge"
    },
    {
        "name": "mem_pools_young_max_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'max_in_bytes'],
        "description": "Total Max memory for young pools in bytes",
        "type": "gauge"
    },
    {
        "name": "mem_pools_young_committed_in_bytes",
        "param": ['jvm', 'mem', 'pools', 'young', 'committed_in_bytes'],
        "description": "Memory committed by young pools in bytes",
        "type": "gauge"
    },
    ########################## GARBAGE COLLECTION
    {
        "name": "gc_collectors_old_collection_count",
        "param": ['jvm', 'gc', 'collectors', 'old', 'collection_count'],
        "description": "Total count of old generation garbage collections",
        "type": "counter"
    },
    {
        "name": "gc_collectors_old_collection_time_in_millis",
        "param": ['jvm', 'gc', 'collectors', 'old', 'collection_time_in_millis'],
        "description": "Time spent on old generation garbage collections",
        "type": "gauge"
    },
    {
        "name": "gc_collectors_young_collection_count",
        "param": ['jvm', 'gc', 'collectors', 'young', 'collection_count'],
        "description": "Total count of young generation garbage collections",
        "type": "counter"
    },
    {
        "name": "gc_collectors_young_collection_time_in_millis",
        "param": ['jvm', 'gc', 'collectors', 'young', 'collection_time_in_millis'],
        "description": "Time spent on young generation garbage collections",
        "type": "gauge"
    },
    ############################ JVM UPTIME
    {
        "name": "jvm_uptime_in_millis",
        "param": ['jvm', 'uptime_in_millis'],
        "description": "Total running time of jvm in millis",
        "type": "counter"
    }
]

#-------------------------------- process metrics-----------------------------------
process_metrices=[
    {
        "name": "process_open_file_descriptors",
        "param": ['process', 'open_file_descriptors'],
        "description": "Number of open file discriptors",
        "type": "gauge"
    },
    {
        "name": "process_peak_open_file_descriptors",
        "param": ['process', 'peak_open_file_descriptors'],
        "description": "Number of peak open file discriptors",
        "type": "gauge"
    },
    {
        "name": "process_max_file_descriptors",
        "param": ['process', 'max_file_descriptors'],
        "description": "Number of max file discriptors",
        "type": "gauge"
    },
    {
        "name": "process_mem_total_virtual_in_bytes",
        "param": ['process', 'mem', 'total_virtual_in_bytes'],
        "description": "Total virtual memory in bytes",
        "type": "gauge"
    },
    {
        "name": "process_cpu_total_in_millis",
        "param": ['process', 'cpu', 'total_in_millis'],
        "description": "Total running time of cpu",
        "type": "counter"
    },
    {
        "name": "process_cpu_percent",
        "param": ['process', 'cpu', 'percent'],
        "description": "Percentage of cpu used",
        "type": "gauge"
    },
]

#-------------------------------- pipeline metrics-----------------------------------
pipeline_metrices=[
    {
        "name": "pipeline_events_duration_in_millis",
        "param": ['pipeline', 'events', 'duration_in_millis'],
        "description": "Total event duration in millis",
        "type": "counter"
    },
    {
        "name": "pipeline_events_in",
        "param": ['pipeline', 'events', 'in'],
        "description": "Number of event in",
        "type": "counter"
    },
    {
        "name": "pipeline_events_out",
        "param": ['pipeline', 'events', 'out'],
        "description": "Number of events out",
        "type": "counter"
    },
    {
        "name": "pipeline_events_filtered",
        "param": ['pipeline', 'events', 'filtered'],
        "description": "Number of event filtered",
        "type": "counter"
    },
    {
        "name": "pipeline_events_queue_push_duration_in_millis",
        "param": ['pipeline', 'events', 'queue_push_duration_in_millis'],
        "description": "Time taken to push events in queue in millis",
        "type": "gauge"
    },
    {
        "name": "pipeline_reloads_successes",
        "param": ['pipeline', 'reloads', 'successes'],
        "description": "Number of config reload successes",
        "type": "counter"
    },
    {
        "name": "pipeline_reloads_failures",
        "param": ['pipeline', 'reloads', 'failures'],
        "description": "Number of config reload failures",
        "type": "counter"
    },
]

