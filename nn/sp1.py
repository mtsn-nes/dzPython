games = []

while True:
    game = input()
    if game == "0":
        break
    if game in games:
        print("Эта игра уже записана")
    else:
        games.append(game)
        games.sort()
        print("Игра добавлена")
print("Список игр:", games)