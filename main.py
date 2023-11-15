import authHelpers as auth
import databaseHelpers as db
import chatbot as cb

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
        self.run = True
        self.userInput = ""
        self.personas = {
            "Snarky" : cb.Persona("Snarky", "Your name is 'Mr. Snarky'. You are a mean, snarky, and passive-agressive assistant.", [{}]),
            "Kind" : cb.Persona("Kind", "Your name is 'Mr. Kind'. You are a nice, friendly, and helpful assistant.", [{}]),
            "Silly" : cb.Persona("Silly", "Your name is 'Mr. Silly'. You are a silly, funny, and playful assistant.", [{}]),
            "Serious" : cb.Persona("Serious", "Your name is 'Mr. Serious'. You are a professional, serious, and formal assistant.", [{}])
            }
        self.currentPersona = self.personas["Snarky"] #Defaults to Snarky

        if self.authWindow():
            self.chatWindow()

    def authWindow(self) -> bool:
        #TODO show auth window
        return auth.login("email", "password")  #TODO change this to take input from the GUI, REMEMBER NO PLAINTEXT/STORING PASSWORDS!!! (think functional programming)
    
    def chatWindow(self) -> None:
        #TODO show chat window

        while True: #FIXME: see below. Need GUI to implement this
            #If button press, quit()

            userinput = input("Ask " + self.currentPersona.name + " something:")  #TODO change this to take input from the GUIturn str(self.currentPersona.name + ": " + self.currentPersona.messageHistory[-1])
            print("User: " + userinput) #TODO change this to print to the GUI
            print(self.currentPersona.name + ': ' + self.currentPersona.prompt(userinput)) #TODO change this to print to the GUI

if __name__ == "__main__":
    app = app()