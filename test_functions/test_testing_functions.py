#THIS IS A SANDBOX FOR TESTING. FEEL FREE TO DELETE.
from replit import db
import json

print(json.loads(db.get_raw("CJ")).get("ivs"))
x = []
y = []
x = (json.loads(db.get_raw("CJ")).get("ivs"))
print(x)
print(x[0],x[1])

y = json.loads(db.get_raw("CJ")).get("stats")[0]
print(y[0],y[1])



db = {
  "CJ":
  {
    "Poke": "Magikarp",
    "nick":"Henry",
  }
}