###IF STATEMENTS
kpop = ['bts','twice','stray kids','le sserafim']
for group in kpop:
    if group == 'bts': #if statement uses ==
        print(group.upper())
    else:
        print(group.title())

# group = bts #this would give the group variable the value of bts
# group == bts #this checks if the group is bts

##equality is case sensitive, set the variable to lower to avoid an issue 
group = 'Le sSeraFim'
group.lower() == "le sserafim"

#check inequality
topping = 'tomato'
if topping != 'tomato':
    print("no tomatoes please!")

answer = 21
if answer != 38:
    print("wrong answer!")

#checking comparisons
age = 24
if age < 21:
    print("no minors at the bar!")
if age >= 21:
    print("party time!")

##check multiple conditions
age_kj = 24
age_kb = 22
if age_kj >= 21 and age_kb >=21:
    print("double party time!")

##check for one condition
color1 = 'pink'
color2 = 'yellow'
if color1 or color2 == 'pink':
    print("I love pink!")

##check for a value in a list
med_bowl = ['rice','falafel','hummus','tahini']
topping = 'hummus'
if topping in med_bowl:
    print(f"Yum {topping}!")

##check that a value is not in a list
banned_users = ['bob', 'snob', 'glob']
user = 'susan'
if user not in banned_users:
    print("access granted O.o")

##Python uses the "elif" keyword
age = 10
if age < 4:
    price = 'free'
elif age < 12:
    price = 10
else:
    price = 15
print(f"admission cost = ${price}")

##you don't need else, can just have many elif statements
grade = 11
if grade < 5:
    school = 'elementary'
elif grade < 8:
    school = 'middle'
elif grade < 12:
    school = 'high'
print(f"you are in {school} school")

##testing multiple conditions
if 'rice' in med_bowl:
    print ("Adding rice")
if 'hummus' in med_bowl:
    print ("Adding hummus")
if 'falafel' in med_bowl:
    print ("Adding falafel")
if 'slaw' in med_bowl:
    print ("Adding slaw")
print("\nMed bowl ready!")

sandwich_toppings = ['spinach','avocado','pickles', 'lettuce']
for topping in sandwich_toppings:
    if topping == 'lettuce':
        print(f"Sorry, we are out of lettuce!")
    else:
        print(f"Adding {topping}!")
print("\nSandwich ready!")

##Check list is not empty
sandwich_toppings = []

if sandwich_toppings:
    for topping in sandwich_toppings:
        print(f"Adding {topping}")
    print ("\n Sandwich ready!")
else:
    print("You just want bread?")

print("\n")
##Using two lists together

available_toppings = ['cheese','jalapenos','green peppers','mushrooms','spinach','basil']
requested_toppings = ['cheese', 'pineapple', 'jalapenos']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}!")
    else:
        print(f"Sorry we don't have {requested_topping}.")
print("\n Pizza is ready!")
