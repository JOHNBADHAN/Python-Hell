name = ["John", "Sam", "Chris", "Ron"]

print(",".join(name))

a = name[1:3]
print(a)

word = "amazing"

# b = word[-7:-1]
# b = word[:7]    
# b = word[0:]
# print(b)

print(len(word))
print(word.endswith("ing"))
print(word.count("a"))
print(word.capitalize())
print(word.find("m"))
print(word.replace("m", "p"))

# Format

str = "{} is a good {}"

format = str.format("Mark", "Boy")
print(format)

a = r"ron/dd\nj"

print(a)