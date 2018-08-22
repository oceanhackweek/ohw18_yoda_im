import sys
import json
import requests
import pandas as pd
from flask import Flask, request, abort, jsonify, send_file, Response

base_url = "http://ooi.visualocean.net"

app = Flask(__name__)




@app.route("/")
def hello():
    return "hello world"

@app.route("/products")
def list_data_products():
    params = requests.get("{}/parameters.json".format(base_url)).json()
    df = pd.DataFrame.from_records(params['data'])
    sdf = df[df.data_product_type == 'Science Data']
    all_params = list(sdf['display_name'].dropna().values) + list(sdf['name'].dropna().values) + list(sdf['standard_name'].dropna().values)
    unique_list = sorted(list(set(all_params)))
    return jsonify(unique_list)
    # return jsonify(list(sdf.display_name.unique()))
    


if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
