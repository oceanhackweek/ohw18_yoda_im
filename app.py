import sys
import json
from flask import Flask, request, abort, jsonify, send_file, Response

app = Flask(__name__)

@app.route("/")
def hello():
  return "hello world"


if __name__ == "__main__":
  port = int(sys.argv[1])
  app.run(host="0.0.0.0", port=port, debug=True, threaded=True)