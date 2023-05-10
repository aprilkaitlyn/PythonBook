###CREATING AND EDITING LISTS

coffees = ['caramel','vanilla','mocha','hazelnut'] 
print(coffees) #will print exactly as written above

print(coffees[0]) #access list elements
print(coffees[-1]) #access the last item in the list

message = f"My favorite coffee flavor is {coffees[0]}"
print(message)

coffees[2] = 'cinnamon' #can change any element in the list
coffees.append('toffee nut') #add element to the end of the list
print(coffees)

coffees.insert(0, 'white chocolate') #insert an element at a certain position
del coffees[0] #delete an element at a certain position

popped_coffee = coffees.pop() #deletes the last element of the list and we can assign that value to a variable
print(coffees)
print(f"Removed flavor: {popped_coffee}")

flavor = coffees.pop(1) #can pop from any position in the list
print(f"We are sold out of {flavor}")

#if you just want the value gone, use del. If you want to access the removed item use pop

coffees = ['caramel','vanilla','mocha','hazelnut','toffee nut'] 
coffees.remove('mocha') #can still remove items if you don't know their position
print("\n")

###ORGANIZING A LIST

kpop = ['twice', 'stray kids', 'le sserafim', 'ive', 'stayc']
kpop.sort() #permanently sorts the list alphabetically
print(kpop)

kpop.sort(reverse=True) #permanently sorts alphabetically backwards
print(kpop)

kpop = ['twice', 'stray kids', 'le sserafim', 'ive', 'stayc']
print("Original list:")
print(kpop)

print("\nSorted list:")
print(sorted(kpop)) #temporarily sort the list alphabetically

kpop.reverse() #permanently reverses order of the list chronologically
print(kpop)
print("\n")

len(kpop) #find the length of the list

