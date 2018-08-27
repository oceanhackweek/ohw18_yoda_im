from gevent import monkey; monkey.patch_all()
import sys
import json
import requests
import pandas as pd
import numpy as np
# from flask_cors import CORS
from flask import Flask, request, abort, jsonify, send_file, Response
from visualocean import VisualOcean, merge_name_rd
from typing import List
#from inst_data import instData
from inst_data import get_data

base_url = "http://ooi.visualocean.net"

app = Flask(__name__, static_url_path='')
# CORS(app)
visualocean = VisualOcean(base_url)


def filtered(m: str, values: List[str]) -> List[str]:
    """Filter a list to strings that contain a substring"""
    n = m.lower()
    return list(filter(lambda s: n in s.lower(), values))


@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route("/products")
def list_data_products():
    unique_values = visualocean.products()
    f = request.args.get('filter')
    if f:
        unique_values = filtered(f, unique_values)
    return jsonify(unique_values)

@app.route("/ids_array")
def search_on_array():
    unique_IDs = visualocean.ids_at_array()
    f = request.args.get('filter')
    if f:
        unique_IDs = filtered(f, unique_IDs)
    return jsonify(unique_IDs)

    
@app.route("/products/id/<name>")
def find_product_id(name):
    pid = visualocean.parameter_id(name)
    if pid == -1:
        abort(404)
    else:
        return jsonify({"id": pid, "requested_name": name})

@app.route("/streams/<parameter_id>")
def find_stream_names(parameter_id):
    names = visualocean.stream_names(parameter_id)
    if len(names) == 0:
        abort(404)
    else:
        return jsonify(names)

@app.route("/reference_designator/<stream_name>")
def find_reference_designator(stream_name: str):
    rds = visualocean.reference_designator(stream_name)
    if len(rds) == 0:
        abort(404)
    else:
        return jsonify(rds)

@app.route("/deployments/<reference_designator>")
def find_deployments(reference_designator):
    ds = visualocean.deployments(reference_designator)
    if len(ds) == 0:
        abort(404)
    else:
        return jsonify(ds)

@app.route("/deployments/find/<param_name>")
def find_deployments_by_param(param_name):
    ds = visualocean.deployments_by_param_name(param_name)
    if len(ds) == 0:
        abort(404)
    else:
        return jsonify(ds)


@app.route("/instruments")
def list_instruments():
    unique_values = visualocean.instruments()
    f = request.args.get('filter')
    if f:
        unique_values = filtered(f, unique_values)
    return jsonify(unique_values)


@app.route("/nodes")
def list_nodes():
    unique_values = visualocean.nodes()
    f = request.args.get('filter')
    if f:
        unique_values = filtered(f, unique_values)
    return jsonify(unique_values)


@app.route("/sites")
def list_sites():
    unique_values = visualocean.sites()
    f = request.args.get('filter')
    if f:
        unique_values = filtered(f, unique_values)
    return jsonify(unique_values)

@app.route("/regions")
def list_regions():
    unique_values = visualocean.regions()
    f = request.args.get('filter')
    if f:
        unique_values = filtered(f, unique_values)
    return jsonify(unique_values)


@app.route("/data/<instrument_rd>")
def get_inst_data(instrument_rd):
    username = request.args.get('username')
    token = request.args.get('token')
    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')
    refID = instrument_rd
    data = get_data(username, token, refID, begin_date, end_date)
    return jsonify(data)

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
