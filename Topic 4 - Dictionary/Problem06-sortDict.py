"""
Write a program to sort a dictionary by its values in descending order.
"""
import operator #operator module specifies standard operators as function
def sortDict(unsortedDict):
    sortedDict = sorted(unsortedDict.items(), key=operator.itemgetter(1), reverse=True)
    # operator.itemgetter() -> Return a callable object that fetches item from its operand using the operand’s __getitem__() method. If multiple items are specified, returns a tuple of lookup values.
    return sortedDict

unsortedDict = {'a':12, 'b':5, 'c':6, 'd':4}
print(sortDict(unsortedDict))
