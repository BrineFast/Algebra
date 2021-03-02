import string

first_letter = ord('а')
alphabet = [chr(i) for i in range(first_letter, first_letter + 32)]
alphabet += list(string.punctuation)
alphabet += list(string.digits)
alphabet += list(string.whitespace)
codes = list(map(lambda letter: '0' * (6 - len(format(alphabet.index(letter), 'b')))
                                + format(alphabet.index(letter), 'b'), alphabet))

with open('utils/fifth_task.txt', encoding='utf-8') as f:
    text = list(f.read().lower())
    f.close()
key = "101010"
key = int(key, 2)


def encrypt():
    text_code = list(map(lambda x: codes[alphabet.index(x)], text))
    xor = list(map(lambda x: format(int(x, 2) ^ key, 'b'), text_code))
    return list(map(lambda x: alphabet[int(x, 2) % len(alphabet)], xor)), xor


def decryption(xor):
    text_code = list(map(
        lambda letter: '0' * (6 - len(format(int(letter, 2) ^ key, 'b')))
                       + format(int(letter, 2) ^ key, 'b'), xor))
    return list(map(lambda letter: alphabet[int(letter, 2)], text_code))


encoded, xor = encrypt()
print(f"Шифр: {''.join(encoded)}")
decoded = decryption(xor)
print(f"Расшифровка: {''.join(decoded)}")
