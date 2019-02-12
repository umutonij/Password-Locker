class Credential:

    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,user_name,site_name,account_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
        credential_list = [] # Empty credential list
 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves user objects into credential_list
        '''

        Credential.credential_list.append(self)
      
    def delete_credential(self):

        '''
        delete_credential method deletes a saved user from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_site(cls,site):
        '''
        Method that takes in a site_name and returns a credential that matches that site_name.

        Args:
            site_name: site_name to search for
        Returns :
            Credential of person that matches the site_name.
        '''

        for credential in cls.credential_list:
            if credential.site_name == site:
                return credential
    @classmethod
    def credential_exist(cls,site):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            site: site name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.site_name == site:
                    return True

        return False  

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
