from collections import Counter

our_list = ['one','two','three','one','two','three','one','one']

words_counter = Counter(our_list)

#finding how many times an element occured frequently

frequently_occured = words_counter['one']

print frequently_occured

#finding the most occured element

most_occured = words_counter.most_common(1)

print most_occured

#finding the most occured 2 elements in the list 

most_occured_two = words_counter.most_common(2)

print most_occured_two
