while True:
 a = input("Введите первое число: ")
 b = input("Введите второе число: ")
 if a.isdigit() and b.isdigit():
  a1 = int(a)
  b2 = int(b)
  sum = a1 + b2
  print(f"Сумма чисел: {sum}")
 else:
  print("Ошибка! Введите целые числа.")
