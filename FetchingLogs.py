from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
from QueryBuilder import *
from multidict import *

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")


def get_data_from_elastic(log, token, time, limit):
    
    
    query = query_builder(log, token, time, limit)
    
    
    result = scan(client=es,             
               query=query,                                     
               scroll='1m', 
               index='fluent-bit',
               raise_on_error=True,
               preserve_order=False,
               clear_scroll=True,
               size = limit)

    
    for hit in result:
        print(hit['_source'], hit['_id'])

    return result

# get_data_from_elastic('workflow-scheduler', MultiDict([('stream', 'stderr')]), time = None,limit= 100)
   

# if __name__ == "__main__":
#     t = []
   # stuff only to run when not called via 'import' here

   




















































    # from elasticsearch import Elasticsearch
    # from elasticsearch.helpers import scan

    # es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")

    # def get_data_from_elastic(log , tokens):
    
    # #    clauses = [
    # #     {
    # #        "match": {i[0]: i[1]}
            
    # #     }
    # #        for i in tokens
    # #     ]

    
    #    payload = {
    #         "query": {
    #             "bool": {
    #                 "must": {
    #                     "match": {
    #                     "app": log
    #                     }
    #                 },
    #                 "filter": [
    #                     {"match":{
    #                      "loglevel":"D"}},
    #                     {"range":{"time":{"gte":"2023-01-04T10:15:57.683414298Z"}}}
    #                 ]
    #                 }
    #             },
    #             "sort": [
    #             {
    #                 "time": {
    #                 "order": "asc"
    #                 }
    #             }
    #             ],
    #         "fields": [
    #             "message"
    #         ]
    #     }

    #    result = scan(client=es,             
    #                query=payload,                                 # stuff only to run when not called via 'import' here    
    #                scroll='1m', 
    #                index='fluent-bit',
    #                raise_on_error=True,
    #                preserve_order=False,
    #                clear_scroll=True,
    #                size = 100)

    #    # Keep response in a list.
    
    #    list = []
    #    for hit in result:
    #         print(hit['_source'])


    #    return list

    # log = 'istio-proxy'
    # token = []

    # get_data_from_elastic(log, token)





    # #    payload = {
    # #         "query": {
    # #             "bool": {
    # #                 "must": [{"match": {"app.keyword": log}}
    # #                  ,{"span_near": {"clauses": clauses, "slop": 0, "in_order": False}}
    # #                 ],
    # #                 "filter": [{"match": {"logdata": logdata}},{"match": {"logs": logs}}, {"match": {"stream": stream}} ]
    # #             } 
    # #         }
        
    # #     }


    # # payload = {
    # #         "query": {
    # #                 },
    # #                 "filter": [
    # #                     {"match":{
    # #                      "loglevel":"D"}},
    # #                     {"range":{"time":{"gte":"2023-01-04T10:15:57.683414298Z"}}}
    # #                 ]
    # #                 }
    # #             },
    # #             "sort": [
    # #             {
    # #                 "time": {
    # #                 "order": "asc"
    # #                 }
    # #             }
    # #             ],
    # #         "fields": [
    # #             "message"
    # #         ]
    # #     }

    #                     "app": "log"
    # #                     }
    # #                 },
    # #                 "filter": [
    # #                     {"match":{
    # #                      "loglevel":"D"}},
    # #                     {"range":{"time":{"gte":"2023-01-04T10:15:57.683414298Z"}}}
    # #                 ]
    # #                 }
    # #             },
    # #             "sort": [
    # #             {
    # #                 "time": {
    # #                 "order": "asc"
    # #                 }
    # #             }
    # #             ],
    # #         "fields": [
    # #             "message"
    # #         ]
    # #     }


