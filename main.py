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
        #Opens the login screen upon startup.
        self.authwindow = login_screen.Window()

if __name__ == "__main__":
    app = app()