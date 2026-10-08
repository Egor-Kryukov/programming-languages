

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))

group = input("Введите группу: ")
city = input("Введите ваш город: ")
fav = input("Введите ваш любимый предмет: ")
clockOnWeek = float(input("Введите количество часов: "))

newAge = age + 4
month = clockOnWeek * 4
day = round(clockOnWeek/7, 2)


print("КАРТОЧКА СТУДЕНТА")
print("ваше имя и фамилия:", name + surname)
print("Ваша фамилия:", surname)

if age < 1 or age > 120:
    print("ваш возраст: некорректный возраст")

else:
    print("Через 4 года вам будет:", newAge)
print("Ваша группа:", group)
print("Количество часов в месяц: ", month)
print("Количество часов в день: ", day)

