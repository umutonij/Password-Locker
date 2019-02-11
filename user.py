class User:

    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,email,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        user_list = [] # Empty user list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
      
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: Password to search for
        Returns :
            User of person that matches the password.
        '''

        for user in cls.user_list:
            if user.password == password:
                return user