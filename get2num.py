def get_num1():
    while True:
        num1 = input("Please give me a number: ")
        try:
            num1 = int(num1)
        except ValueError:
            print("This is not a number. Please try again.")
        else:
            return num1


def get_num2():
    while True:
        num2 = input("Please give me another number: ")
        try:
            num2 = int(num2)
        except ValueError:
            print("This is not a number. Please try again.")
        else:
            return num2


def get_sum():
    num1 = get_num1()
    num2 = get_num2()
    print(num1 + num2)


get_sum()
