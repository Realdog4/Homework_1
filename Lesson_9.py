import random
from string import ascii_lowercase


my_list = [
    "Goat",
    "Amber",
    "amateur",
    "Octane",
    "Baba",
    "You",
    "Turn",
    "Specs",
    "activate"]
any_list = [
    1,
    "123",
    3,
    "11",
    "22",
    33,
    "55"]
names = ["james",
         "harden",
         "kareem",
         "dwayne",
         "kevin"]
domains = ["com",
           "ua",
           "net"]


def mirror_unmatched_position(list_1):
    new_list = []
    for i, element in enumerate(list_1):
        if i % 2 == 0:
            new_list.append(element)
        else:
            new_list.append(element[::-1])

    print(new_list)


def string_find_first_a(list_2):
    new_list2 = []
    for element in list_2:
        if (element[0]) == "a":
            new_list2.append(element)
    print(new_list2)


def string_anywhere_a(list_3):
    new_list3 = []
    for element in list_3:
        if "a" in element:
            new_list3.append(element)
    print(new_list3)


def list_string_type(list_4):
    new_list = []

    for element in list_4:
        if isinstance(element, str):
            new_list.append(element)

    print("Новий список, у якому лише рядки з my_list:", new_list)


def string_frequency_one_time(string):
    unique_letters = []

    for unique_letter in string:
        if string.count(unique_letter) == 1:
            unique_letters.append(unique_letter)

    print("Символи, які зустрічаються в рядку ТІЛЬКИ ОДИН раз: ", unique_letters)


def two_or_more_times_in_strings(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    list_letters = list(set1.intersection(set2))
    print("Символи, які є в обох рядках хоча б один раз: ", list_letters)


def list_char_in_2_strings_one_time(str01, str02):
    set_1 = set(char for char in str01)
    set_2 = set(char for char in str02)

    common_symbols = set_1.intersection(set_2)

    result_str = []
    for char in common_symbols:
        if str01.count(char) == 1 and str02.count(char) == 1:
            result_str.append(char)

    print("Ці символи є в кожному рядку по одному разу: ", result_str)


def create_domains(login, host):
    i = str(random.choice(login))

    second_item = str(random.randint(100, 999))

    string_length = random.randint(5, 7)

    alphabet = list(ascii_lowercase)
    rand_symbol = []
    for s in range(string_length):
        rand_index = random.randint(0, len(alphabet)-1)
        rand_symbol.append(alphabet[rand_index])

    third = str(random.choice(host))

    result = i + "." + second_item + "@" + (''.join(rand_symbol)) + "." + third
    # print(i)
    # print(second_item)
    # print(string_length)
    # print(rand_symbol)
    # print(third)
    print(result)


mirror_unmatched_position(my_list)

string_find_first_a(my_list)

string_anywhere_a(my_list)

list_string_type(any_list)

my_str = input("Введіть будь-який текст: ")
string_frequency_one_time(my_str)

str_one = input("Введіть будь-який текст для першої строки: ")
str_two = input("Введіть будь-який текст для другої строки: ")
two_or_more_times_in_strings(str_one, str_two)

str_1 = input("Введіть будь-який текст першої строки: ")
str_2 = input("Введіть будь-який текст другої строки: ")
list_char_in_2_strings_one_time(str_1, str_2)

create_domains(names, domains)
