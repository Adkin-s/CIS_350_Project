import authHelpers as auth
import databaseHelpers as db

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
