message = "Hello world!"
print(message)

message = "Python time" #you can keep redefining the same variable like so
print(message)

name = "kaitlyn"
print(name.title()) #prints with first letter capitalization
print(name.upper()) #prints all caps
print(name.lower()) #prints lowercase

first_name = "Kaitlyn"
last_name = "Heishman"
full_name = f"{first_name} {last_name}" #f is used for concatenation
print(full_name)

print("\tTabby text") # \t places a tab

print("Drinks:\n\tCoffee\n\tDiet Coke") # \n places a new line

name = " Kaitlyn "
name.rstrip() #rstrip removes whitespace on the right side of the string
name.lstrip() #lstrip removes whitespace on the left side
name.strip() #strip removes whitespace on both ends

url = "https://kaitlyniscool.com"
url.removeprefix('https://') #removes the prefix of course

money = 8_000_000 #underscores in a number used for readability, python won't print them

x,y,z  = 1,2,3 #assign variables at the same time

CONSTANT_NUMBER = 500 #write constants in all caps
