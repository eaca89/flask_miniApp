from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# the pages of our website
@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["jack", "sarah", "tom"])

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin")
# def admin():
#     # return redirect(url_for("home"))
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()