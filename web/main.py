# -*- coding: utf-8 -*-
from flask import Flask, escape, request, jsonify, render_template
import os

app = Flask(__name__, static_folder = 'src')


@app.route('/')
def hello():
    os.system("cp /root/data/analyze.jpg /root/web/src/")
    return app.send_static_file('index.html')
