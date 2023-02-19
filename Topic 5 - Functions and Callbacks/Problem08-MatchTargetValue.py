# Create a Python function that takes a list of integers and a target value, and returns a tuple containing the indices of the two integers in the list that add up to the target value. 
# If no such pair exists, the function should return None.

def matchTargetValue(aLists, target):
  matchingTuple = ()
  for i in list(enumerate(aLists)):
    for j in list(enumerate(aLists))[i[0]+1:]:
      if i[1] + j[1] == target:
        matchingTuple = (i[0], j[0])
        return matchingTuple
  return None

aLists = [1, 2, 5, 3, 6, 8, 9, 7]
target = 15
print(matchTargetValue(aLists, target))
