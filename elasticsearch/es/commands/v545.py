#!/usr/bin/python
elasticsearch_metrices=[

{
	"name":"docs_count",
	"command": ic_stats['_all']['total']['docs']['count'],
	"description":"Total number of documents",
	"type":"summary"
},
{
	"name":"docs_deleted",
	"command": ic_stats['_all']['total']['docs']['deleted'],
	"description":"Number of documents deleted",
	"type":"summary"
}

]
