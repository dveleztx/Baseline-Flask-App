#!/usr/bin/python3
#######################################################################################################################
# Program     : app.py
# Author      : David Velez
# Date        : 09/19/2020
# Description : Template Flask App
#######################################################################################################################

# Imports
from flask import Flask
from flask_login import LoginManager
# Custom Libraries
from data import db_session
from services import user_service

app = Flask(__name__)


# Main
def main():
    header()
    setup_db()
    register_blueprints()
    init_login_manager()
    app.run(debug=True, host="127.0.0.1")


def header():
    print("-" * 36)
    print("         Template Flask App")
    print("-" * 36)
    print()


def setup_db():
    db_session.global_init()


def register_blueprints():
    from views.home import home_view
    from views.account import account_view

    app.register_blueprint(home_view.blueprint)
    app.register_blueprint(account_view.blueprint)


def init_login_manager():
    app.secret_key = "mytemplatekeyneedstobestronger"
    lm = LoginManager()
    lm.login_view = "/account/login"
    lm.init_app(app)

    @lm.user_loader
    def load_user(user_id):
        uid = user_service.find_user_by_id(user_id)
        return uid


# Initialize
if __name__ == "__main__":
    main()
