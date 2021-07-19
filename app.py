from flask import Flask, Response
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info("/status")
    json = "{\"result\": \"OK - healthy\" }"
    return Response(json,mimetype ="application/json"),200

@app.route("/metrics")
def metrics():
    logging.info("/metrics")
    json = "{ \"data\": {\"UserCount\": \"140\", \"UserCountActive\": \"23\" }"
    return Response(json,mimetype ="application/json")

if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG, filename = 'app.log', format= '%(asctime)s, %(message)s endpoint was reached')
    app.run(host='0.0.0.0'),200
