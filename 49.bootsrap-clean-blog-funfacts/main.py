import requests
from datetime import datetime
from notification_manager import NotificationManager
from flask import Flask, render_template, request

app = Flask(__name__)

blog_data = requests.get(url="https://api.npoint.io/153d97e51d3e49660d73").json()

def dates_manager(blog_data):
    """sort posts by date and prettify the date format, from format YYYY-MM-DD to DD BB YYYY, eg. 07 April 2024

    Args:
        blog_data (dict): json data with all blog posts and its content
    """
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, r'%Y-%m-%d')
        return date_obj.strftime(r'%d %B %Y')
    sorted_data = sorted(blog_data, key=lambda x: datetime.strptime(x['date_added'], r'%Y-%m-%d'), reverse=True)
    for item in sorted_data:
        item['date_added'] = format_date(item['date_added'])
    return sorted_data

all_posts = dates_manager(blog_data=blog_data)
del blog_data

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "message": request.form["message"]
        }
        nm = NotificationManager(data, "gabsdidit@icloud.com")
        nm.send_email()
        return render_template("contact.html", is_sent=True)
    return render_template("contact.html", is_sent=False)

@app.route('/post/<int:post_id>')
def post(post_id: int):
    post_ = None
    for blog_post in all_posts:
        if blog_post['id'] == post_id:
            post_ = blog_post
            return render_template('post.html', post_=post_)


if __name__ == "__main__":
    app.run(debug=True)
