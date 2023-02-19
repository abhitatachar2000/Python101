# Implement a Python function that takes a list of tuples, where each tuple contains two integers, and returns the tuple with the largest sum of the two integers. 
# The function should be able to handle empty lists and lists with invalid tuples (e.g. tuples that do not contain two integers).

def findTupleWithMaxSum(tupleList):
  maxSum = 0
  maxTuple = ()
  for i in tupleList:
    tupleSum = i[0] + i[1]
    if tupleSum >= maxSum:
      maxSum = tupleSum
      maxTuple = i
  return maxTuple

tupleList = [(1,20), (2, 3), (3, 4), (7, 9), (5, 6), (7, 2)]
print("Tuple with maximum sum is {0}".format(findTupleWithMaxSum(tupleList)))
