from flask import Flask, render_template, redirect, request, url_for
import random
import string

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Tools Page
@app.route('/tools')
def tools():
    return render_template('tools.html')

# Password Generator Page
@app.route('/password-generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_lowercase = 'use_lowercase' in request.form
        use_uppercase = 'use_uppercase' in request.form
        use_digits = 'use_digits' in request.form
        use_special_characters = 'use_special_characters' in request.form

        password = generate_random_password(length, use_lowercase, use_uppercase, use_digits, use_special_characters)
        return render_template('password-generator.html', password=password, length=length, use_lowercase=use_lowercase, use_uppercase=use_uppercase, use_digits=use_digits, use_special_characters=use_special_characters)

    password = generate_random_password(12, 1, 1, 1, 1)
    return render_template('password-generator.html', password=password, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_characters=True)


def generate_random_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_characters=True):
    characters = string.ascii_lowercase if use_lowercase else ''
    characters += string.ascii_uppercase if use_uppercase else ''
    characters += string.digits if use_digits else ''
    characters += string.punctuation if use_special_characters else ''

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

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
