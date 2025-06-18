from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required

index_bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
    static_folder="src",
)


@index_bp.route("/")
def index():
    return render_template("index.html")


@index_bp.route("/login")
def login():
    return render_template("login.html")


@index_bp.route("/register")
def register():
    return render_template("register.html")


@index_bp.route("/showcase")
def showcase():
    return render_template("showcase.html")


@index_bp.route("/function")
@jwt_required()
def function():
    return render_template("function.html")
