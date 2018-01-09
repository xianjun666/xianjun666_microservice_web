#!flask/bin/python
from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)
tasks = [
        {
            'id': 1,
            'title': u'Buy something',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python turorial on the web',
            'done': False
        }
    ]
json1 = json.dumps(tasks)
data = json.loads(json1)


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)

