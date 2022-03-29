def myfunc(string):

    lower_count = 0
    upper_count = 0

    for letter in string:
        if letter.islower():
            lower_count += 1
        elif letter.isupper():
            upper_count += 1

    print(f'Number of Lower case characters: {lower_count}')
    print(f'Number of Upper case characters: {upper_count}')

myfunc('Hello Mr. Rogers, how are you this fine Tuesday?')