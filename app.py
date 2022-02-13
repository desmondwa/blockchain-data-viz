from flask import Flask
import psql 
# from env import API_KEY

app = Flask(__name__)

@app.route('/')
def browser():
    return psql.load_data(public.daily_gas_used)