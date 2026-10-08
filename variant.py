

order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

item1_name = input("Введите название первой позиции: ")
item1_qty = int(input("Введите количество первой позиции: "))
item1_price = float(input("Введите цену за единицу первой позиции: "))

item2_name = input("Введите название второй позиции: ")
item2_qty = int(input("Введите количество второй позиции: "))
item2_price = float(input("Введите цену за единицу второй позиции: "))

delivery_cost = float(input("Введите стоимость доставки: "))
paid_amount = float(input("Введите внесённую сумму: "))

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
items_total = item1_total + item2_total
grand_total = items_total + delivery_cost
total_qty = item1_qty + item2_qty
change = paid_amount - grand_total

print()
print("Заказ:", order_name)
print("Заказчик:", customer_name)
print()
print(item1_name, "|", item1_qty, "|", format(item1_price, ".2f"), "|", format(item1_total, ".2f"))
print(item2_name, "|", item2_qty, "|", format(item2_price, ".2f"), "|", format(item2_total, ".2f"))
print()
print("Стоимость товаров без доставки:", format(items_total, ".2f"))
print("Стоимость доставки:", format(delivery_cost, ".2f"))
print("Общая сумма с доставкой:", format(grand_total, ".2f"))
print("Общее количество единиц:", total_qty)
print("Сдача:", format(change, ".2f"))