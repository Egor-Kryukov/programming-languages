n = int(input("Введите количество чисел n: "))

total = 0
positives = 0

first = int(input("Введите число 1: "))
total = total + first
maximum = first
if first > 0:
    positives = positives + 1

for i in range(2, n + 1):
    x = int(input("Введите число " + str(i) + ": "))
    total = total + x
    if x > 0:
        positives = positives + 1
    if x > maximum:
        maximum = x

print("Сумма:", total)
print("Положительных:", positives)
print("Максимум:", maximum)