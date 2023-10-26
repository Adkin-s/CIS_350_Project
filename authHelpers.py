import pyrebase
import warnings
from firebaseConfig import firebase

auth = firebase.auth()

def warn(message):
    warnings.warn(message)

def login(self, email, _password):
    try:
        auth.sign_in_with_email_and_password(email, _password)
        return True
    except:
        warn("Invalid email or password.")
        return False

def signup(self, email, _password):
    try:
        auth.create_user_with_email_and_password(email, _password)
        return True
    except:
        warn("Email already exists.")
        return False

def reset_password(self, email):
    try:
        auth.send_password_reset_email(email)
        return True
    except:
        warn("Email does not exist.")
        return False