
import math

def solve(result, m,count):
    if count > 0:
        print(f"Решение: {result}")
        return solve(result + m, m, count - 1)
    return None

def last_frac(p0, p1, i, count, nums):
    if (i < count - 1):
        return last_frac(p1, nums[i] * p1 + p0, i + 1, count, nums)
    return p1

def fraction_con(x, num, coefs):
    if num > 0.00001 and len(coefs) == 0:
        a = int(x)
        x0 = x - float(a)
        coefs.append(a)
        return fraction_con(a, x0, coefs)
    elif num > 0.00001 and len(coefs) != 0:
        a = int(1/ num)
        x0 = 1 / num - a
        coefs.append(a)
        return fraction_con(a, x0, coefs)
    return coefs

def euclid(a, b, m):
    print(f"Уравнение: {a}x = {b}(mod{m})")
    gcd = math.gcd(a, m)
    if b % gcd == 0 and gcd == 1:
        n = fraction_con(m / a, 1, [])
        x0 = NotImplemented
        if math.pow(-1, len(n) - 1) > 0:
            x0 = (math.pow(-1, len(n) - 1) * last_frac(1, n[0], 1, len(n), n) * b) % m
        else:
            x0 = (last_frac(1, n[0], 1, len(n), n) * b) % 11 * math.pow(-1, len(n) - 1)
        return [x0, len(n), m]
    elif gcd != 1:
        a = a / gcd
        b = b / gcd
        m = m / gcd
        n = fraction_con(m / a, 1, [])
        if math.pow(-1, len(n) - 1) > 0:
            x0 = (math.pow(-1, len(n) - 1) * last_frac(1, n[0], 1, len(n), n) * b) % m
        else:
            x0 = (last_frac(1, n[0], 1, len(n), n) * b) % 11 * math.pow(-1, len(n) - 1)
        return [x0, len(n), m]
    print("Нет решений")
    return None

def homomorphism(n, m):
    euclid_val = euclid(n, 0, m)
    solve(euclid_val[0], euclid_val[2], math.gcd(n, m))
    print(f"Гомоморфизмов: {math.gcd(n, m)}")

homomorphism(40, 60)