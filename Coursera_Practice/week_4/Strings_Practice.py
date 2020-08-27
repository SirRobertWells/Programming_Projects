name = 'Manny'
number = len(name) * 3
print('Hello {} your lucky number is {}'.format(name, number))

print('Your lucky number is {number}, {name}.'.format(name=name, number=len(name) * 3))


def student_grade(name, grade):
    return '{} received {}% on the exam'.format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print('Base price: ${:^6.2f}. With Tax: ${:^20.2f}.'.format(price, with_tax))


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if letter != " ":
            new_string = new_string + letter.lower()
            reverse_string = new_string[::-1]
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


# Question 4
# Fill in the gaps in the nametag function so
# that it uses the format method to return
# first_name and the first initial of last_name
# followed by a period.
# For example, nametag("Jane", "Smith") should return "Jane S."


def nametag(first_name, last_name):
    return ("{} {[0]}.".format(first_name, last_name))


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))


# Should display "Jean-Luc G."


# Question 5
# The replace_ending function replaces the old string in a
# sentence with the new string, but only if the sentence ends
# with the old string. If there is more than one occurrence of
# the old string in the sentence, only the one at the end is
# replaced, not all of them.
# For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz,
# not xyzxyz or xyzabc. The string comparison is case-sensitive,
# so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if old == sentence[-len(old):]:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

weather = 'Rainfall'
print(weather[:])

x = ['Now', 'we', 'are', 'cooking!']
print(type(x))
print(x)
print(len(x))
print('are' in x)
print('today' in x)
print(x[0])
print(x[3])
print(x[-2])
print(x[1:3])
print(x[:2])
print(x[2:])


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n-1]
    return ("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing
