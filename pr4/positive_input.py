rejected = 0
value = int(input("Введите положительное целое число: "))

while value <= 0:
    rejected = rejected + 1
    value = int(input("Число не положительное, попробуйте снова: "))

square = value * value

print("Квадрат числа:", square)
print("Отклонённых попыток:", rejected)