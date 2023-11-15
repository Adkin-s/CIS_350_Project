import databaseHelpers as db
import chatbot as cb
import login_screen

'''
#UserData test. - Failed

testuser = db.UserData("funnyman@sharklasers.com")
testuser.create_user()
print(testuser.get_user())
'''

'''
#Authentication test. - Passed

auth.signup("funnyman@sharklasers.com", "funnyman")
auth.login("funnyman@sharklasers.com", "funnyman")
auth.reset_password("funnyman@sharklasers.com")
'''

class app():

    def __init__(self) -> None:
        #self.run = True
        self.userInput = ""
        self.personas = {
            "Snarky" : cb.Persona("Snarky", "Your name is 'Mr. Snarky'. You are a mean, snarky, and passive-agressive assistant.", [{}]),
            "Kind" : cb.Persona("Kind", "Your name is 'Mr. Kind'. You are a nice, friendly, and helpful assistant.", [{}]),
            "Silly" : cb.Persona("Silly", "Your name is 'Mr. Silly'. You are a silly, funny, and playful assistant.", [{}]),
            "Serious" : cb.Persona("Serious", "Your name is 'Mr. Serious'. You are a professional, serious, and formal assistant.", [{}])
            }
        self.currentPersona = self.personas["Snarky"] #Defaults to Snarky

        #Opens the login screen upon startup.
        self.authwindow = login_screen.login_screen(self)

if __name__ == "__main__":
    app = app()