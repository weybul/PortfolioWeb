from flask import Flask, redirect, render_template

# creating an instance of our Flask class
app = Flask(__name__)

# define routes
@app.route("/")
def default_route():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

# starts our Flask development server
if __name__=="__main__":
    app.run(debug=True)
