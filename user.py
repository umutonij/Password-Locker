class User:
    """
    class that generates new instances of user
    """
    
    user_list=[]

    def __init__(self,first_name,last_name,create_pw,confirm_pw):
    
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New user first name.
            last_name : New user last name.
            create_pw: New user create pw.
            confirm_pw : New user confirm pw .
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.create_pw = create_pw
        self.confirm_pw= confirm_pw
    
    user_list=[]
    def login_user(self):
        '''
        login_user method saves contact object into user_list
        '''
        User.user_list.append(self)