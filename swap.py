

first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("Исходные значения:")
print("first_room =", first_room)
print("second_room =", second_room)

temp = first_room
first_room = second_room
second_room = temp

print("После обмена:")
print("first_room =", first_room)
print("second_room =", second_room)