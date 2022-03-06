from flask import Flask
import psql 
import pandas
import plotly.express as px

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

@app.route('/line')
def line():
   df = psql.load_data('public','daily_gas_used')
   fig = px.scatter(df, x="collected_for_day", y="gas_used")
   fig.show()
  

# connect to other datasources and compare w/
# plotly with flask + python viz or create csv + tableau 