from flask import Flask, request, render_template, jsonify
import config
import requests
import json

app = Flask(__name__)
app.config.from_object(config)

@app.route('/members')
def members():
    context = {
        'name':u'xianjun666', 'ph':u'010-2482-6368',
        'name1':u'hongxianjun', 'ph1':u'12341234',
        'name2':u'xianjun', 'ph2':u'12341234',
    }
    # members restapi call
    data
    return render_template('members_rest.html',**context)

@app.route('/notics')
def notics():
    res = requests.get('http://127.0.0.1:9000/notics_api', json={'order': 'all'})
    data = res.json()

    return render_template('notics.html', **data)


if __name__ == '__main__':
    app.run(port=8000)