import sys
import json
import requests
import pandas as pd
from flask import Flask, request, abort, jsonify, send_file, Response
from visualocean import VisualOcean

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)
visual_ocean = VisualOcean(base_url)


def string_match(a, b): 
  return a in b

@app.route("/")
def hello():
    return "hello world"

@app.route("/products")
def list_data_products():
    unique_list = visual_ocean.products()
    f = request.args.get('filter')
    if (f):
      lf = f.lower()
      unique_list = list(filter(lambda s: lf in s.lower(), unique_list))
    return jsonify(unique_list)
    # return jsonify(list(sdf.display_name.unique()))
    


if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
