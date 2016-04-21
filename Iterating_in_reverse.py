#Iterating elements from a sequence in reverse order
some_list = [1,2,3,4,5,6,7,8,9]

for elements in reversed(some_list):
	print elements

#Method 2:
some_list = [1,2,3,4,5,6,7,8,9]

reversed_list = some_list[::-1]

for elements in reversed_list:
	print elements
