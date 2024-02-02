from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('default.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/features')
def fea():
    return render_template('features.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)