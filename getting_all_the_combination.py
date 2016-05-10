#Getting all the combination from a sequence to form the sum of target
from itertools import combinations_with_replacement

some_list = [1,2,4,8,16,32]

target = 140

combinations = [comb for i in range(1,10) for comb in combinations_with_replacement(some_list, i) if sum(comb) == target]

print combinations
