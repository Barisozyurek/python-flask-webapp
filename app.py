from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Twitter redirect
@app.route('/twitter')
def twitter():
    return redirect('https://twitter.com/barisozyurek1')

# LinkedIn redirect
@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/barisozyurek/')

# 404 redirect
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
