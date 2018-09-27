from flask import Flask, request, render_template
app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route('/')
def index():
    return render_template('index.html')



#@app.route('/', methods=['POST','GET'])
# about():





app.run()