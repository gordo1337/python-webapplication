from flask import Flask, render_template, url_for
app = Flask(__name__)
# Blog posts by users
post = [
    {
        'anon': 'Anon Nymous',
        'title' : 'post 1',
        'content': 'First post content',
        'date_posted': 'May 12, 2021'
    },
    {
        'anon': 'Anon non',
        'title' : 'post 2',
        'content': 'Second post content',
        'date_posted': 'May 12, 2021'
    }
]

# Homepage located /home
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post='posts')

#about page /about
@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)