import os
from flask import Flask, render_template, abort, url_for, json, jsonify, redirect
import json
import html
app = Flask(__name__)
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")

def get_data_from_elastic(log):
   
   #Fetching Queries on the basis of App keyword
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

   # Keep response in a list.
   
   # list = []
   # for hit in result:
   #      list.append(hit['_source'])


   return result['_source']


@app.route('/admin')
def base_log():
   return 'Hello Base'

@app.route('/app/<log>')
def system_log(log):
   this_log = get_data_from_elastic(log)
   return render_template('index.html', title="page", jsonfile=json.dumps(this_log))
   

@app.route('/logs/<log>')
def hello_log(log):
   if log =='admin':
      return redirect(url_for('base_log'))
   else:
      return redirect(url_for('system_log',log = log))


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)