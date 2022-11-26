try:
    num = int(input("Enter number:"))
    if num % 3  == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5  == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 3  % 5 == 0:
        print("Fizz Buzz")
except ValueError as vl_ex:
    print(f'ValueError: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')