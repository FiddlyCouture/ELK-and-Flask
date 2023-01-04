from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")

def get_data_from_elastic(log , logdata, logs, stream):
   
#    query = {
#         "query": {
#             "match": {
#                 "app.keyword": log
#             }
#         }
#     }
    
#    clauses = [
#     {
#         "span_multi": {
#             "match": {"fuzzy": {"log": {"value": i, "fuzziness": "AUTO"}}}
#         }
#     }
#         for i in tokens
#     ]

   payload = {
        "query": {
            "bool": {
                "must": [{"match": {"app.keyword": log}}
                # ,{"span_near": {"clauses": clauses, "slop": 0, "in_order": False}}
                ],
                "filter": [{"match": {"logdata": logdata}},{"match": {"logs": logs}}, {"match": {"stream": stream}} ]
            } 
        }
    
    }

   result = scan(client=es,             
               query=payload,                                     
               scroll='1m', 
               index='fluent-bit',
               raise_on_error=True,
               preserve_order=False,
               clear_scroll=True,
               size = 100)

   # Keep response in a list.
   
   list = []
   for hit in result:
        print(hit['_source'])


   return list

log = 'istio-proxy'
logdata = """- via_upstream - "-" 0 466 6 5 "-" "Go-http-client/1.1" "2f5d8f11-592a-448b-a5c9-045e9755c0f9" "a10f0c4949f624418895556815a713ca-78314279.us-east-1.elb.amazonaws.com" "54.174.149.51:80" outbound|80||a10f0c4949f624418895556815a713ca-78314279.us-east-1.elb.amazonaws.com 10.109.0.62:55404 54.174.149.51:80 10.109.0.62:55400 - - """
logs = " "
stream = " "
time = ""
get_data_from_elastic(log, logdata, logs, stream)


