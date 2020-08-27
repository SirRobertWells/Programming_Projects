animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
    chars += len(animal)

print('Total characters: {}, Average length: {}'.format(chars, chars / len(animals)))

# now going over the "enumerate" function
winners = ['Ashley','Dylan', 'Reese']
for index, each_person in enumerate(winners):
    print('{} - {}'.format(index + 1, each_person))
# The enumerate function returns a tuple for each element (each_person) in the list (winners).
# The first value {} in the tuple is the index (index + 1) of the element in the sequence.
# The second value {} in the tuple is the element (each_person) in the sequence.

# practice exercise

# Try out the enumerate function for yourself in this quick exercise.
# Complete the skip_elements function to return every other element from the list,
# this time using the enumerate function to check if
# an element is on an even position or an odd position.
#def skip_elements(elements):
#    # code goes here
#
#   return ___
#
#
#print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
#print(skip_elements(
#    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
def skip_elements(elements):
    # code goes here
    for i

    return ___


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']