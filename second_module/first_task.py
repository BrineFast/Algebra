import math
import random

from second_module.fifth_task import jacobi
from second_module.fourth_task import legendre


def willson(number):
    if (math.factorial(number - 1) + 1) % number == 0:
        print(f"{number} простое")
    else:
        print(f"{number} не простое")

def fermat(number):
    for i in range(2, number * number + 1):
        if number % i != 0:
            if (pow(i, number - 1) - 1) % number == 0:
                print(f"{number} простое")
            else:
                print(f"{number} не простое")
            break

def gcd_check(n, m):
    if m % 2 == 0:
        raise Exception('Неверный ввод')
    while n != 0 and m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    if n + m != 1:
        raise Exception('Неверный ввод')
    return True

def solovay(n, k, i):
    if i == k:
        print(f"{i} прострое с вероятностью {1 - math.pow(2, -k)}")
        return True
    else:
        value = random.randint(2, n - 1)
        if not gcd_check(value, n) or ((math.pow(value, (n - 1) / 2) % n) != jacobi(value, n) % n):
            print(f"{i} составное")
            return False
        solovay(n, k, i+1)

def ldf(k, n):
    if n % k == 0:
        return k
    elif n <= k * k:
        return n
    return ldf(k + 1, n)


def make_factors(n, factors=None):
    if factors is None:
        factors = []
    if n == 1:
        return factors
    else:
        factor = ldf(2, n)
        factors.append(factor)
    return make_factors(n / factor, factors)


def carmichael(n, factors):
    for i in factors:
        if not ((((n - 1) % (i - 1)) == 0) and (n % (i * i) != 0)):
            return False
    return True

print("Критерий Вильсона: ")
willson(7)
willson(4)

print("Тест на основе малой теоремы Ферма:")
fermat(7)
fermat(6)

print("Тест Соловея:")
solovay(17, 100, 0)

print("Тест Кармайкла:")
print(carmichael(562, make_factors(562)))

for i in range(5, 100000):
    if carmichael(i, make_factors(i)) and len(set(make_factors(i))) >= 3:
        print(f"{i} - число Кармайкла")