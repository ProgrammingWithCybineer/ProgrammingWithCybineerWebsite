from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/consultation")
def consultation():
    return render_template("consultation.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/services")
def services():
    return render_template("services.html")





if __name__ == '__main__':
    app.run(debug=True)