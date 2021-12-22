from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encryption", methods=['GET'])
def encryption():
    return render_template("encryption.html")


@app.route("/result", methods=['POST'])
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=True)
