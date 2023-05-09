from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)

### GREET 

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

### CALC 

@app.route("/add")
def do_add():
    """Add a and b """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a + b

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a - b

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a * b

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a / b

    return str(result)

### CALC TWO

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<sign>")
def do_math(sign):
    """Solve for a <sign> b """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[sign](a, b)

    return str(result)