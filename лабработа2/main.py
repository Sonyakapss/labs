#1
a = input("Введите число\n")
b = input("Введите число\n")
if a > b:
  print(b)
elif a < b:
  print(a)
  
  
#2
print("Введите числа:")
a = input("Число 1\n")
b = input("Число 2\n")
c = input("Число 3\n")
if a < b < c:
 print(f"Меньшее число - {a}")
elif a > b > c:
 print(f"Меньшее число - {c}")
else:
 print(f"Меньшее число - {b}")
 

#3
print("Введите числа:")
a = input("Число 1\n")
b = input("Число 2\n")
c = input("Число 3\n")
if a == b == c:
  print("У вас три одинаковых числа")
elif a == b or a == c or b == c:
  print("У вас 2 одинаковых числа")
else:
  print("Нет одинаковых чисел")
