


def swap_case(string):
    result = ''
    for i in string:
        if i.islower():
           i = i.upper()
        elif i.isupper():
           i = i.lower()
        result += i
    return result
