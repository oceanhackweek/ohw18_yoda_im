import sys
import json
import requests
import pandas as pd
from flask import Flask, request, abort, jsonify, send_file, Response

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)


def string_match(a, b): 
  return a in b

@app.route("/")
def hello():
    return "hello world"


### DATA PRODUCTS ROUTE
@app.route("/products")
def list_data_products():
    ## Request all parameters from visual ocean
    params = requests.get("{}/parameters.json".format(base_url)).json()
    df = pd.DataFrame.from_records(params['data'])

    ## Filter only science data
    sdf = df[df.data_product_type == 'Science Data']

    ## Concatinate the lists, sort, unique-ify, and drop nones
    all_params = list(sdf['display_name'].dropna().values) + list(sdf['name'].dropna().values) + list(sdf['standard_name'].dropna().values)
    unique_list = sorted(list(set(all_params)))
    
    ## what does this do?
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
    nodes    = requests.get('/'.join([base_url, 'nodes.json'])).json()
    nodes_df = pd.DataFrame.from_records(nodes['nodes'])
    unique_nodes = sorted(list(set(nodes_df['name'].dropna().values)))
    return jsonify(unique_nodes)


if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
