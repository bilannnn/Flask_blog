from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'author': 'Jon Doe',
     'title': 'First post',
     'content': 'First post content',
     'date_posted': 'November 5, 2022'},

    {'author': 'Ivan Petriv',
     'title': 'Second post',
     'content': 'Second post content',
     'date_posted': 'November 5, 2022'}

]


@app.route('/')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(port=8888)
