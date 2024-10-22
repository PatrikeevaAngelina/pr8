def print_integers_between(a, b):
 # Сортируем числа, чтобы a всегда было меньше b
 if a > b:
  a, b = b, a
 # Выводим целые числа
 for i in range(int(a), int(b) + 1):
  print(i)
if __name__ == "__main__":
 a = float(input("Введите первое число: "))
 b = float(input("Введите второе число: "))
 print_integers_between(a, b)
