
total = int(input("Введите общий объём (количество книг): "))
capacity = int(input("Введите вместимость одной единицы (книг в коробке): "))

full_units = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print("Полностью заполненных коробок:", full_units)
print("Остаток книг:", remainder)
print("Минимальное число коробок:", min_units)

