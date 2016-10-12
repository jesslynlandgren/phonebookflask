from flask import Flask, render_template

app = Flask('HelloApp')

@app.route('/')

def helloWorld():
    return render_template(
    'index.html',
    title='HELLOOOOOO WORLLLLLLD',
    ok = 'OK!!',
    hello = 'hi hi hi hi hi'
    )

if __name__ == '__main__':
    app.run(debug=True)
