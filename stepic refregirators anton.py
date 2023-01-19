n = int(input())
word = 'anton'
index = 0
j = 0
k = 0
s = ''
s_out = ''
while k < n:
    st = input()
    k += 1
    s += st
    for i in range(len(s)):
        if s[i] == word[index]:
            index += 1
            if index == 5:
                j += 1
                s_out += str(j)
                s = ''
                index = 0
                break
        else:
            if index < 5 and i == len(st) - 1:
                j += 1
                s_out += ' '
                s = ''
                index = 0
                break
print(' '.join(s_out))
