import unittest
from responses import get_response 

class TestStringMethods(unittest.TestCase):

    def test_list_mons(self):
      self.assertEqual(get_response("help"),"add mons, calc, del mon, or erase all)\n")

    def test_get_response(self):
      self.assertEqual(get_response("@@"),"no valid input")
      
    def test_get_response(self):
      self.assertEqual(get_response("cheat Revive"),"0018")

if __name__ == '__main__':
    unittest.main()