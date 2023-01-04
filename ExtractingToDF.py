from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")

def get_data_from_elastic(log):
    # query: The elasticsearch query.
    query = {
        "query": {
            "match": {
                "app.keyword": log
            }
        }
    }

    # Scan function to get all the data. 
    
    result = scan(client=es,             
               query=query,                                     
               scroll='1m', 
               index='fluent-bit',
               raise_on_error=True,
               preserve_order=False,
               clear_scroll=True)

    # We need only '_source', which has all the fields required.
    # This elimantes the elasticsearch metdata like _id, _type, _index.
    
    for hit in result:
        print(hit['_source'], hit['_id'])

    return result

log = "istio-proxy"
get_data_from_elastic(log)

# print(df.head())