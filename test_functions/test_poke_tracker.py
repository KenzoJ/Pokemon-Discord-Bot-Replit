from test_input import input_checker
from test_dict import calc_export

def main():
  x = input("Task?")
  if x == "Add Pokemon":
    input_checker()
  if x == "Calc":
    calc_export()
  if x == "Clear":
    del db["CJ"]

main()

##REALLY RECOMMEND reading through https://replit-py.readthedocs.io/en/latest/db_tutorial.html for an understanding on the datbase. 