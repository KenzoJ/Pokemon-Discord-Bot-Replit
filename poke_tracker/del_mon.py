from replit import db
import json


def del_mon():
  try:
    person = input("For whom?\n")
    for i in db[person].keys():
      print(i)
    delete_mon = input("\nWhich mon\n")
    if delete_mon in db[person].keys():
      del db[person][delete_mon]
      print("It's gone")
      break
  except KeyError:
    continue
    "try again"

if __name__ == "__del_mon__":
  del_mon()