"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""
sentence = 'aeioufaisaaea'

def get_count(sentence):
    print(sum(c in 'aeiou' for c in sentence))

get_count(sentence)