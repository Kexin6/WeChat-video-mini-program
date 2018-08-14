'''
    一段小程序
'''

account= 'cassie'
password = '123456'

print("Please enter account: ")
userAccount = input()
print("Please enter password:")
userPassword = input()

if account == userAccount and password == userPassword :
    print("Success")
elif userAccount != account :
    print("Account DNE")
else:
    print("Wrong password")
