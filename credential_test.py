import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_credential=Credential("Instagram","123")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.password,"123")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into credential list
        '''
        self.new_credential.save_credential()   
        self.assertEqual(len(Credential.credential_list),1) 

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''    
        self.new_credential.save_credential()
        test_credential = Credential("Instagram","123")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential=Credential("Instagram","123")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)    
        
    def test_find_credential_by_name(self):
        '''
        test to check if we can find a credential by account name and dispaly information
        '''     
        self.new_credential.save_credential()
        test_credential=Credential("Instagram","123")
        test_credential.save_credential()

        found_credential=Credential.find_by_name("Instagram")

        self.assertEqual(found_credential.password,test_credential.password)


if __name__=='__main__':
    unittest.main()        

