# Dicts are not sorted and cannot be indexed

#Creating
world = {
    'Italy':'Rome', 
    'Spain': 'Madrid', 
    'Norway': 'Oslo', 
    'Iceland':'Reykjavik'
}

#Adding values
world['Greenland'] = 'Nuuk'

#Adding multiple values at a time
world.update({"anotherTown":"anotherCapital", "someTown":"someCapital"})

# Accessing values
print(world['Spain'])

#Deleting values
del(world['Iceland'])
world.pop('someTown') 
world.clear #Empties entire dict

#Packing...another way to create a dict
def packer(name=None, **kwargs): #it will catch 'name' and not including in the packing process
    print(kwargs)                #**kwargs must always be the final parameter
    
packer(name='Peter',gender='male', age=28)

#Unpacking
my_dict = {'first_name':'Peter', 'last_name':'Correa'}

"My name is {first_name} {last_name}".format(**my_dict)

#Iteration
my_dict = {'Conductor':'Sir Simon Rattel', 'Composition':'Symphony in D minor', 'Composer':'G. Mahler'}

for k in my_dict:
    print(k + ': ' + my_dict[k])
    
#more pythonic
for k in my_dict.items():
    print(k)

#Loops through Dictionaries...must add .items() method
world_dict = {
             'Country':['Italy','Spain', 'Norway', 'Belgium', 'Iceland', 'Finland'],
             'Capital':['Rome','Madrid','Oslo','Brussels','Reykjavik','Helsinki'],
             'Population':[15,11,9,7,8,3]}

for key, value in world_dict.items(): 
    print(key, value)