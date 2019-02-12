#!/usr/bin/env python3.6
import pyperclip
from user import User
from credential import Credential

def create_user(fname,lname,email,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,email,password)
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