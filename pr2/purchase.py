price = int(input("Введите цену одной тетради: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму: "))

cost = price * count
change = paid - cost

print("стоимость", cost, ", сдача", change)