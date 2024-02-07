from replit import db
from cheat import moves

def get_response(user_input):
  response: str = user_input.lower()

  if response.startswith("@"):
    return "delete"
  if response == "list mons":
    return "list mons"
  if response.startswith("cheat"):
    response = response.split()
    response = " ".join(response[1:])
    code = moves(response)
    return code
  else:
    return "no valid input"
