subject1 = input("Введите предмет 1: ")
subject2 = input("Введите предмет 2: ")
week1 = int(input(f"Введите количество занятий в неделю для {subject1}: "))
week2 = int(input(f"Введите количество занятий в неделю для {subject2}: "))
minute1 = int(input(f"Введите продолжительность занятия {subject1} в минутах: "))
minute2 = int(input(f"Введите продолжительность занятия {subject2} в минутах: "))
timee = int(input("Введите доступное время на неделю(в часах): "))


print(f"{subject1}",minute1, "min")
print(f"{subject2}",minute2, "min")

'''
print(f"общая нагрузка для {subject1} в минутах: ", week1 * minute1)
print(f"общая нагрузка для {subject2} в минутах: ", week2 * minute2)


print(f"общая нагрузка для {subject1} в часах: ", float((week1 * minute1)/60))
print(f"общая нагрузка для {subject2} в часах: ", float((week2 * minute2)/60))
'''

print("общая нагрузка в минутах: ", (week1 * minute1) + (week2 * minute2))
print("общая нагрузка в часах: ", ((week1 * minute1) + (week2 * minute2))/60)

print(f"Нагрузка за 4 недели в часах: ", (((week1 * minute1) + (week2 * minute2))/60) *4)

print("Остаток свободного времени в часах: ", ((((week1 * minute1) + (week2 * minute2))/60)*4) - timee)

