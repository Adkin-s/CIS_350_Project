import database as db

'''
#UserData test. - Failed

testuser = db.UserData("funnyman@sharklasers.com")
testuser.create_user()
print(testuser.get_user())
'''

'''
#Authentication test. - Passed

testlogin = db.Authentication("funnyman@sharklasers.com", "funnyman")
testlogin.signup()
testlogin.login()
testlogin.reset_password()
'''
