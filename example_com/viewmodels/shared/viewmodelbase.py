# Imports
import flask
from flask import Request
from flask_login import current_user
from typing import Optional
# Custom Imports
from infrastructure import request_dict


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create("")

        self.error: Optional[str] = None
