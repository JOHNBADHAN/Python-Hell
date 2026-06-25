# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter Species of your Pet: ").capitalize()
age = int(input("Enter age of your Pet: "))

if age < 2 and species == "Dog":
    food = "Puppy food"

elif age > 5 and species =="Cat":
    food = "Senior cat food"

print(food)