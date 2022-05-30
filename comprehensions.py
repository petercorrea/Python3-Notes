# Comprehensions allow you to work with iterators and create iterators
# Syntax follows [<returned_exp> for <item> in <iterable>]

# List Comprehenshions
lcomp = [num * 2 for num in range(1, 6)]

# Dict Comprehenshions
dcomp = {letter: num for letter, num in zip('abcdef', range(1, 7))}

# Set Comprehenshions
scomp = {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}

print(lcomp)
print(dcomp)
print(scomp)
outer = 'abc'
inner = '123'
[(y, x) for y in outer for x in inner]

num_pairs = [(num1, num2) for num1 in range(0,4) for num2 in range(4, 8)]
print(num_pairs)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(3)] for row in range(7)]

# Print the matrix
for row in matrix:
    print(row)

#Conditionals in Comprehenshions Predicate
[num ** 2 for num in range(10) if num % 2 == 0]

#Dict Comprehenshions
pos_neg = {num : -num for num in range(10)}
print(pos_neg)

#Conditionals in Comprehenshions Output Expression
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)

#Generators
#Same as list, except they produce Generator objects and are computed when needed...not stored in memmory
result = (num for num in range(31))

print(next(result))
print(next(result))

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)

#Generator functions are functions that, like generator expressions, yield a series of values, 
#instead of returning a single value.

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)


for value in get_lengths(lannister):
    print(value)