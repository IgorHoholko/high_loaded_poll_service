from flask import Flask, escape, request, jsonify
import psycopg2
from sqlalchemy import create_engine

from database.settings import SETTINGS_DEFAULT

app = Flask(__name__)

conn_string = "host={} dbname={} user={}".format(
    SETTINGS_DEFAULT['host'], SETTINGS_DEFAULT['dbname'], SETTINGS_DEFAULT['user']
)

conn = psycopg2.connect(conn_string)

engine = create_engine("postgresql://{}@{}:5432/{}".format(
    SETTINGS_DEFAULT['host'], SETTINGS_DEFAULT['dbname'], SETTINGS_DEFAULT['user']
))



@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'<h1> Hello, {escape(name)}! !!<h1>'


@app.route('/pool', methods=["POST"])
def pool():
    content = request.get_json()
    print(content)
    return jsonify(content)