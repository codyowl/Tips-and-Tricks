some_list = ['one', 'two', 'three', 'four']

#Method :1 
#Conver the list to string and then remove the first and last element

method_1 = str(some_list)[1:-1]

#Method :2
#Use join to seperate elements
method_2 = ', '.join(map(str, some_list))


