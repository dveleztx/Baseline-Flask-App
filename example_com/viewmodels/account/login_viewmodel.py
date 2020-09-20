# Custom Imports
from viewmodels.shared.viewmodelbase import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.username = self.request_dict.username.strip().lower()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.username:
            self.error = "Please enter a username."
        elif not self.password:
            self.error = "Please enter a password."
