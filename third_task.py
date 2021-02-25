import string

first_letter = ord('а')
alphabet = [chr(i) for i in range(first_letter, first_letter + 32)]
alphabet += list(string.punctuation)
alphabet += list(string.digits)
alphabet += [' ']

def gcd_check():
    n = int(input('n: '))
    k = int(input('k: '))
    m = len(alphabet)
    while n != 0 and m != 0:
        if n > m:
            n %= m
        else:
            m %= n


    if n + m != 1:
        raise Exception('Неверный ввод')
    return n, k

def encrypt(n, k):
    with open('file.txt', encoding='utf-8') as f:
        text = list(f.read().lower())
        f.close()
        return ''.join(list(map(lambda x: alphabet[(alphabet.index(x) * n + k) % len(alphabet)], text)))

def decryption(text):
    return ''.join(list(map(lambda x: alphabet[(alphabet.index(x) - k + len(alphabet)) % len(alphabet)], text)))

n, k = gcd_check()
encrypted = encrypt(n,k)
decrypted = decryption(encrypted)
print(encrypted)
print(decrypted)