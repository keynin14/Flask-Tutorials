from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"


@app.route('/hello', methods=['GET', 'POST', 'PUT'])
def hello():
    if request.method == 'POST':
        return "Hello, POST request!\n"
    elif request.method == 'GET':
        return "Hello, GET request!\n"
    else:
        return "You will never see this message\n"
    return "Hello, World!"

@app.route('/greet/<name>') #If I write http://127.0.0.1:5555/greet/Kenan, I'll see Hello Kenan
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>') #int: typecasting
def add(number1, number2):
    
    return f"{number1}+{number2}={number1+number2}" #If I write http://127.0.0.1:5555/add/10/20, I'll se 10+20=1020 because ý didn't do typecasting.

@app.route('/handle_url_parameters')
def handle_params():
    #return str(request.args)
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name=request.args.get('name')
        return f'{greeting}, {name}' #we can see Hello, Kenan
    else:
        return 'Some parameters are missing'



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)

     