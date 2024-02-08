#This function is to test the poke tracker and adding mons and exporting the calc

import unittest
from responses import get_response 
from cheat import moves
from poke_tracker.export_pokemon import calc_mon

class TestStringMethods(unittest.TestCase):
  
  def test_export_mons(self):
    self.assertEqual(calc_mon("CJ","Magi"),['Magikarp', 'Level: 50', 'Bold Nature', 'Ability: Flash Fire', 'EVs: 252 HP / 252 Def', 'IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe', '-Tackle', '-Tackle', '-Tackle', '-Tackle'])

if __name__ == '__main__':
    unittest.main()