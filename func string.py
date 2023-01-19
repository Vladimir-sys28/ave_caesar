# def fnc(x=0):
#     v = ['!', 'O', '/', '/' + chr(92), '!', '/', '/' + chr(92)]
#     return v[x]


# print(fnc())

# def f():
#     for num in range(10):
#         num = input()
#         if num.isdigit():
#             return 'word'
#         if num.isalpha():
#             return '!'
#             return quit(guessing_words)
def fin():
    num = input()
    while num:
        if num.isdigit() is True:
            return 'word'
        else:
            return '!'
            return quit(fin)


print(fin())



