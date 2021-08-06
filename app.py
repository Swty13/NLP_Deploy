from flask import Flask, request, jsonify, render_template
from predict import predict_category

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/category', methods=['POST'])
def category():
    if request.method == 'POST':

        text = request.form['originalText']

        category= predict_category(text)

        return render_template('result.html',
                               category=category,
                               )


if __name__ == '__main__':
    app.run(debug=True)