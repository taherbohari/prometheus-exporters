#!/usr/bin/python
kafka_metrices=[
   # {
   # 'name': 'number_of_partitions',
   # 'command': "/opt/kafka/kafka_2.11-1.0.0/bin/kafka-topics.sh --describe --zookeeper localhost:2181",
   # 'desc': 'Number of partitions',
   # 'type': 'counter',
   # 'data_type': 'integer'
   # },
   # {
   # 'name': 'number_of_replications',
   # 'command': "/opt/kafka/kafka_2.11-1.0.0/bin/kafka-topics.sh --describe --zookeeper localhost:2181",
   # 'desc': 'Number of replications',
   # 'type': 'counter',
   # 'data_type': 'integer'
   # },
    {
    'name': 'number_of_topics',
    'command': "/opt/kafka/kafka_2.11-1.0.0/bin/kafka-topics.sh --list --zookeeper localhost:2181|wc -l",
    'desc': 'Number of topics',
    'type': 'counter',
    'data_type': 'integer'
    }
    




]
