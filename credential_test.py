import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Umutoni","Instagram","umutonij","test123") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Umutoni")
        self.assertEqual(self.new_credential.site_name,"Instagram")
        self.assertEqual(self.new_credential.account_name,"umutonij")
        self.assertEqual(self.new_credential.password,"test123")



    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the user list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

        # Items up here...

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Jacky","Twitter","umutonij","test123") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

# other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Jacky","Twitter","umutonij","test185") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
            # More tests above
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Muhoza","Gaju","muhozagaju@gmail.com","test185") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_site(self):
        '''
        test to check if we can find a credential by site and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Jacky","Twitter","umutonij","test123") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_site("Twitter")

        self.assertEqual(found_credential.password,test_credential.password)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Jacky","Gmail","umutonij","test456") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Gmail")

        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentialS saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ ==  '__main__':
    unittest.main()
