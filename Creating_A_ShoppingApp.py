print("Welcome to the Marketplace!")
login_dict = {'User1': {'password': 'userpassword', 'type': 'user'},
              'Admin1': {'password': 'adminpassword', 'type': 'admin'}}

username = input("Please enter your username ")
password = input("Please enter your password ")

# check if username in login dict
if username in login_dict.keys():
    # check if password is correct 
    if password == login_dict[username]['password']:
        print('Login Successful')
    # if password incorrect
    else:
        print('Bad Password')
# if username incorrect
else:
    print('Bad Username')
