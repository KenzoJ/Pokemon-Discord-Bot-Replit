#this is a basic test to see if help gives you
#actual help. And if there's no valid input.

import unittest
from responses import get_response 

class TestStringMethods(unittest.TestCase):

    def test_list_mons(self):
      self.assertEqual(get_response("help"),"You can:\n -add mons\n -export\n -del mon\n -erase all\n")

    def test_get_response(self):
      self.assertEqual(get_response("@@"),"no valid input")

      

if __name__ == '__main__':
    unittest.main()