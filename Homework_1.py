def calculate ():
    while True:
        try:
            value_digit = float(input("Add a number:"))
            break
        except ValueError:
            print("Type just a number")
    while True:
        try:
            operation = input("Please choose operation:\n'+'\n'-'\n'*'\n'/'\n ")
            if operation == '+' or operation == '-' or operation == '*' or operation == '/':
                break
        except ValueError:
            print("Try again")
    while True:
        try:
            value_another_digit = float(input("Add another number:"))
            break
        except ValueError:
            print("Type just a number")

    if operation == '+':
        print("Your answer:"'\n{} + {} ='.format(value_digit, value_another_digit), value_digit + value_another_digit)
    elif operation == '-':
        print("Your answer:"'\n{} - {} ='.format(value_digit, value_another_digit), value_digit - value_another_digit)
    elif operation == '*':
        print("Your answer:"'\n{} * {} ='.format(value_digit, value_another_digit), value_digit * value_another_digit)
    elif operation == '/':
        if value_another_digit == 0:
            while value_another_digit == 0:
                try:
                    value_another_digit = float(input("Add another number:"))
                except ValueError:
                    print('You chose the invalid characters')
        print("Your answer:"'\n{} / {} ='.format(value_digit, value_another_digit), value_digit / value_another_digit)

    def retry ():
        calc_retry = str(input('''
Do you want to calculate once again?
Please type your choice by buttons:
"Y" for Yes and "N" for stop the process '''))
        if calc_retry.upper() == 'Y':
            calculate()
        elif calc_retry.upper() == 'N':
            print("See you next time!")
        else:
            retry()

    retry()


calculate()
