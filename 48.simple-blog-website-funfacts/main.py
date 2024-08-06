from flask import Flask, render_template
import json

app = Flask(__name__)

with open("posts_content.json", 'r') as file:
    all_posts = json.load(file)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:index>')
def post(index):
    post_ = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            post_ = blog_post
    return render_template("post.html", post=post_)


if __name__ == "__main__":
    app.run(debug=True)
