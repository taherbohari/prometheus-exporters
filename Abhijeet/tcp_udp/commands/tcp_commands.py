#!/usr/bin/python

tcp_udp_metrics=[
	{
		'name' : 'sockstat_sockets',
		'command' : 'cat /proc/net/sockstat| awk "/sockets/ { print $3 }" | cut -d":" -f2 | cut -d " " -f3',
		'description' : 'total number of sockets used',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_tcp_inuse',
		'command' : "cat /proc/net/sockstat| awk '/TCP/ { print $3 }'",
		'description' : 'total established connections',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_tcp_orphan',
		'command' : "cat /proc/net/sockstat| awk '/TCP/ { print $3 }'",
		'description' : 'Orphaned tcp connections(not attached to any user file handle)',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_tcp_timewait',
		'command' : "cat /proc/net/sockstat| awk '/TCP/ { print $7 }'",
		'description' : 'TIME_WAIT connections(millisec)',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_tcp_allocated',
		'command' : "cat /proc/net/sockstat| awk '/TCP/ { print $9 }'",
		'description' : 'TCP sockets allocated( All type for example, ESTABLISH, CLOSE_WAIT, TIME_WAIT, etc)',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_tcp_mem',
		'command' : "cat /proc/net/sockstat| awk '/TCP/ { print $11 }'",
		'description' : 'total memory for TCP socket(KiloBytes)',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_udp_inuse',
		'command' : "cat /proc/net/sockstat| awk '/UDP:/ { print $3 }'",
		'description' : 'total established connections',
		'type' : 'summary'
	},

	{
		'name' : 'sockstat_udp_mem',
		'command' : "cat /proc/net/sockstat| awk '/UDP:/ { print $5 }'",
		'description' : 'total memory for udp socket(KB)',
		'type' : 'summary'
	},



]
