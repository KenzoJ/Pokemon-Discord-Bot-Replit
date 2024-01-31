#THIS IS A SANDBOX FOR TESTING. FEEL FREE TO DELETE.
from replit import db
import json

person = "CJ"
print(db.keys(),"\n")

for i in db.keys():
  print(i)
for i in db[person].keys():
  print(i)
print(db.get_raw(person))

x = input("Delete mon?")
#works!
del db[person][x]
print("Success!")

#also works
print(db[person].pop(x))

'''
dict['user'].pop(0)
print(db.pop("a"))

print("All mons:
\n",json.loads(db.get_raw(person)))
print(json.loads(db.get_raw(person)).get("Magy"))

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