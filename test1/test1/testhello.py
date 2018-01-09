from flask import Flask


app = Flask(__name__)


@app.route('/')
def test():
    return 'hello,world'


if __name__ == '__main__':
    app.run(port=1130)