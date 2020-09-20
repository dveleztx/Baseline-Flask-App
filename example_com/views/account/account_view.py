# Imports
from flask import Blueprint, render_template, redirect
from flask_login import login_user, login_required, current_user, logout_user
# Custom Imports
from services import user_service
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = Blueprint("account", __name__, template_folder="templates")


###############################################################################
# INDEX
###############################################################################
@blueprint.route("/account")
@login_required
def index():
    return render_template("account/account.html", name=current_user.name)


###############################################################################
# REGISTER
###############################################################################
@blueprint.route("/account/register", methods=["GET"])
def register_get():
    return render_template("account/register.html")


@blueprint.route("/account/register", methods=["POST"])
def register_post():

    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return render_template("account/register.html",
                               name=vm.name,
                               username=vm.username,
                               email=vm.email,
                               error=vm.error)

    user = user_service.create_user(vm.name, vm.username, vm.email, vm.password)
    if not user:
        vm.error = "The account could not be created."
        return render_template("account/register.html",
                               error=vm.error)

    return redirect("/account/login")


###############################################################################
# LOGIN
###############################################################################
@blueprint.route("/account/login", methods=["GET"])
def login_get():

    return render_template("account/login.html")


@blueprint.route("/account/login", methods=["POST"])
def login_post():
    vm = LoginViewModel()
    vm.validate()

    if vm.error:
        return render_template("account/login.html",
                               error=vm.error)

    user = user_service.login_user(vm.username, vm.password)
    if not user:
        return render_template("account/login.html",
                               username=vm.username,
                               error="The account does not exist or the "
                                     "password is wrong.")

    # Validate the user
    login_user(user)

    return redirect("/account")


###############################################################################
# LOGOUT
###############################################################################
@blueprint.route("/account/logout")
@login_required
def logout():
    logout_user()
    return redirect("/account/login")
