# No indexing, no order, iterable

set_of_nums = set([1,2,3,4,5,6,7,8,9,0])
set_of_primes = set([1, 3, 5, 7, 9, 11, 13, 17,19])

union = set_of_nums.union(set_of_primes) #All items
diff = set_of_nums.difference(set_of_primes) #Unique to the first set
sym_diff = set_of_nums.symmetric_difference(set_of_primes) #unique to eachside
intersect = set_of_nums.intersection(set_of_primes) #Shared values
