import bcrypt
import os
import maskpass  # to hide the password
from getpass import getpass


password = b'bossy'  # it gets encoded


# check if hashed password txt exists
# if not, make it and store the pass there
# exists then just verify the password and carry on

def password_check(password):
    if os.path.exists('./hashed-pw.txt'):
        with open('./hashed-pw.txt', 'r') as f:
            pass_hash = str.encode(f.readline().strip())
            # pass_hash = bytes(pass_hash)
            print(f'passhash found, it is: {pass_hash}')
            if bcrypt.checkpw(password, pass_hash):
                return True
            else:
                return False
    else:
        with open('./hashed-pw.txt', 'w') as f:
            pass_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
            f.write(pass_hash)
            return 'Password was not found, file was created for new password'



# password =  getpass.getpass(prompt='Your password is: ')
def say_hi():
    print('hi')



# password = input('what is the password you want to hash:')

