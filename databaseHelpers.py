from warnings import warn
from firebaseConfig import firebase

db = firebase.database()

#TODO Turn UserData class into helper functions.
#FIXME Maybe don't remove class, but only call it once upon logging in. Then use helper functions to access data.
    #Example logic: Init_app -> enter email, if email exists, create UserData object, else prompt to create a new user.

class UserData():
    def __init__(self, email):
        self.email = email
        self.user = db.child("users").child(self.email)
        #Database structure: db -> users : email -> conversations : conversation_id -> messages : message_id -> message : raw_str
        #TODO create message_id and conversation_id generator (conversation_id [persona_type][int], message_id [date][human_or_persona]).

    def create_user(self):
        if self.user.get().val() == None:
            self.user.push(self.email)
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
            new_conversation.push(conversation_id)
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
            new_message.push(message)
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
