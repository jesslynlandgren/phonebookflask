

from flask import Flask, request

app = Flask('HelloApp')

@app.route('/')
def hello():
    name = request.args.get('name', 'world')
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
