votes = {}
candidates = ["Владимир Владимирович Путин", "Ксения Анатольевна Собчак", "Владимир Вольфович Жириновский"]

def display_candidates():
    print("Кандидаты на должность президента РФ 2024-2030:")
    for i, candidate in enumerate(candidates):
        print(f"{i + 1}. {candidate}")

def cast_vote(candidate):
    if candidate in candidates:
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1
        print(f"Ваш голос за кандидата: {candidate} - был учтен.")
    else:
        print(f"{candidate} не существует.")

if __name__ == '__main__':
    while True:
        display_candidates()
        choice = input("Выберите порядковый номер кандидата: ")
        if choice == "q":
            break
        else:
            cast_vote(candidates[int(choice) - 1])

print("Election Results:")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")