###LOOPY LISTY
colors = ['pink','yellow','orange','blue','green']
for color in colors:
    print(color) #loop through and print every color in the colors list

for color in colors:
    print(f"{color} is a pretty color!") #can write as many lines as you want to print for each item in the list

for value in range(1,5):
    print(value) #this will print 1-4

for value in range(6):
    print(value) #this will print 0-5

numbers = list(range(1,6))
print(numbers) #make a list using range()

even = list(range(2, 11, 2)) #print every other number between 2 and 10
print(even)

###NUMBER LISTS
squares = [] #make empty list
for value in range(1,11):
    square = value ** 2 # ** means ^
    squares.append(square) #add value created in equation to the empty squares list
print(squares) 

digits = [1,2,5,7,8,9,12,21]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares) #this does the same thing as the previous loop but makes the calc in the list instead of a loop

##SLICE N DICE
hair = ['bow','bandana','hat','barettes','claw clip']
print(hair[0:3]) #prints items 1-3 in the list
print(hair[:2]) #this will start the list at its beginning
print(hair[2:]) #this will start at 3rd item and print the rest
print(hair[-2:]) #this will print the last 2 items in the list

for style in hair[:2]:
    print(style.title()) #loop through a slice

##COPYING
my_foods = ['falafel', 'chickpeas', 'naan']
med_foods = my_foods[:] #a slice with just : will basically copy the list. Just setting the lists equal to eachother does not work!
print(med_foods)

#the lists are now separate and can be edited separately
my_foods.append('tzatziki')
med_foods.append('tahini')
print(my_foods)
print(med_foods)

##TUPLES - list of items that cannot change using () instead of []
dimensions = (20,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (30,60) #you can override a tuple by redefining it
print("New dimensions:")
for dimension in dimensions:
    print(dimension)
