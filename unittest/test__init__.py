import unittest
from EE551Project.src.startup import *

class TestStartUp(unittest.TestCase):

    def test_StartUp(self):
        self.assertRaises(TypeError, StartUp())

if __name__ == '__main__':
    unittest.main()
