from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def bosh_sahifa():
    return render_template('index.html')


@app.route('/about')
def about_sahifa():
    return render_template('about.html')


@app.route('/greeting')
def greeting():

    params = request.args
    
    name = params.get('name', '')

    return render_template('greeting.html', name=name)

@app.route('/calc')
def calc():

    params = request.args

    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    operator = params.get('operator', '-')

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a / b
    elif operator == '*':
        result = a * b

    return render_template("calc.html", a=a, b=b, result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

