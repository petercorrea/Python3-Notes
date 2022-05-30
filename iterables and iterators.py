#Iterables and Iterators
# Iterables and Iterators
# all()
# any()
# enumerate()
# iter()
# next()
# reversed()

# len()
# filter()
# sorted()
# map()

# range()
# slice()
# zip()


word = iter("PETERCORREA") #becomes an Iterator
next(word)
next(word) #Iterates through the iterable

#* 
word = iter("PETERCORREA") #becomes an Iterator
print(*word)


#Enumerate
heros = ['Batman', 'Superman', 'Flash', 'Rorschach']
names = ['Justin', 'Bryan', 'Eric', 'Pedro']

h = enumerate(heros)
list(h)

#Enumerate Unpack
for index, value in enumerate(heros):
    print(index, value)

    #Zip...similar to colum stack
heros = ['Batman', 'Superman', 'Flash', 'Rorschach']
names = ['Justin', 'Bryan', 'Eric', 'Pedro']

z = zip(heros, names)
list(z)

#Zip...create a dict
heros = ['Batman', 'Superman', 'Flash', 'Rorschach']
names = ['Justin', 'Bryan', 'Eric', 'Pedro']

z = zip(heros, names)
dict(z)

#Zip unpack
heros = ['Batman', 'Superman', 'Flash', 'Rorschach']
names = ['Justin', 'Bryan', 'Eric', 'Pedro']

for z1, z2 in zip(heros, names):
    print(z1, z2)

    # Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = list(mutants)

# Print the list of tuples
print(mutant_list)

# Change the start index
for index2, value2 in enumerate(mutant_list, start = 1):
    print(index2, value2)

    #Iterating through data chunks
for chunk in pd.read_csv('tweets.csv', chunksize = 10):
    # rest of for loop

