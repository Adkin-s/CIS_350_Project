import pyrebase
import warnings

firebaseConfig = {
    'apiKey': "AIzaSyCXRXtK07m6wmrX4ZPhzYXevo_Dv2MCENI",
    'authDomain': "snrk-a6050.firebaseapp.com",
    'databaseURL': "https://snrk-a6050-default-rtdb.firebaseio.com",
    'projectId': "snrk-a6050",
    'storageBucket': "snrk-a6050.appspot.com",
    'messagingSenderId': "227455950615",
    'appId': "1:227455950615:web:ec7caa4f3a41168c936152"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()

def warn(message):
    warnings.warn(message)

class Authentication():
    def __init__(self, email, _password):
        self.email = email
        self._password = _password

    def login(self):
        try:
            auth.sign_in_with_email_and_password(self.email, self._password)
            return True
        except:
            warn("Invalid email or password.")
            return False

    def signup(self):
        try:
            auth.create_user_with_email_and_password(self.email, self._password)
            return True
        except:
            warn("Email already exists.")
            return False
    
    def reset_password(self):
        try:
            auth.send_password_reset_email(self.email)
            return True
        except:
            warn("Email does not exist.")
            return False
        
class UserData():
    def __init__(self, email):
        self.email = email
        self.user = db.child("users").child(self.email)
        #Database structure: db* -> users* -> email -> conversations* -> conversation_id -> message_id -> message
        # * = unchanging node

        #TODO create message_id and conversation_id generator here, or in a separate file.

    def create_user(self):
        if self.user.get().val() == None:
            self.user.set(self.email)
            return True
        else:
            warn("User already exists.")
            return False
        
    def get_user(self):
        if self.user.get().val() != None:
            return self.user.get().val()
        else:
            warn("User does not exist.")
            return False
        
    def create_conversation(self, conversation_id):
        new_conversation = self.user.child("conversations").child(conversation_id)

        if new_conversation.get().val() == None:
            new_conversation.set(conversation_id)
            return True
        else:
            warn("Conversation already exists")
            return False
    
    def get_conversation(self, conversation_id):
        conversation = self.user.child("conversations").child(conversation_id).get().val()

        if conversation != None:
            return conversation
        else:
            warn("Conversation does not exist.")
            return False

    def add_message(self, conversation_id, message_id, message):
        new_message = self.user.child(conversation_id).child(message_id)

        if new_message.get().val() == None:
            new_message.set(message)
            return True
        else:
            warn("Message already exists.")
            return False
        
    #TODO add function to edit message.
        
    def get_message(self, conversation_id, message_id):
        return self.user.child("conversations").child(conversation_id).child("message_id").child(message_id).child("message").get().val()
    
    def get_all_messages(self, conversation_id):
        messages = []

        if self.user.child("conversations").child(conversation_id).get().val() != None:
            for i in self.user.child("conversations").child(conversation_id).get().val():
                messages.append(i)
        
            #TODO sort messages by time sent. Depends on message ID format.
            return messages

        else:
            warn("Conversation does not exist.")
            return False
    
    def delete_message(self, conversation_id, message_id):
        if self.user.child("conversations").child(conversation_id).child(message_id).get().val() != None:
            self.user.child("conversations").child(conversation_id).child(message_id).remove()
            return True
        else:
            warn("Message does not exist.")
            return False
    
    def delete_all_messages(self, conversation_id):
        if self.user.child("conversations").child(conversation_id).get().val() != None:
            self.user.child("conversations").child(conversation_id).remove()
            return True
        else:
            warn("Conversation does not exist, or has no messages.")
            return False

    def delete_conversation(self, conversation_id):
        if self.user.child("conversations").child(conversation_id).get().val() != None:
            self.user.child("conversations").child(conversation_id).remove()
            return True
        else:
            warn("Conversation does not exist.")
            return False
    
    def delete_all_conversations(self):
        if self.user.child("conversations").get().val() != None:
            self.user.child("conversations").remove()
            return True
        else:
            warn("User does not exist, or has no conversations.")
            return False

    def delete_user(self):
        if self.user.get().val() != None:
            self.user.remove()
            return True
        else:
            warn("User does not exist.")
            return False
    