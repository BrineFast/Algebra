import math

def willson(number):
    if (math.factorial(number - 1) + 1) % number == 0:
        print(f"{number} простое")
    else:
        print(f"{number} не простое")

def fermat(number):
    for i in range(1, number * number + 1):
        if number % i != 0:
            if (pow(i, number - 1) - 1) % number == 0:
                print(f"{number} простое")
            else:
                print(f"{number} не простое")
            break

print("Критерий Вильсона: ")
willson(5)
willson(4)

print("Тест на основе малой теоремы Ферма: ")
fermat(7)
fermat(6)