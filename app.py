import sys
import json
import requests
import pandas as pd
import numpy as np
from flask_cors import CORS
from flask import Flask, request, abort, jsonify, send_file, Response
from visualocean import VisualOcean, merge_name_rd

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)
CORS(app)
visualocean = VisualOcean(base_url)


def string_match(a, b):
    return a in b


@app.route("/")
def hello():
    return "hello world"


@app.route("/products")
def list_data_products():
    unique_list = visualocean.products()
    f = request.args.get('filter')
    if (f):
        lf = f.lower()
        unique_list = list(filter(lambda s: lf in s.lower(), unique_list))
    return jsonify(unique_list)
    # return jsonify(list(sdf.display_name.unique()))


@app.route("/instruments")
def list_instruments():
    unique_inst = visualocean.instruments()
    f = request.args.get('filter')
    if (f):
        lf = f.lower()
        unique_inst = list(filter(lambda s: lf in s.lower(), unique_inst))
    return jsonify(unique_inst)

@app.route("/nodes")
def list_nodes():
    unique_nodes = visualocean.nodes()
    f = request.args.get('filter')
    if (f):
        lf = f.lower()
        unique_nodes = list(filter(lambda s: lf in s.lower(), unique_nodes))
    return jsonify(unique_nodes)

@app.route("/sites")
def list_sites():
    unique_sites = visualocean.sites()
    f = request.args.get('filter')
    if (f):
        lf = f.lower()
        unique_sites = list(filter(lambda s: lf in s.lower(), unique_sites))
    return jsonify(unique_sites)

@app.route("/regions")
def list_regions():
    unique_regions = visualocean.regions()
    f = request.args.get('filter')
    if (f):
        lf = f.lower()
        unique_regions = list(filter(lambda s: lf in s.lower(), unique_regions))
    return jsonify(unique_regions)

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
