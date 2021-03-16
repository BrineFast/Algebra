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


def jacobi(number, odd_number):
    gcd_check(number, odd_number)
    jacobi_sign = 1
    if number < 0:
        number *= -1
        if odd_number % 4 == 3:
            jacobi_sign *= -1

    while number != 0:
        step = 0
        while number % 2 == 0:
            step += 1
            number /= 2

        if step % 2 != 0 and (odd_number % 8 == 3 or odd_number % 8 == 5):
            jacobi_sign *= -1

        if number % 4 == 3 and odd_number % 4 == 4:
            jacobi_sign *= -1

        number, odd_number = odd_number % number, number
    return jacobi_sign


print(jacobi(1236, 20003))
