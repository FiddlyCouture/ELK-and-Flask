import os
from flask import Flask, render_template, abort, url_for, json, jsonify, redirect, request  
import json
import html
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import FetchingLogs

app = Flask(__name__)

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")
# print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")


@app.route('/app/<log>')
def system_log(log):
   print(request.args)
   
   times = request.args.get("time")
   if times:
      key1 = request.args.to_dict().pop('time', None)
   
   Limit = request.args.get("limit",10)
   if Limit:
      key1 = request.args.to_dict().pop('limit', None)

   this_log = FetchingLogs.get_data_from_elastic(log, request.args, times, Limit)
   
   return this_log
   
if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)







# @app.route('/search', methods=['POST'])
# def search():
#     payload = request.json
#     query = payload['q']
#     field = payload.get('field', 'message')  # set a default value for 'field'
#     time = payload.get('time')  # time is optional
#     size = payload.get('size', 10)  # set a default value for 'size'
#     body = {'query': {'match': {field: query}}}
#     if time:
#         # add time range filter to the query
#         body['query']['bool'] = {'filter': {'range': {'@timestamp': {'gte': time['gte'], 'lte': time['lte']}}}}
#     results = []
#     for result in scan(client=es, query=body, size=size):
#         results.append(result)
#     return results


# @app.route('/logs/<log>')
# def hello_log(log):
#    if log =='admin':
#       return redirect(url_for('base_log'))
#    else:
#       return redirect(url_for('system_log',log = log))