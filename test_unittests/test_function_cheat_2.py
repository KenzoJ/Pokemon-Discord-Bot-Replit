import unittest
from responses import get_response 
from cheat import moves
from add_mon import add_mon
from del_mon import del_mon
from export_mon import export_mon

class TestStringMethods(unittest.TestCase):

    def test_list_mons(self):
      self.assertEqual(")
  
'''
    def test_get_response(self):
      self.assertEqual(get_response("@@"),"delete")
'''
if __name__ == '__main__':
    unittest.main()