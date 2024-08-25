def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        if type(a) is int or type(a) is float:
            a = str(a)
            result = a + b
        else:
            b = str(b)
            result = a + b
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
