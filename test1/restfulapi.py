#encoding: utf-8

from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}, 201, {'Etag': 'some'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()

