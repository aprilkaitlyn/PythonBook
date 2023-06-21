###DICTIONARIES

##Created in a key-pair manner
smite_0 = {'name': 'Nu Wa', 'class': 'Mage'}
smite_1 = {'name': 'Awilix', 'class': 'Assassin'}
smite_2 = {'name': 'Neith', 'class': 'Hunter'}

##Access values in a dictionary
print(smite_0['name'])

##Add new key values
smite_0['pantheon'] = 'Chinese'
smite_1['pantheon'] = 'Mayan'
smite_2['pantheon'] = 'Egyptian'

print(smite_1)

##Starting off empty, often when user input is involved
drink_0 = {}

drink_0['name'] = 'Latte'
drink_0['flavor'] = 'Caramel'

##Modify values just like a regular variable
drink_0['flavor'] = 'Vanilla'

##Delete values
del drink_0['flavor']
print(drink_0)
print("\n")

##Dictionary of similar objects
last_comeback = {
    'twice': 'set me free',
    'le sserafim': 'unforgiven',
    'stray kids': 'case 143',
    'ive': 'I am',
    'stayc': 'teddy bear',
}
song = last_comeback['le sserafim'].title()
print(f"Le Sserafim's last comeback was {song}")
print("\n")

##Use get() if you are unsure if the key exists for the object
size = drink_0.get('size', 'No default size')
print(size) 

##Loop through a dictionary
user_0 = {
    'username': 'jimjim',
    'first': 'Jimbo',
    'last': 'Jambo', 
}
print("\n")

for key, value in user_0.items(): #you can use any words in place of key and value
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for group, song in last_comeback.items():
    print(f"{group.title()}'s last comeback was {song.title()}")
print("\n")

##Loop through using a key
for group in last_comeback.keys(): #looping through keys is default so omitting .keys() wouldn't change the output
    print(group.title())
print("\n")

#Using if statement while looping through key
fave_veggie = {
    'suze': 'broccoli',
    'marla': 'tomato',
    'tera': 'cucumber',
    'grace': 'corn',
}

agree = ['suze','grace']
for name in fave_veggie.keys():
    print(f"Hi {name.title()}")

    if name in agree:
        veggie = fave_veggie[name].title()
        print(f"\t{name.title()}, I also like {veggie}")

if 'dorothy' not in fave_veggie.keys():
    print("Dorothy what is your fave veggie?")

##Using sorted() to see the keys in order
for name in sorted(fave_veggie.keys()):
    print(f"{name.title()}, thanks for sharing the veggies")

##Loop through all values in the dictionary
print("The following veggies have been mentioned:")
for veggie in fave_veggie.values():
    print(veggie.title())

##Loop through without duplicates with set()
print("The following veggies have been mentioned:")
for veggie in set(fave_veggie.values()):
    print(veggie.title())

print("\n")

##LIST OF DICTIONARIES

###Create multiple cakes
cake_0 = {'flavor':'vanilla', 'frosting':'buttercream'}
cake_1 = {'flavor':'red velvet', 'frosting':'cream cheese'}
cake_2 = {'flavor':'chocolate', 'frosting':'fudge'}

###Put the cakes in a list
cakes = [cake_0, cake_1, cake_2]

for cake in cakes:
    print(cake)

###Use range() to create many cakes at once
cakes = []

for cake_number in range(20):
    new_cake = {'flavor':'lemon', 'frosting':'strawberry'}
    cakes.append(new_cake)

for cake in cakes[:5]:
    print(cake)

print(f"There are {len(cakes)} cakes now!")

###Go back and alter some of the new cakes, could also add elif statements to further change them
for cake in cakes[:3]:
    if cake['flavor'] == 'lemon':
        cake['flavor'] = 'confetti'
        cake['frosting'] = 'vanilla'

for cake in cakes[:5]:
    print(cake)

print("\n")

##THE SEQUEL: NOW LISTS IN DICTIONARIES - do this when you want multiple values assigned to one key in a dictionary
sandwich = {
    'bread':'wheat',
    'toppings':['avocado','cheddar','lettuce']
}

print(f"You ordered a {sandwich['bread']} bread sandwich with:")

for topping in sandwich['toppings']:
    print(f"\t{topping}")

### some keys could have only one variable
fave_fruit = {
    'Mauve': ['strawberry'],
    'Violet': ['apple', 'grape'],
    'Peach': ['watermelon']
}

###now use an if statement to adjust how each are printed - lists can't use title but str(ings) can, give a new loop just for fruits to use .title?
for name, fruits in fave_fruit.items():
    if len(fruits) == 1:
        print (f"{name}'s favorite fruit is:")
        for fruit in fruits:
            print(f"{fruit.title()}")
    else:
        print (f"{name}'s favorite fruits are:")
        for fruit in fruits:
            print(f"{fruit.title()}")

print("\n")

##INCEPTION DICTIONARY INSIDE DICTIONARY??
smoothies = {
    'dreamboat': {
        'fruit':'banana',
        'base':'almond milk',
        'extra':'chia'
    },
    'islander': {
        'fruit':'pineapple',
        'base':'coconut milk',
        'extra': 'protein'
    }
}

#the dictionary associated with each smoothie will be referred to as 'recipe'
for smoothie, recipe in smoothies.items():
    ingredients = f"{recipe['fruit']}, {recipe['base']}, {recipe['extra']}"
    print(f"\nThe {smoothie.title()} smoothie is made with {ingredients}")
    
