from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>" #Heading

if __name__== '__main__': 
    app.run(host='0.0.0.0', debug=True) # This will run the Flask application on localhost at port 5000

# Running on http://127.0.0.1:5000 #LocalHost and Private IP Adress
# Running on http://192.168.1.103:5000 #
