print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)},")
print(f"Memory Address: {id(name)})")

print(f"Age: {age} (Type: {type(age)},")
print(f"Memory Address: {id(age)})")

print(f"Height: {height} (Type: {type(height)},")
print(f"Memory Address: {id(height)})")

print(f"Favourite Number: {fav_number} (Type: {type(fav_number)},")
print(f"Memory Address: {id(fav_number)})")

current_year = 2026
birth_year = current_year - age

print("\nYour birth year is approximately:")
print(f"{birth_year} (based on your age of {age})\n")

print("Thank you for using the Personal Data Collector. Goodbye!")
