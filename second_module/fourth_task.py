import math


def is_primitive(number):
    if (math.factorial(number - 1) + 1) % number == 0:
        return True
    else:
        return False


def legendre(number, primitive_number):
    if not is_primitive(primitive_number):
        raise Exception(f"Число {primitive_number} не простое")
    if (number == 0) or (number == 1):
        return number
    if number % primitive_number == 0:
        return 0
    if number % 2 == 0:
        legendre_symbol = legendre(number / 2, primitive_number)
        if primitive_number * primitive_number - 1 & 8 != 0:
            legendre_symbol *= -1
    else:
        legendre_symbol = legendre(primitive_number % number, number)
        if (number - 1) * (primitive_number - 1) & 4 != 0:
            legendre_symbol *= -1
    return legendre_symbol


print(legendre(2, 5))
