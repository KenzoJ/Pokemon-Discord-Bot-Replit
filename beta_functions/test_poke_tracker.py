from test_input import input_checker
from test_dict import calc_export
from replit import db
import sys

def main():
  x = input("Task? (add mons, calc, del mon, or erase all)\n")
  if x == "add mons":
    input_checker()
  if x == "calc":
    calc_export()
  if x == "erase all":
    if "Sam" in db.keys():
      del db["Sam"]
    if "Doug" in db.keys():
      del db["Doug"]
    if "CJ" in db.keys():
      del db["CJ"]
    else:
      print("Bitch empty")
      sys.exit
      
  if x == "del mon":
    while True:
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
   
    
    
main()
##REALLY RECOMMEND reading through https://replit-py.readthedocs.io/en/latest/db_tutorial.html for an understanding on the datbase. 