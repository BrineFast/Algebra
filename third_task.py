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
    with open('third_task.txt', encoding='utf-8') as f:
        text = f.read()
        f.close()
        delete_punctuation = text.maketrans(dict.fromkeys(string.punctuation))
        delete_digits = text.maketrans(dict.fromkeys(string.digits))
        text = text.translate(delete_punctuation).translate(delete_digits).replace("\n", '')
    return ''.join(list(map(lambda x: alphabet[(alphabet.index(x.lower()) * n + k) % len(alphabet)], text)))


def decryption(text, n):
    reversed_element = 0
    for i in range(1, len(alphabet)):
        if (i * n) % len(alphabet) == 1:
            reversed_element = 1
            break
    return ''.join(list(
        map(lambda x: alphabet[((alphabet.index(x) - k + len(alphabet)) * reversed_element) % len(alphabet)], text)))


n, k = gcd_check()
print(len(alphabet))
encrypted = encrypt(n, k)
decrypted = decryption(encrypted, n)
print(encrypted)
print(decrypted)
