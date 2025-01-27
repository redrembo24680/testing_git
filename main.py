num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))


def mult(num1, num2):
    print(f"result of multiply is {num1*num2}")


mult(num1, num2)


def suming(num1, num2):
    print(f"result of suming is {num1+num2}")


suming(num1, num2)


def raise_pow(num1, num2):
    print(f"result of suming is {pow(num1, num2)}")


raise_pow(num1, num2)


def subtraction(num1, num2):
    print(f"result of subtraction is {num1-num2}")


subtraction(num1, num2)


def module(num1, num2):
    print(
        f"result of first`s num module is {abs(num1)} second`s num module is {abs(num2)}")


module(num1, num2)

name = input("Enter your name: ")

def upper_case(name):
    print(name.upper())

upper_case(name)