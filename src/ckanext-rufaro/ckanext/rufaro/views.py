from flask import Blueprint


rufaro = Blueprint(
    "rufaro", __name__)


def page():
    return "Hello, rufaro!"


rufaro.add_url_rule(
    "/rufaro/page", view_func=page)


def get_blueprints():
    return [rufaro]
