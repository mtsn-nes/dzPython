"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""
b = input('введите имя файла: ')
s = {}
with open(b, 'r') as f:
    for line in f:
        words = line.strip().lower().split()
        for word in words:
            word = word.strip('.,!?')
            if word in s:
                s[word] += 1
            else:
                s[word] = 1
slova = max(s, key=s.get)
print('часто встречающиеся слово:', slova)
print('его количество в файле:', s[slova])