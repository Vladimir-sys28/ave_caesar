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
    print(f"Вы угадали: {len(s)} букв из загаданного слова")
    i = 0
    v = ['!', 'O', '/', chr(92), '!', '/', chr(92)]
    dead = ''
    while i < len(word):
        print("Всего в загаданном слове ", len(word), "букв")
        letter = input()
        # print(letter)
        if letter in word:
            s += letter
            print("Вы угадали: ", len(s), "букву")
            print(f'Вы угадали букву {s} в загаданном слове')
        if len(s) == len(word):
            print('Поздравляю! Вы угадали все слово!: ', word)
            break
        if letter not in word:
            # print(i)
            # x = 0
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
                print("К сожалению, вы не смогли угадать слово. Увеличте свой словарный запас и начните игру заново ")
            j += 1
    i += 1


guessing_words()
