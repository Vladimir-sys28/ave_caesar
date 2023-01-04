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
    # j = 0
    s = ''
    print(f'Угадано: {len(s)} букв')
    i = 0
    v = ['!', 'O', '/', chr(92), '!', '/', chr(92)]
    dead = ''
    k = 0

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
        if letter not in word:
            j = 0
            # while j <= len(v):
            while j <= len(v):
                for man in range(len(v)):
                    if man == 0:
                        sim = '!'
                        dead += sim
                        print(sim)
                        break
            # for man in v:
                    if man == 1:
                        one = man
                        print(one)
                        dead += man
                        break
            # for man in v:
            #     if man == '/':
            #         print(man)
            #         break
            # for man in v:
            #     if man == chr(92):
            #         hand = '/' + chr(92)
            #         print(hand)
            #         dead += hand
            #         break


            j += 1

                    # dead = ''.join(chr(92))
                    # print(dead)
                    # print(j)

                # else:
                #     dead += v[j]
                #     print('\n'.join(dead))
                # j += 1
                # break
    i += 1


guessing_words()
print(f'Это была твоя крайняя попытка. Начни игру сначала.')