# we want the multiples of 7
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# we want to do the same thing, but with less code
# List comprehension
multiples = [x * 7 for x in range(1, 11)]
print(multiples)
# List comprehensions let us create new lists based on sequences or ranges

# we want to generate a list of the lengths of the strings
languages = ['python', 'perl', 'ruby', 'go', 'java', 'c']
lengths = [len(language) for language in languages]
print(lengths)

# we want all the numbers divisible by 3 between 0 and 100
z = [x for x in range(0,101) if x % 3 ==0]
print(z)
