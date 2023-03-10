number_1 = int(input("Введіть перше число: "))
number = str(number_1)
zero = 0
for digit in number:
    if digit == "0":
        zero += 1

print("У цьому числі нулів:", zero)

number_2 = int(input("Введіть друге число: "))
if number_2 == 0:
     print("1 нуль")
else:
    count = 0
    while number_2 % 10 == 0 and number_2 != 0:
        count += 1
        number_2 = number_2 / 10
    print("У цьому числі ", count, " нулі в кінці")

"""Дано списки my_list_1 та my_list_2.
Створити список my_result, який спочатку помістити
елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2."""

my_list_1 = [125, 556, 45, 65, 4554, 465, 22]
my_list_2 = [155, 455, 545, 2, 10]

my_result = my_list_1[::2] + my_list_2[::2]
print("Eлементи на парних місцях: ", my_result)

"""Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]"""

my_list = [125, 586, 458, 111]
new_list = my_list[1:] + [my_list[0]]

print("Перший елемент з my_list стоїть на останньому місці", new_list)

"""Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
[1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)"""

my_list_2 = [458, 25, 46, 74]
my_list_2.append(my_list_2.pop(0))

print("Перший елемент переставити на останнє місце за допомогою методу pop: ", my_list_2)

"""Дано рядок у якому є числа (розділяються пробілами).
Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)"""

arr_text = "Маємо числа - 43 55 68"
elements_arr = arr_text.split()

sum_number = 0
for element in elements_arr:
    if element.isdigit():
        sum_number += int(element)

print("Сума всіх чисел: ", sum_number)

"""Наведено список чисел. Визначте, скільки в цьому списку елементів,
які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0."""

arr_numbers = [2, 4, 1, 5, 3, 9, 0, 7]

count_elements = 0
for i in range(1, len(arr_numbers)-1):
    if arr_numbers[i] > arr_numbers[i-1] + arr_numbers[i+1]:
        count_elements += 1

print("Кількість елементів, які більше суми двох своїх сусідів (ліворуч і праворуч): ", count_elements)

"""Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
Наприклад [1, 2, 3, "11", "22", 33]
Створити новий список у який помістити лише рядки з my_list."""

any_list = [1, "123", 3, "11", "22", 33, "55"]
new_list = []

for element in any_list:
    if isinstance(element, str):
        new_list.append(element)

print("Новий список, у якому лише рядки з my_list:", new_list)

"""Дано рядок my_str. Створити список в який помістити символи з my_str,
які зустрічаються в рядку ТІЛЬКИ ОДИН разів."""

my_str = input("Введіть будь-який текст: ")
unique_letters = []

for unique_letter in my_str:
    if my_str.count(unique_letter) == 1:
        unique_letters.append(unique_letter)

print("Символи, які зустрічаються в рядку ТІЛЬКИ ОДИН раз: ", unique_letters)

"""Дано два рядки. Створити список, у якому помістити ті символи,
які є в обох рядках хоча б один раз."""

str_one = input("Введіть будь-який текст для першої строки: ")
str_two = input("Введіть будь-який текст для першої строки: ")
set1 = set(str_one)
set2 = set(str_two)
list_letters = list(set1.intersection(set2))
print("Символи, які є в обох рядках хоча б один раз: ",list_letters)

"""Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
але в кожній ТІЛЬКИ З одного разу.
Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу"""

str_1 = input("Введіть будь-який текст першої строки: ")
str_2 = input("Введіть будь-який текст другої строки: ")

set_1 = set(char for char in str_1)
set_2 = set(char for char in str_2)

common_symbols = set_1.intersection(set_2)

result_str = []
for char in common_symbols:
    if str_1.count(char) == 1 and str_2.count(char) == 1:
        result_str.append(char)

print("Ці символи є в кожному рядку по одному разу: ", result_str)




