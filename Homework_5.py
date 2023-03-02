value_1 = (input("Please type your free mind string:"))

print("виведіть третій символ цього рядка:", value_1[2], "; введено раніше:", value_1)
print("виведіть передостанній символ цього рядка:", value_1[-1 - 1], "; введено раніше", value_1)
print("виведіть перші п'ять символів цього рядка:", value_1[0:5], "; введено раніше", value_1)
print("виведіть весь рядок, крім двох останніх символів:", value_1[0:-1 - 1], "; введено раніше", value_1)
print("виведіть усі символи з парними індексами вважаючи,\
 що індексація починається з 0,тому символи виводяться починаючи з першого:", value_1[::2], "; введено раніше", value_1)
print("виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка:", value_1[1::2],
      "; введено раніше", value_1)
print("виведіть усі символи у зворотному порядку:", value_1[::-1], "; введено раніше", value_1)
print("виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього:", value_1[::-2],
      "; введено раніше", value_1)
print("виведіть довжину цього рядка:", len(value_1), "; введено раніше", value_1)
print(
    "Дано рядок, що складається зі слів, розділених пробілами. \nВизначте, скільки у ній слів.\n Використовуйте для вирішення завдання функцію count. Відповідь:" \
    , (value_1.count(" ") + 1))
print(
    "Користувач вводить окремо рядок `s` та один символ `ch`. \nНеобхідно здійснити пошук у рядку `s` всіх символів `ch`.\nДля вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).")


def all_incomes ():
    char_type = input("Please type character to find:")
    array_total = []
    length = len(value_1)
    index = 0
    while index < length:
        ind = value_1.find(char_type, index)
        if ind == -1:
            return print("Your answer is:", array_total)
        array_total.append(ind)
        index = ind + 1


all_incomes()


#Якщо я правильно зрозумів завдання, ми повинні отримати рядок,
# де заміняємо всі указані літери (окрім першого і останнього входження цієї літери)/
# Наприклад, у рядку hhhhhh  - повинні отримати hHHHHh (h заміняємо на H)


char_type_1 = input("Please type character to replace:")
char_type_2 = input("Please enter a new character:")
index_arr = []
def getIndex ():

    length = len(value_1)
    i = 0
    while i < length:
        ind = value_1.find(char_type_1, i)
        if ind == -1:
            return index_arr
        index_arr.append(ind)
        i = ind + 1

    # new_value = value_1[change_total[0]:change_total[-1]].replace(char_type_1, char_type_2)
    # return print("Your answer is:", change_total)
getIndex ()
index_arr.pop(0)
index_arr.pop(-1)

def changeArr():
    value_arr = list(value_1)
    for i, item in enumerate(index_arr):
        value_arr[index_arr[i]] = char_type_2
    new_value = ''.join(value_arr)
    return print("Your answer is:", new_value)

changeArr ()


