import random
import sys


def guessing_words():
    print('Введите любую цифру от 0 до 9: ')

    lst_words = ['год', 'человек', 'время', 'статья', 'день', 'жизнь', 'дело', 'работа', 'вопрос', 'рука', 'город',
                 'слово', 'место', 'ребенок', 'друг', 'усилитель', 'мир', 'случай', 'сторона', 'дом', 'страна', 'сила',
                 'лицо', 'женщина', 'система', 'вид', 'голова', 'проблема', 'конец', 'приход', 'компания', 'история',
                 'путь', 'машина', 'вода', 'решение', 'развитие', 'программа', 'начало', 'момент', 'закон', 'число',
                 'цель', 'отец', 'правда', 'нога'
                 ]
    word = random.choice(lst_words)
    constanta = word

    def fin():
        num = input()
        while num:
            if num.isdigit():
                return word
            if num.isalpha():
                print('Будьте внимательнее! Нужно ввести цифру от 0 до 9! Попробуйте сначала!')
                return sys.exit(0)

    print(fin())

    j = 0
    s = ''
    print(f"Вы угадали: {len(s)} букв из загаданного слова")
    i = 0
    dead = ''
    while i < len(word):
        print("Осталось угадать: ", len(word), "букв")
        letter = input()
        if letter in word:
            print(f"{letter}: {word.count(letter)}")
            s += letter * (word.count(letter))
            print(s)
            print("Вы угадали: ", len(s), "букву")
            print(f'Вы угадали буквы {s} в загаданном слове')
            new_word = word.replace(letter, '')
            # print(new_word)
            word = new_word
            # print(word)

        if len(s) == len(constanta):
            print('Поздравляю! Вы угадали все слово!:', constanta)
            break
        if letter not in s:
            def fnc(j):
                v = ['!', 'O', '/', '/' + chr(92), '!', '/', '/' + chr(92)]
                return v[j]

            dead += fnc(j)
            if j <= 2:
                print('\n'.join(dead))
            if j == 3:
                new_dead = dead[:2]
                print('\n'.join(new_dead))
                print('/' + chr(92))
            if j == 4:
                new_dead = dead[:2]
                print('\n'.join(new_dead))
                print('/' + chr(92))
                print('!')
            if j == 5:
                new_dead = dead[:2]
                print('\n'.join(new_dead))
                print('/' + chr(92))
                print('!')
                print('/')
            if j == 6:
                new_dead = dead[:2]
                print('\n'.join(new_dead))
                print('/' + chr(92))
                print('!')
                print('/' + chr(92))
                print("К сожалению, вы не смогли угадать слово. Повышайте свой словарный запас "
                      "и приходите играть с новыми знаниями.")
            j += 1
    i += 1


guessing_words()
