import csv
import string

with open('first_second_tasks.txt', encoding='utf-8') as f:
    text = f.read()
    first_letter = ord('а')
    delete_punctuation = text.maketrans(dict.fromkeys(string.punctuation))
    delete_digits = text.maketrans(dict.fromkeys(string.digits))
    delete_whitespaces = text.maketrans(dict.fromkeys(string.whitespace))
    text = text.translate(delete_punctuation).translate(delete_digits).translate(delete_whitespaces).lower()
    table = dict([(chr(i), 0) for i in range(first_letter, first_letter + 32)])
    for letter in table:
        table[letter] = round(text.count(letter) / len(text), 3)
    with open('result_first_task.csv', 'w', newline='') as f2:
        writer = csv.DictWriter(f2, table.keys(), delimiter=";")
        writer.writeheader()
        writer.writerow(table)
        f2.close()
    f.close()