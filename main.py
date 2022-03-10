from data import navigation_data
#
from data import toy_data
import copy

# import a copy of the navigation data
# data = copy.copy(navigation_data)
data = copy.copy(navigation_data)

scores = {")" : 3,
         "]":57,
         "}":1197,
         ">":25137}

forward_mapping = {'{':'}' ,
          '[':']',
          '(':')',
          '<':'>'
                  }

reverse_mapping = {v: k for k, v in forward_mapping.items()}

# first, I want to remove the valid pairs and collapse
# the data strings into their unmatched pairs
def valid_pairs_find_and_remove(data):
  valid_pairs_removed = False
  while not valid_pairs_removed:
    stack = data
    data = data.replace('()','')
    data = data.replace('[]','')
    data = data.replace('{}','')
    data = data.replace('<>','')
    if stack == data:
      valid_pairs_removed = True
  return data

data = valid_pairs_find_and_remove(data)

# secondly, I want to parse through the characters 
# and match the open brackets to any hanging closed 
# brackets.  
total_score = 0
for line in data.splitlines():
  stack = []
  for char in line:
    if char in forward_mapping:
      stack.append(char)
    elif char in reverse_mapping:
      if reverse_mapping[char] == stack[-1]:
        stack.pop()
      else:
        total_score += scores[char]
        break
    else:
      score = 0

print("score: {0}".format(total_score))

