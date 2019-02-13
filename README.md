# PASSWORD LOCKER

## Built By Jacqueline UMUTONI
## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories

These are the behaviours/features that the application implements for use by a user.

As a user I would like:

* To create an account with my details - log in and password.
* Store my existing login credentials.
* Create new account credentials in the application.
* To view my various account credentials and their passwords in the application.
* To delete a credentials account that I no longer need in the application.

## Specifications

Behaviour	Input	Output
Display codes for navigation	In terminal: $./password.py	Welcome, choose an option: ca-Create Account, lg-Log In, ex-Exit
Display prompt for creating an account	Enter: ca	Enter your first name, last name and password
Display prompt for login in	Enter: lg	Enter your account name and password
Display codes for navigation	Successful login	Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit
Display prompt for creating a credential	Enter: cc	Enter the site name, your username and password
Display a list of credentials	Enter: dc	Prints a list of saved credentials
Display prompt for which credential to copy	Enter: copy	Enter the site name of the credential you wish to copy.
Exit application	Enter: ex	Exit the current navigation stage
## SetUp / Installation Requirements

### Prerequisites
* python3.6
* pip
* pyperclip

## Cloning

* In your terminal:

  * $ git clone https://github.com/umutonij/Password-Locker/
  * $ cd Password-Locker
## Running the Application
* To run the application, in your terminal:

  $ chmod +x password.py
  $ ./password.py
## Testing the Application
* To run the tests for the class file:

  $ python3.6 user_test.py
  $ python3.6 credential_test.py
## Technologies Used

* Python3.6

## License

MIT ©2019 Jacqueline UMUTONI