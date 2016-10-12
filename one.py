from flask import Flask

app = Flask('HelloApp')

@app.route('/')

def helloWorld():
    return '<span>Hello World!</span>'

if __name__ == '__main__':
    app.run(debug=True)
