#!/usr/bin/env python3.6
from user import User
from credential import Credential
import string
import random
import sys 


def create_user(fname,lname,cpw,fpw):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,cpw,fpw)
    return new_user

def create_credential(acc_name,password):
    '''
    function to create a new credential
    '''
    new_credential=Credential(acc_name,password)
    return new_credential

def login_users(user):
    '''
    function to login user 
    '''
    user.login_user()

def save_credentials(credential):
    '''
    function to login user 
    '''
    credential.save_credential()

def del_credentials(credential):
    '''
    function to delete delete credentials
    '''
    credential.delete_credential()

def find_credential(name):
    '''
    function that finds a credential by name and returns the password
    '''
    return Credential.find_by_name(name)  

def display_credentials():
    '''function that returns all saved credentials
    '''
    return Credential.display_credentials()

def check_existing_credentials(name):
    '''
     Function that check if a credential exists with that account name and return a Boolean
    '''
    return Credential.credential_exist(name)


def main():
    print("Welcome to the Password Locker Application.")
    print('\n')
   
    print("Enter the First Name")
    print("-"*50)
    f_name=input()

    print("Enter the Last name")
    print("-"*50)
    l_name = input()

    print(f"Hello {f_name}  {l_name}. To continue you have to create a password and confirm it!")
    print('\n')


    print("Create Password")
    print("-"*50)
    cr_pw = input()

    print("Confirm Password")
    print("-"*50)
    fi_pw = input()

    login_users(create_user(f_name,l_name,cr_pw,fi_pw)) 

    if cr_pw == fi_pw:
        print(f"The account for {f_name}  {l_name}  successfully created ")
        print('\n')
    else:
        print(f"password {cr_pw} or {fi_pw} incorrect. Next time , Please confirm the password correctly.")  
        sys.exit()
    print("Use these short codes: lg - login "," ex - exit the app")  

    short_code=input().lower()

    if short_code == 'lg': 
        print("Let us  login to our account")
        print('\n')
        print("*"*50)
        print("Enter your first name (The name must be the same to the as the first name you entered previously ):")
        print('*'*50)
        print('\n')
        print("Enter the first name")
        print("-"*50)
        login_name=input()
        print("Enter the password")
        print("-"*50)
        passw=input()
    
        if fi_pw==passw and f_name==login_name:
            print("You are successfully logged into your account")
            print('\n')
        else:
            print(f"password: {passw} or name: {login_name} incorrect. Next time , Please confirm the password correctly.")  
            sys.exit()   
    elif short_code=='ex':
        print("Bye .......")
        sys.exit()

    while True:
        print("Use these short codes: ca - create a new account"," dc - display created accounts ", "del - to delete account"," ex - exit app")    
        
        short_code=input().lower()

        if short_code == 'ca':  
            print("Create a new Password")
            print("-"*50)

            print("Account name")
            print("-"*50)
            account_name=input()

            print("password")
            print("-"*50)
            password=input()

            save_credentials(create_credential(account_name,password))
            print('\n')
            print(f"The new Password for {account_name} : {password} created")
            print('\n') 

        elif short_code=='dc':
            if display_credentials():
                print("here is a list of all your accounts")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.account_name} {credential.password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')


        elif short_code == 'del':
            print("enter name of the account you want to delete")
            search_name=input()

            if check_existing_credentials(search_name):
                Credential =find_credential(search_name) 
                del_credentials(Credential)
                print(f"The {Credential.account_name} Account is deleted")
                print('\n')

                print("credential and password deleted")
            else:
                print("account name does not exist")  


        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()


    
