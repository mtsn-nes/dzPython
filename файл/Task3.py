"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""
a = input('введите название файла: ')
with open("FileforTask3.txt", "r") as f, open(f'{a}.txt', "w") as fa:
    for i, line in enumerate(f):
        fa.write(f'{i+1}: {line}')