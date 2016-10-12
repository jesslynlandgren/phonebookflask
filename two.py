from flask import Flask, render_template

app = Flask('HelloApp')

@app.route('/')

def helloWorld():
    return render_template(
    'layout.html',
    title='HELLOOOOOO WORLLLLLLD',
    hello='Hello World!!!!!'
    )

if __name__ == '__main__':
    app.run(debug=True)
