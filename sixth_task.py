import string

first_letter = ord('а')
alphabet = [chr(i) for i in range(first_letter, first_letter + 32)]
alphabet += list(string.punctuation)
alphabet += list(string.digits)
alphabet += list(string.whitespace)
codes = list(map(lambda letter: '0' * (6 - len(format(alphabet.index(letter), 'b')))
                                + format(alphabet.index(letter), 'b'), alphabet))

with open('utils/sixth_task.txt', encoding='utf-8') as f:
    text = list(f.read().lower())
    f.close()

def generate_key(states):
    output = ''
    count = 0
    length = pow(2, len(states)) - 1
    while count < length:
        next_el = int(states[0]) ^ int(states[-1])
        output += str(states[-1])
        states.insert(0, next_el)
        del states[-1]
        count += 1
    return output

def encrypt():
    text_code = list(map(lambda x: codes[alphabet.index(x)], text))
    xor = list(map(lambda x: format(int(x, 2) ^ key, 'b'), text_code))
    return list(map(lambda x: alphabet[int(x, 2) % len(alphabet)], xor)), xor


def decryption(xor):
    text_code = list(map(
        lambda letter: '0' * (6 - len(format(int(letter, 2) ^ key, 'b')))
                       + format(int(letter, 2) ^ key, 'b'), xor))
    return list(map(lambda letter: alphabet[int(letter, 2)], text_code))

global key
key = int(generate_key(input("Ввеидет состояния: ").split()))

print(f"Ключ: {key}")
encoded, xor = encrypt()
print(f"Шифр: {''.join(encoded)}")
decoded = decryption(xor)
print(f"Расшифровка: {''.join(decoded)}")