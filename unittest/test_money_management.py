import unittest
import sys
import money_management
from __init__ import *


class TestLogInUser(unittest.TestCase):

    def test_checkpassword(self):
        checkpassword = money_management.checkpassword()
        self.assertFalse(checkpassword)


# class TestStartUp(unittest.TestCase):

# class TestLogInNewUser(unittest.TestCase):

# class TestBankActions(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
