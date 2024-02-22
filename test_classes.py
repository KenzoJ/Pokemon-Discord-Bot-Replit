import json
from replit import db

def export_mon(dict_name):
  x = []
  y = []
  x = json.loads(db.get_raw(dict_name)).get("stats")[0:]
  y = json.loads(db.get_raw(dict_name)).get("ivs")
  test_vari = []
  test_vari.append(db[dict_name]["poke"])
  level = f'Level: {db[dict_name]["lv"]}'
  test_vari.append(level)
  test_vari.append(f'{db[dict_name]["ntr"]} Nature')
  test_vari.append(f'Ability: {db[dict_name]["abil"]}')
  test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
  test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
  for i in db[dict_name]["all_moves"]:
    test_vari.append(f"{i}")
  return test_vari
  
