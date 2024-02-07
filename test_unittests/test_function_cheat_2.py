import unittest
from responses import get_response 
from cheat import moves

class TestStringMethods(unittest.TestCase):

  def test_get_response(self):
    self.assertEqual(get_response("@@"),"no valid input")

if __name__ == '__main__':
    unittest.main()