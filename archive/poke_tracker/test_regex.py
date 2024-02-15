import re

pattern = r'Start(.*?)End'
with open("CJ.txt", 'r') as file2:
  text = file2.read()
  match = re.search(pattern, text, re.DOTALL)
  print(f'\nthe match is: {match.group(0)!r}')
  print('\nthe span is:', match.span(0))
  print(match)
  pattern2 = r'Start[\r\n]+([^\r\n]+)'
  all_mons = re.findall(pattern2, "CJ.txt")

  print(all_mons)
