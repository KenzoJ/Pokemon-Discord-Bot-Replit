#THIS IS A SANDBOX FOR TESTING. FEEL FREE TO DELETE.
from references import cheat_database
from replit import db
import json
from references import cheat_database, stats, iv_dict, move_database, all_battle_items


temp_list = []
for i in all_battle_items:
  temp_list.append(i)
index = 0
limit = 5
for index, element in zip(range(limit), all_battle_items):
  print(all_battle_items[index])
  