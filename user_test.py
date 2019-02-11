import unittest # Importing the unittest module
from contact import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Umutoni","Jacqueline","jacquelineumutoni13@gmail.com","test123") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Umutoni")
        self.assertEqual(self.new_user.last_name,"Jacqueline")
        self.assertEqual(self.new_user.email,"jacquelineumutoni13@gmail.com")
        self.assertEqual(self.new_user.password,"test123")



if __name__ == '__main__':
    unittest.main()