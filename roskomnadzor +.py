nik = input()
print(f"{nik} запретил букву а")
alphabet = 'aбвгдежзиклмнопрстуфхцчшщэюя'
name = f'{nik} запретил букву'
new_name = name[::-1]
for j in range(len(alphabet)):
    if j == 0:
        new_name = ''.join(new_name.split('а'))
        name = new_name[::-1]
        # print(new_name[::-1] + ' ' + alphabet[1])
    if j == 1:
        new_name = ''.join(new_name.split('а'))
        name = new_name[::-1]
        # print(new_name[::-1] + ' ' + alphabet[1])
    if alphabet[j] in name:
            new_name = ''.join(new_name.split(alphabet[j - 1]))
            name = new_name
            print(new_name[::-1] + ' ' + alphabet[j])
