from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/input_name", methods=['POST'])
def insert():
    if request.method == "POST":
        username = request.form['username']
    return render_template('/menupage/menupage.html', name=username)



if __name__ == "__main__":
    app.run(debug=True)
