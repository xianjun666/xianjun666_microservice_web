#!flask/bin/python
from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)
json_data = [{
            'id': 1,
            'title': u'Buy something',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        }]


@app.route('/')
def get_tasks():
    return render_template('restfulapi.html', **{'json_data': json_data})


if __name__ == '__main__':
    app.run(debug=True)