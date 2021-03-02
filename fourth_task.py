import string

first_letter = ord('а')
alphabet = [chr(i) for i in range(first_letter, first_letter + 32)]
table = [[[0 for k in range(32)] for j in range(32)] for i in range(32)]
for i in range(0, 32):
    for j in range(0, 32):
        table[i][j] = alphabet[(j + i) % 32]

def full_key(text, key):
    word_key = ''
    whitespaces = 0
    for i in text:
        if (i == ' '):
            word_key += i
            whitespaces += 1
        else:
            word_key += key[(text.index(i) - whitespaces) % len(key)]
    return word_key


def encode(text, key):
    encoded = ''
    for i in range(len(text)):
        if (text[i] == ' '):
            encoded += text[i]
        else:
            encoded += table[alphabet.index(text[i].lower())][alphabet.index(key[i])]
    return encoded


def decode(text, key):
    decoded = ''
    for i in range(len(text)):
        if (text[i] == ' '):
            decoded += text[i]
        else:
            for j in range(len(alphabet)):
                if table[alphabet.index(key[i])][j] == text[i]:
                    decoded += alphabet[j]
    return decoded


with open('utils/fourth_task.txt', encoding='utf-8') as f:
    text = f.read()
    f.close()
delete_punctuation = text.maketrans(dict.fromkeys(string.punctuation))
delete_digits = text.maketrans(dict.fromkeys(string.digits))
text = text.translate(delete_punctuation).translate(delete_digits).replace("\n", '')

print(f"Текст: {text}")
key = input("Ключ: ").lower()
word_key = full_key(text, key)

encoded = encode(text, word_key)
print(f"Шифр: {encoded}")

decoded = decode(encoded, word_key)
print(f"Расшифрованный текст: {decoded}")
