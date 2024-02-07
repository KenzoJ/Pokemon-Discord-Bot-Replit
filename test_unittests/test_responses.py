import unittest
from responses import get_response 

class TestStringMethods(unittest.TestCase):

    def test_list_mons(self):
      self.assertEqual(get_response("list mons"),"list mons")

    def test_get_response(self):
      self.assertEqual(get_response("@@"),"delete")
      
    def test_get_response(self):
      self.assertEqual(get_response("cheat Revive"),"0018")

if __name__ == '__main__':
    unittest.main()