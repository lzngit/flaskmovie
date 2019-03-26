from flask import render_template, redirect, url_for

from . import home


#详情页面
@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


@home.route("/register/")
def register():
    return render_template("home/register.html")


@home.route("/user/")
def user():
    return render_template("home/user.html")

@home.route("/updatepwd/")
def updatepwd():
    return render_template("home/updatepwd.html")


@home.route("/comments/")
def comments():
    return render_template("home/comments.html")


@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")


@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")


#电影页面
@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

#搜索页面
@home.route("/search/")
def search():
    return render_template("home/search.html")

#详情页面
@home.route("/play/")
def play():
    return render_template("home/play.html")


