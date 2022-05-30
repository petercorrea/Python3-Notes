# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Creating
tuple = 'Pirates', 'Rum'
type(tuple)

#Accessing elements
print(tuple[0])
print(tuple[1])

#Tuples are immutable...will display errors
tuple[0] = 'Capt. Jack Sparrow'

#Mutable elements can be updated
list1 = ['Whiskey', 'Beer', 'Wine']
list2 = ['Professor Plum', 'Mr.Green']
list3 = [1, 2, 3, 4]

anotherTuple = (list1, list2, list3)
list1.append('Scotch')
anotherTuple 

#Tuple swapping...unpacking tuples
a, b = 1, 5 #print(1, 5)
a, b = b, a
a, b #prints (5, 1)

#Looping through a list of tuples
list_of_tuples = [(2,2),(3,3),(4,4)]

new_list = [tup[0]*tup[1] for tup in list_of_tuples]
print(new_list)