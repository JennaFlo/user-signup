from flask import Flask, request, render_template, url_for, redirect
import re
app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route('/')
def index():
    return render_template('index.html')

def username_test(username):
    if username == "":
        #return: "You forgot to enter a username"
        return "blank_error"
    elif re.match("^[a-zA-Z0-9]{3,20}$", username) == None:
        #return "The username must have between 3 and 20 characters, and no special characters"
        return "format_error"
    else:
        return ""
def password_test(password):
    if password == "":
        return "blank_error"
    elif re.match("^[a-zA-Z0-9]{3,20}$", password) == None:
        return "format_error"
    else:
        return ""
def verify_password_test(verify_password, password):
    if verify_password == "":
        return "blank_error"
    elif verify_password != password:
        return "format_error"
    else:
        return ""
def email_test(email):
    if email == "":
        return ""
    if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+\.[a-zA-Z]{3,20}", email) == None:
        return "format_error"
    else:
        return ""

@app.route('/', methods=['GET','POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password_entered")
    verify_password = request.form.get("verifypassword_entered")
    email = request.form.get("email_input")
    u_test = username_test(username) 
    p_test = password_test(password)
    pv_test = verify_password_test(verify_password, password)
    e_test = email_test(email)
    if u_test != "" or p_test != "" or pv_test !="" or e_test != "":
        return render_template('index.html', username = username, email = email,  username_error = u_test, password_error = p_test, verify_error = pv_test, email_error = e_test)

    #error = None
    #if request.method == 'POST':
    #    if request.form['username'] ('^[a-zA-0-9])') or request.form['password'] != 'admin' or request.form['verify_password'] != 'password':
    #        error = 'Invalid Credentials. Please try again.'
    #    else:
            #return redirect(url_for('welcome'))
    else:

        return redirect ("/welcome?name=" + username)
   
@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html', name = request.args.get("name"))





app.run()