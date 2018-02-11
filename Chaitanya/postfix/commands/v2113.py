#!/usr/bin/python
postfix_metrices=[
    {
    'name': 'total_mails',
    'command': "pqshell --summary |awk '/Total mails in queue:/ {print $5}'",
    'desc': 'Number of mails in the queue',
    'type': 'summary',
    'data_type': 'integer',
    },
    {
    'name': 'status_active',
    'command': "pqshell --summary |awk '/Active/ {print $2}'",
    'desc': 'Number of mails with active status',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'status_deferred',
    'command': "pqshell --summary |awk '/Deferred/ {print $2}'",
    'desc': 'Number of mails with deferred status',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'status_hold',
    'command': "pqshell --summary |awk '/Hold/ {print $2}'",
    'desc': 'Number of mails with hold status',
    'type': 'summary',
    'data_type': 'integer'
    },
    {
    'name': 'queue_size',
    'command': "pqshell --summary |awk '/Total queue size/ {print $4}'",
    'desc': 'Size of the mail queue in MB',
    'type': 'summary',
    'data_type': 'float'
    }

]
