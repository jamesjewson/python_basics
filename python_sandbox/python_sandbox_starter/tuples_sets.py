# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes') 
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#If you have only one value, you want a trailing comma
fruits3 = ('Apples',)

#Get value
# print(fruits[1])

#Can't Change value
# fruits[0] = 'Pears'

#Delete tuple
del fruits2

# print(fruits, fruits2)

#Get length
# print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
# print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

#Add duplicate (Nothing happens)
fruits_set.add('Apples')

#Remove 
# fruits_set.remove('Grape')

#Clear set
# fruits_set.clear()

#Delete set
# del fruits_set

print(fruits_set)