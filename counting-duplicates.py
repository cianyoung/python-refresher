"""Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'

Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python
"""

text = "annnbbcde"

def duplicate_count(text):
# Your code goes here
    total = 0
    duplicates = {}
    for character in text.lower():
        if character in duplicates:
            duplicates[character] += 1
        else:
            duplicates[character] = 1

    print(f'\nThere are {total} reoccurring characters.')
    for element in duplicates:
        if duplicates[element] > 1:
            print(f'\t"{element}" occurs {duplicates[element]} times.')

duplicate_count(text)
