# A List is a collection which is ordered and changeable. Allows duplicate members.
# Like arrays

#Create List
numbers = [1, 2, 3, 4, 5]
#Use Constructor
numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

#Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)


#Change value
fruits[0] = 'Blueberries'


#Remove from position with pop

fruits.pop(2)
print(fruits)


# Reverse list
fruits.reverse()

#Sort list
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)
