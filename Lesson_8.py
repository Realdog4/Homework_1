""""1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range."""

my_list = ["Goat",
           "Amber",
           "amateur",
           "Octane",
           "Baba",
           "You",
           "Turn",
           "Specs",
           "activate"]
# print(my_list)
new_list = []
for i, element in enumerate(my_list):
    if i % 2 == 0:
        new_list.append(element)
    else:
        new_list.append(element[::-1])
print(new_list)
"""2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
у яких перший символ - буква "a".
"""
new_list2 = []
for element in my_list:
    if (element[0]) == "a":
        new_list2.append(element)
print(new_list2)
"""3. Наведено список рядків my_list. Створити новий список до якого помістити
елементи з my_list, у яких є символ - буква "a" на будь-якому місці."""
new_list3 = []
for element in my_list:
    if "a" in element:
        new_list3.append(element)
print(new_list3)
"""4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]"""
people_list = [{"name": "John",
                "age": 13},
               {"name": "Matthew",
                "age": 14},
               {"name": "Alexander",
                "age": 26},
               {"name": "Isaiah",
                "age": 13},
               {"name": "Dominique",
                "age": 22},]

# print(people_list)
list_max_name = []
list_average_age = []
"""а) Створити список і помістити туди ім'я наймолодшої людини. 
Якщо вік збігається – помістити всі імена наймолодших."""
ages = {user["name"]: user["age"] for user in people_list}
min_age = min(ages.values())
youngest_names = [name for name, age in ages.items() if age == min_age]
print(youngest_names)
"""б) Створити список та помістити туди найдовше ім'я.
 Якщо довжина імені збігається - помістити такі імена."""
max_name = 0
names = [name["name"] for name in people_list]
for element in names:
    if len(element) > max_name:
        list_max_name = [element]
        max_name = len(element)
    elif len(element) == max_name:
        list_max_name.append(element)
print(list_max_name)
"""в) Порахувати середню вік усіх людей із початкового списку.
"""
average_ages = [age["age"] for age in people_list]
sum_age = sum(average_ages) / len(average_ages)
print(sum_age)
"""5) Дано два словники my_dict_1 і my_dict_2."""
my_dict_1 = {1: 20,
             2: 15,
             14: 20,
             5: 40,
             30: 480,
             16: 20,
             0: 180,
             }
my_dict_2 = {1: 450,
             3: 50,
             14: 20,
             6: 7300,
             29: 20,
             16: 620,
             7: 10,
             }
"""а) Створити список із ключів, які є в обох словниках."""
intersection_keys = list(my_dict_1.keys() & my_dict_2.keys())
print(intersection_keys)
"""б) Створити список із ключів, які є у першому, але немає у другому словнику."""
subtraction_keys = list(my_dict_1.keys() - my_dict_2.keys())
print(subtraction_keys)
"""в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику."""
res = {key: my_dict_1[key] for key in set(my_dict_1) - set(my_dict_2)}
print(res)
"""г) Об'єднати ці два словники у новий словник за правилом:
якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}"""
dict_update = {}
for key1 in set(my_dict_1.keys()).union((my_dict_2.keys())):
    if key1 in my_dict_1 and key1 not in my_dict_2:
        dict_update[key1] = my_dict_1[key1]
    elif key1 in my_dict_2 and key1 not in my_dict_1:
        dict_update[key1] = my_dict_2[key1]
    else:
        dict_update[key1] = [my_dict_1[key1], my_dict_2[key1]]
# print(set(my_dict_1.keys()).union((my_dict_2.keys())))
# print(my_dict_2.keys())
# print(my_dict_1.keys())
print(dict_update)
















