#THIS IS A SANDBOX FOR TESTING. FEEL FREE TO DELETE.
from replit import db
import json

person = input("For whom?\n")
print(db.keys(),"\n")
print(db[person].keys(),"\n")
print(db.get_raw(person))
print("All mons:\n",json.loads(db.get_raw(person)))
print(json.loads(db.get_raw(person)).get("Magy"))
'''
while True:
  try:
    for i in db[person].keys():
      print(i)
    delete_mon = input("Which mon\n")
    if delete_mon in db[temp_name].keys():
      print(db[temp_name].pop(delete_mon))
      break
  except KeyError:
    continue
    "try again"
'''