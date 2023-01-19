v = ['!', 'O', '/', chr(92), '!', '/', chr(92)]
dead = ''
# j = 0
for man in v:
    if man == '!':
        sim = man
        print("{:^4.9}".format(sim))
        # print(sim)
        dead += man
    elif man == 'O':
        one = man
        print("{:^4}".format(one))
        dead += man
    elif man == '/':
        print("{:>2}".format(man))
    elif man == chr(92):
        hand = '/' + chr(92)
        print("{:>3}".format(hand))
        dead += hand
print(f'Это была твоя крайняя попытка. Начни игру сначала.')
