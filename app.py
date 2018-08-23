import sys
import json
import requests
import pandas as pd
import numpy as np
from flask import Flask, request, abort, jsonify, send_file, Response
from visualocean import VisualOcean, merge_name_rd

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)
visual_ocean = VisualOcean(base_url)


def string_match(a, b): 
  return a in b

@app.route("/")
def hello():
    return "hello world"


### DATA PRODUCTS ROUTE
@app.route("/products")
def list_data_products():
    unique_list = visual_ocean.products()
    f = request.args.get('filter')
    if (f):
      lf = f.lower()
      unique_list = list(filter(lambda s: lf in s.lower(), unique_list))
    return jsonify(unique_list)
    # return jsonify(list(sdf.display_name.unique()))

@app.route("/instruments")
def list_instruments():
    ## Request JSON instrument info from visual oceans
    inst = requests.get('/'.join([base_url, 'instruments.json'])).json()
    ## Convert to pandaframe
    inst_df = pd.DataFrame.from_records(inst['data'])
    ## Sort, remove dupes, drop nones, convert to list
    unique_inst	= sorted(list(set(inst_df['name'].dropna().values)))
    return jsonify(unique_inst)


@app.route("/nodes")
def list_nodes():
    nnames = requests.get('/'.join([base_url, 'nodes.json'])).json()
    nodes_df    = pd.DataFrame.from_records(nnames['nodes'])
    node_names  = nodes_df['name']
    node_refIDs = nodes_df['reference_designator']
    nnames = node_names.apply(lambda x: x.split('(')[0])
    unique_nodes = list(np.sort(nodes_df.apply(merge_name_rd, axis=1).unique()))
#    nodes    = requests.get('/'.join([base_url, 'nodes.json'])).json()
#    nodes_df = pd.DataFrame.from_records(nodes['nodes'])
#    unique_nodes = sorted(list(set(nodes_df['name'].dropna().values)))
    return jsonify(unique_nodes)


if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
