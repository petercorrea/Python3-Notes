# Lists
list = ["peter", "miguel", "correa"]
list.append("michael")
list.remove("miguel")  # will err if val is not found
list.sort()
list.reverse()
secondItem = list[0]
lastItem = list[-1]
slice = list[0:3]  # both indices are inclusive

#Creating
toDoList = ["Wash Car", "Walk Dog", "Visit Tristan da Cunha"]

#Appending
toDoList.append('Read a Novel')

#Add elements from one list to another
otherList = ['Visit the Moon', 'Feed Snake', 'Walk Dog']
toDoList.extend(otherList)

#Concat
otherList = ['Visit the Moon', 'Feed Snake', 'Walk Dog']
together = toDoList + otherList

#Finding index of element
snake_position = toDoList.index('Feed Snake')

#Deleting values
toDoList.pop(snake_position) #takes index
toDoList.remove('Walk Dog') #deletes first occurance 
del(toDoList[2]) 

#Slicing [start:exclusive_end:skips]
someList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
someList[0:3] #last selection is exclusive
someList[0:8:2] #skips
someList[-7:-1] #negative indexing...-1 is the second to last element from the right
someList[-2:-8:-1] #-1 allows to print right to left (-2 to -8)

#Length
len(toDoList)

#Lists are Reference Type
toDoList = ["Wash Car", "Walk Dog", "Visit Tristan da Cunha"]

toDoList2 = toDoList
toDoList2[2] = "Learn Swing Dancing"

print(toDoList) #original is changed
print(id(toDoList)) # Same ID
print(id(toDoList2))

#Copy Lists
toDoList = ["Wash Car", "Walk Dog", "Visit Tristan da Cunha"]

toDoList2 = toDoList.copy() #copies
toDoList2[2] = "Learn Swing Dancing"

print(toDoList)
print(toDoList2)
print(id(toDoList))
print(id(toDoList2))

#Looping
for i in toDoList:
    print(i)

    # Checking for values
if "Wash Car" in toDoList:
        print("yes")
