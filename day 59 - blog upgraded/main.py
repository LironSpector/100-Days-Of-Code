from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = "lirontheprog@gmail.com"
# MY_PASSWORD = "programmer#1"
MY_PASSWORD = "ciexaniegletpvnu"



app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"{email_message}")


if __name__ == "__main__":
    app.run(debug=True)
