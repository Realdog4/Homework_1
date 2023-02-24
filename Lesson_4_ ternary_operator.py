# 1
value1 = int(input("new_value<100 = new_value/2 or >100 ('-'new-value)\n"))
new_value1 = value1 / 2 if value1 < 100 else -value1
print(new_value1)

# 2
value2 = int(input("new_value<100 then new_value =1 or >100 new-value = 0\n"))
new_value2 = 1 if value2 < 100 else 0
print(new_value2)
# 3
value3 = int(input("new_value<100 = 'true' or  new_value >100 = 'false'\n"))
new_value3 = True if value3 < 100 else False
print(new_value3)
# 4
my_str1 = input("string length < 5 = 2 times string in line else 'string'\n")
new_value4 = (my_str1 * 2) if len(my_str1) < 5 else my_str1
print(new_value4)
# 5
my_str2 = input("string length < 5 = 'string+gnirts' or string length >5 = string\n")
new_value5 = (my_str2 + my_str2[::-1]) if len(my_str2) < 5 else my_str2
print(new_value5)
