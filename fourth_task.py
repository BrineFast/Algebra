import string

first_letter = ord('а')
alphabet = [chr(i) for i in range(first_letter, first_letter + 32)]
alphabet += list(string.punctuation)
alphabet += list(string.digits)
alphabet += [' ']
codes = list(map(lambda x: '0' * (6 - len(list(map(bin, bytearray(alphabet.index(x))))))
                           + ''.join(map(bin, bytearray(alphabet.index(x)))), alphabet))

def encrypt():
    with open('file.txt', encoding='utf-8') as f:
        text = list(f.read().lower())
        f.close()
        key = "101010"
        text_code = list(map(lambda x: codes[alphabet.index(x)], text))
        xor = list(map(lambda x: ''.join(map(bin, bytearray(int(x, 2) ^ int(key, 2)))), text_code))
        return list(map(lambda x: alphabet[int(x, 2) % len(alphabet)], xor))

def decryption(text):
    return ''.join(list(map(lambda x: alphabet[(alphabet.index(x) - k + len(alphabet)) % len(alphabet)], text)))


encrypted = encrypt()
decrypted = decryption(encrypted)
print(encrypted)
print(decrypted)