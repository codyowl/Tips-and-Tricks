from collections import Counter


list_with_repeated_numbers = [1,2,2,3,3,3,4,4,4,4,4]

counted_list = Counter(list_with_repeated_numbers)

for key, value in counted_list.items():
	print "Number %s is occured %s times" % (key , value)



