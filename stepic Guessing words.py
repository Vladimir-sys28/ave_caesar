import random


def guessing_words():
    print('Введите любую цифру от 0 до 9: ')
    num = input()
    lst_words = ['год', 'человек', 'время', 'статья', 'день', 'жизнь', 'дело', 'работа', 'вопрос', 'рука', 'город',
                 'слово', 'место', 'ребенок', 'друг', 'усилитель', 'мир', 'случай', 'сторона', 'дом', 'страна', 'сила',
                 'лицо', 'женщина', 'система', 'вид', 'голова', 'проблема', 'конец', 'приход', 'компания', 'история',
                 'путь', 'машина', 'вода', 'решение', 'развитие', 'программа', 'начало', 'момент', 'закон', 'число',
                 'цель', 'отец', 'правда', 'нога'
                 ]
    word = random.choice(lst_words)
    if num.isdigit():
        if int(num) in range(9):
            print(word)
        else:
            print('Будьте внимательнее! Нужно ввести только одну цифру от 0 до 9!')
    else:
        print('Будьте внимательнее!')
    j = 0
    s = ''
    print(len(s))
    i = 0
    v = ['!', 'O', '/', chr(92), '!', '/', chr(92)]
    while i < len(word):
        print("Всего в загаданном слове ", len(word), "букв")
        letter = input()
        # print(letter)
        if letter in word:
            s += letter
            print("Вы угадали: ", len(s), "букву")
            print(s)
        if len(s) == len(word):
            print('Поздравляю! Вы угадали все слово!: ', word)
            break
        elif letter not in word:
            while j <= len(v):
                print(v[j])
                j += 1
                break
    i += 1


guessing_words()
