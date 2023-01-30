nik = input()
print("тимур запретил букву а")
alphabet = 'aбвгдежзиклмнопрстуфхцчшщъыьэюя'
i = 0
name = f'{nik} запретил букву'
new_name = name
for j in alphabet:
    if j in name:
        new_name = name.replace(j, '')
        name = new_name
        print(new_name + ' ' + j)
