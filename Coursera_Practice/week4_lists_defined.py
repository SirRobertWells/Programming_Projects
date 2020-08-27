# Modifying the Contents of a List

fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwi')
print(fruits)
# You can start w an empty list and add all
# of it's items using the append method.

fruits.insert(0, 'Orange')
print(fruits)
# fruits.insert(index position, 'element')

fruits.insert(25, 'Peach')
print(fruits)
# selecting an index position LARGER
# than list length still works. no error.
# it just gets added to the end.

fruits.remove('Melon')
print(fruits)
# removes the FIRST OCCURENCE of the element named

###fruits.remove('Pear')
###print(fruits)
# traceback error. element wasnt in the list.

fruits.pop(3)
print(fruits)
# another way to remove elements from a list. receives an index.
# also supposed to return the element. in this ex it would be 'Apple'

fruits[2] = 'Strawberry'
print(fruits)


# assign something else to the position.
# fruits[position for item doing the replacing] = 'NEW ITEM'

##########
# Practice Exercise#
##########

def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(element)
        # Increment i
        i += 1

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []
