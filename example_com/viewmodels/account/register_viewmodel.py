# Custom Imports
from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.username = self.request_dict.username.strip().lower()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name:
            self.error = "Please enter your name."
        elif not self.username:
            self.error = "Please enter a username."
        elif not self.email:
            self.error = "Please enter your email."
        elif not self.password:
            self.error = "Please enter a password."
        elif len(self.password) < 10:
            self.error = "Please enter a password with 10 characters or more."
        elif user_service.find_user_by_email(self.email):
            self.error = "A user with that email address already exists."
