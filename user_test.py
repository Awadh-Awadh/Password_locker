import unittest
from account import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def SetUp(self):
        self.new_account = User("awadh","Dreezy@84")
    
    def test_init(self):
        self.assertEqual(self.new_account.user_name, "awadh")
        self.assertEqual(self.new_account.password, "Dreezy@84")
    
    def test_save_user(self):
        self.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_delete_user(self):
        self.delete_user()
        self.assertEqual(len(User.user_list), 0)

if __name__ == '__main()':
    unittest.main()