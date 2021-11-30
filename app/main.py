from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('main.html')


@app.route('/detail', methods = ['POST'])
def detail():
    res = request.form.to_dict()
    return render_template("detail.html", result = res)


@app.route('/result', methods = ['POST'])
def result():
    res = request.form.to_dict()
    return render_template("result.html", result = res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True, port = 80)
