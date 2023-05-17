while True:
    num = input('How old are you? ')
    try:
        num = float(num)
        if num.is_integer():
            num = int(num)
            print(f'You are {num} years old.')
            break
        else:
            print('Age should be a integer.')
    except ValueError:
        print('This is not a number. Try again.')

