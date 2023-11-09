from flask import Flask
from os import environ
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/login', methods=['GET'])
def login():

    return "Success", 200
  
@app.route('/secret', methods=['GET'])
def secret():
  with open('/app/secret', 'r') as f:
    secret=f.readline()
  return {
     "secret": secret
  }

@app.errorhandler(404) 
  
def not_found(e): 
  
  return "nothing here"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)