N = int(input())
languages = []
for i in range(N):
    M = int(input())
    languages.append(set(input().split()))

intersection = set.intersection(*languages)
print(len(intersection), '-', sorted(list(intersection)))

union = set.union(*languages)
print(len(union), '-', sorted(list(union)))