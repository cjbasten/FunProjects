import re

passwordLength = re.compile(r'\w{8,}')
passwordUpper = re.compile(r'[A-Z]+')
passwordLower = re.compile(r'[a-z]+')
passwordNumber = re.compile(r'\d+')


def strongPassword(password):
    if passwordLength.search(password) == None:
        print('The password is too short')
        return False
    if passwordUpper.search(password) == None:
        print('The password needs at least one uppercase character.')
        return False
    if passwordLower.search(password) == None:
        print('The password needs at least one lowercase character.')
        return False
    if passwordNumber.search(password) == None:
        print('The password needs at least one number.')
        return False
    else:
        return True


password1 = input('What is the password?')
while strongPassword(password1) == False:
    password1 = input("Please enter a secure password.")
else:
    print("This password is secure.")
