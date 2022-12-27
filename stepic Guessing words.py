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

    s = ''
    i = 0
    v = ''
    while i < len(word):
        print(len(word))

        letter = input()
        print(letter)
        if letter in word:
            s += letter
            # j = 0
        elif letter not in word:
            v += '!'
        print(v)
        i += 1
    if len(s) == len(word):
        print(len(s))
        print('Поздравляю! Вы угадали!: ', word)


guessing_words()
