list_int = [20,
            50,
            80,
            110,
            130,
            20,
            175,
            180,
            15,
            36
]
"""1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100.
   Завдання виконати за допомогою циклу for."""
for i in list_int:
    if i > 100:
        print(i)

"""2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
   які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for."""
my_results = []

for i in list_int:
    if i > 100:
        my_results.append(i)

print(my_results)

"""3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
   то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
   то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)"""

if len(list_int) < 2:
    list_int.extend('0')
    print(list_int)
elif len(list_int) >= 2:
    sum_ext = [list_int[-1] + list_int[-2]]
    list_int.extend(sum_ext)
    print(list_int)

