from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def hello():

    return "<h1>Hey You!</h1>"

@app.route("/home")
def home():

    return render_template('home.html')

@app.route("/about")
def about():

    return render_template('about.html')

@app.route("/contact")
def contact():

    return "<h2> Contact us ASAP </h2>"

@app.route("/managers")
def managers():

    return "<li> <ul> Winnie Nyambura </ul> <br> <ul> Everlyn Wanini </ul> </li>"

@app.route("/services")
def services():

    return "<b> We provide the best services</b>"

@app.route("/tips")
def tips():
    return "Some of the best tips include"

if __name__ =='__main__':

    app.run(debug=True)