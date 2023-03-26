product1 = int(input())
product2 = int(input())
product3 = int(input())
total = product1 + product2 + product3
if product1 > product2 and product2 > product3:
    print("Акция!")
    print("Сумма к оплате:", total / 3)
elif product1 < product2 and product2 < product3:
    print("Акция!")
    print("Сумма оплате:", total / 2)
else:
    print("К оплате:", total)