from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Piotr Zacha',
        'title': 'Post 1',
        'content': 'Content 1',
        'date': '02.12.2019'
    },
    {
        'author': 'Jake Doe',
        'title': 'Post 2',
        'content': 'Content 2',
        'date': '03.12.2019'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)
