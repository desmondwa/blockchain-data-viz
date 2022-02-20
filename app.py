from flask import Flask
import psql 
import pandas
# from env import API_KEY

app = Flask(__name__)

# @app.route('/')
# def browser():
#     df = psql.load_data('public','daily_gas_used')
#     return "hello"

@app.route('/')
def browser():
   data = psql.load_data('public','daily_gas_used')
   json_data = data.to_json(orient='values')
   return json_data
  

# connect to other datasources and compare w/
# plotly with flask for python viz or create csv + tableau 