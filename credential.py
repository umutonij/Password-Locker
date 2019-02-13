class Credential:
    '''
    class that generates new instance for credentials
    '''
    credential_list=[]
    def __init__(self,account_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New credential account name.
            password : New credential password.
        '''
        self.account_name = account_name
        self.password = password

    credential_list=[]
    def save_credential(self):
        
        '''
        save_credential method saves credential object into credential_list
        '''
        Credential.credential_list.append(self)  

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
         Method that takes in a number and returns a contact that matches that number.

        Args:
            number:  password to search for
        Returns :
            Credential of account that matches the number.
        '''    

        for credential in cls.credential_list:
            if credential.account_name == name:
                return credential
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account_name: accopunt name to search if it exists
        Returns :
        Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == name:
                    return True

        return False  