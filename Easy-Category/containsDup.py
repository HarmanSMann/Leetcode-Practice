# Contain dupes: https://leetcode.com/problems/contains-duplicate/

# one way to solve the problem is to iterate through the array and store all 
# unique values into a set, if something is already in the set, then stop checking and return contains dup

example = [1,2,3,4,5,6,6,7,8,10]

dup = set()

for n in example:
  if number in dup:
    return True
  else:
    dup.add(n)
