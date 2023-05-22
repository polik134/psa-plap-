from random import shuffle
spisok_ingr = ['соль', 'кетчуп', 'мазик']

triks = input('Введи ингредиент:(хорош - стоп)')

while triks != 'хорош':
    if triks in spisok_ingr:
        print('Это было')

    else:
        spisok_ingr.append(triks)
    
    triks = input('Введи ингредиент:(хорош - стоп)')

spisok_blender = []

num = int(input('Сколько месим ингредиентов:'))

for event in range(num):
    shuffle(spisok_ingr)
    spisok_blender.append(spisok_ingr[0])
    spisok_ingr.remove(spisok_ingr[0])

print('Приготовь что-нибудь из:')
for event in range(num):
    print(spisok_blender[event])