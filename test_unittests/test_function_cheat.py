import unittest
from responses import get_response 
from cheat import moves

class TestStringMethods(unittest.TestCase):

    def test_list_mons(self):
      self.assertEqual(moves("Quick Claw"),"00B7")
  
'''
    def test_get_response(self):
      self.assertEqual(get_response("@@"),"delete")
'''
if __name__ == '__main__':
    unittest.main()