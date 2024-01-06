from flask import Flask, render_template, redirect

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Twitter redirect
@app.route('/twitter')
def twitter():
    return redirect('https://twitter.com/barisozyurek1')

# 404 redirect
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
