"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
song = dict()

place = input('введите место:\n').lower()
signer = input('введите исполнителя:\n').lower()
music = input('введите название трека:\n').lower()

while place != 'off' and signer != 'off' and music != 'off':
    song[(place, signer)] = music
    place = input('введите место:\n').lower()
    signer = input('введите исполнителя:\n').lower()
    music = input('введите название трека:\n').lower()

print(song)