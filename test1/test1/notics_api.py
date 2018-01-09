from flask import Flask, request, jsonify
import json
import config

app = Flask(__name__)
app.config.from_object(config)

#api name : notics_api
#param dic for json: {'order': number or all}
@app.route('/notics_api', methods=['GET', 'POST'])
def notics_api():
    context = {}
    if not request.is_json:
        return 'empty data'

    data = request.json

    if data['order'] == 'all':
        #db call all members
        context = [
            {'name': 'xianjun661', 'ph': '010-2482-6361'},
            {'name': 'xianjun662', 'ph': '010-2482-6362'},
            {'name': 'xianjun663', 'ph': '010-2482-6363'}
        ]
    else:
        order = int(data.get('order'))
        # db_call for order number
        context = [
            {'name': 'yangun1', 'ph': '010-2482-6361'},
            {'name': 'yangun2', 'ph': '010-2482-6362'},
        ]

    return jsonify({'context': context})

if __name__ == '__main__':
    app.run(port=9000)