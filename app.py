from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


def convert_celsius_to_fahrenheit(celsius):
    """Convert to celsius from fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/f/<celsius>')
def f(celsius=0.0):
    return str(convert_celsius_to_fahrenheit(celsius))


if __name__ == '__main__':
    app.run()
