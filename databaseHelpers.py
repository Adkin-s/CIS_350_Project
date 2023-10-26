import pyrebase
import warnings
from firebaseConfig import firebase

db = firebase.database()

def warn(message):
    warnings.warn(message)

#TODO Turn UserData class into helper functions.
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
    