#Write a python function that returns the greatest of three numbers.
def findMax(a, b, c):
	greatest = a;
	if (a > b):
		if b > c:
			greatest = a
		elif a > c:
			greatest = a
		else:
			greatest = c
	else:
		if b > c:
			greatest = b
		else:
			greatest = c
	return greatest

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
print("Max of three number {0}, {1} and {2} is {3}".format(a, b, c, findMax(a, b, c)))
