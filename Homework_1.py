
while True:
 try:
  value_digit = float(input("Add a number:"))
  break
 except:
  print("Type just a number")

operation = input("Please choose operation:\n'+'\n'-'\n'*'\n'/'\n ")

while True:
 try:
  value_another_digit = float(input("Add another number:"))
  break
 except:
  print("Type just a number")

if operation == '+':
 print("Your answer:"'\n{} + {} ='.format(value_digit,value_another_digit), value_digit + value_another_digit)
elif operation == '-':
 print("Your answer:"'\n{} - {} ='.format(value_digit,value_another_digit), value_digit - value_another_digit)
elif operation == '*':
 print("Your answer:"'\n{} * {} ='.format(value_digit,value_another_digit), value_digit * value_another_digit)
elif operation == '/':
 if value_another_digit == 0:
  while value_another_digit == 0:
   try:
     value_another_digit = float(input("Add another number:"))
   except:
    print('Try again')
 print("Your answer:"'\n{} / {} ='.format(value_digit, value_another_digit), value_digit / value_another_digit)








