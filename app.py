import sys
import json
import requests
import pandas as pd
import numpy as np
from flask import Flask, request, abort, jsonify, send_file, Response
from visualocean import VisualOcean, merge_name_rd

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)
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
    return jsonify(unique_inst)

@app.route("/nodes")
def list_nodes():
    unique_nodes = visualocean.nodes()
    return jsonify(unique_nodes)

@app.route("/sites")
def list_sites():
    unique_sites = visualocean.sites()
    return jsonify(unique_sites)

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
