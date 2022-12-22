text = input()


def sdvig():
    count = 0
    s = []
    for i in range(len(text)):
        if text[i].isalpha():
            count += 1
        elif not text[i].isalpha():
            s.append(count)
            count = 0
    s = [x for x in s if x != 0]
    return s


sdvig()
z = sdvig()
# print(z)
# print(len(z))


# y = 0
for y in range(len(z)):
    # print(text[y])
    alf_low = ['абвгдежзийклмнопрстуфхцчшщъыьэюя' * 2, 'abcdefghijklmnopqrstuvwxyz' * 2]
    alf_upp = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2]
    language = 1
    action = 0
# text = input('Введите исходный текст: ')
    key = z[y] % [32, 26][language]
    result_text = ''
    for c in text:
        if c.isalpha() and c.islower():
            result_text += alf_low[language][
                alf_low[language].find(c) + len(alf_low[language]) // 2 * action + [1, -1][action] * key]
        elif c.isalpha() and c.isupper():
            result_text += alf_upp[language][
                alf_upp[language].find(c) + len(alf_low[language]) // 2 * action + [1, -1][action] * key]
        else:
            result_text += c

    print(result_text)
for u in range(len(z)):
    print(u, end=' ')
