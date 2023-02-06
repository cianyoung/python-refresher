def rot13(message):
    empty_string = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                new_value = (ord(char) - ord('a') % 13 ) % 26
                empty_string += chr(new_value + ord('a'))
    print(empty_string)
rot13('test')