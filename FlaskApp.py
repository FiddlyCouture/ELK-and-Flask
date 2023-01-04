import os
from flask import Flask, render_template, abort, url_for, json, jsonify, redirect, request  
import json
import html
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from FetchingLogs import get_data_from_elastic

app = Flask(__name__)

es = Elasticsearch("https://exl.workbench.couture.ai/elastic/")
print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

@app.route('/admin')
def base_log():
   return 'Hello Base'

@app.route('/app/<log>')
def system_log(log):
   logdata = request.args.get('logdata')
   logs = request.args.get('log')
   stream = request.args.get('stream')
   # time = request.args.get('time') # tokens = qu.split(" ")
   this_log = get_data_from_elastic(log, logdata, logs, stream)
   # return render_template('index.html', title="page", jsonfile=json.dumps(this_log))
   return this_log
   

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