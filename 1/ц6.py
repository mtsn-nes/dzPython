a = int(input())
b = 0
while a != 0:
    b += a
    a = int(input())
if b % 2 == 0:
    while b % 2 != 1:
        b = b / 2
    print("К оплате ", b)
else:
    print("К оплате ", b * 0.85)