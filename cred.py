import random 
import string

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__ (self,account_username, account_password):
        '''
        __init method that helps us define properties for our objects
        Args:
        app_name: New app name
        account_username: New account username
        account_password: New account password
        '''
        self.account_username = account_username
        self.account_password = account_password

    def delete_logins(self):
        '''
        method to delete credential object
        '''
        Credentials.credentials_list.remove(self)
