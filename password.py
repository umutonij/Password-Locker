#!/usr/bin/env python3.6
import pyperclip
from user import User
from credential import Credential

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(password):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_password(password)

def check_existing_users(password):
    '''
    Function that check if a user exists with that password and user a Boolean
    '''
    return User.user_exist(password)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
    print(' ')
    print("Hello! Welcome to Password Locker")
    # user_name = input("use these short code")

    # print(f"Hello {user_name}. what would you like to do?")
    # print('\n')

    while True:
                    print('')
                    print("-"*60)
                    print("Use these short codes : \n ca-Create an Account \n li-Log In \n ex-exit the user list  \n dc - display users \n del - delete created account")

                    short_code = input("Enter a choice").lower()

                    if short_code == 'ca':
                            print("New User")
                            print("-"*50)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            password = input()


                            save_users(create_user(f_name,l_name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Account Created for: {f_name} {l_name} {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')
                    elif short_code == 'dl':

                            if display_users():
                                    print("Delete a list of all your users")
                                    print('\n')

                                    for user in delete_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')                    

                    elif short_code == 'li':

                            print("To login, enter your account details:")

                            user_name = input('Enter your first name - ')
                            password = str(input())
                            user_exists = verify_user(user_name,password)
                            if user_exists == user_name:
                                print(" ")
                                print(f'Welcome {user_name}. Please choose an option to continue.')

                            elif short_code == 'ex':
                                            print("Bye .......")
                                            break
                            else:
                                            print("I really didn't get that. Please use the short codes")




if __name__ == '__main__':
	    main()