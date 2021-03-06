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

def euler_solve(m, i, count):
    if i < m and math.gcd(int(m), int(i)) == 1:
        return euler_solve(m, i+1, count+1)
    elif i < m:
        return euler_solve(m, i+1, count)
    return count


def euler(a, b, m):
    print(f"Уравнение: {a}x = {b}(mod{m})")
    gcd = math.gcd(a, m)
    if b % gcd == 0 and gcd == 1:
        eul_solve = euler_solve(m, 1, 0)
        return [int((b * math.pow(a, eul_solve -1)) % m), 1, m]
    elif gcd != 1:
        a = a / gcd
        b = b / gcd
        m = m / gcd
        eul_solve = euler_solve(m, 1, 0)
        return [int((b * math.pow(a, eul_solve -1)) % m), gcd, m]
    print("Нет решений")
    return None

# first = euler(3, 4, 34)
# print(solve(first[0], first[2], first[1]))
second = euler(6, 26, 22)
print(solve(second[0], second[2], second[1]))
