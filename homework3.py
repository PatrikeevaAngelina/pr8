n = 10
#рисуем границы
for i in range(n):
  if i == 0 or i == n - 1:
    print("*" * n)
  else:
    # Рисуем боковые стороны и пустые ячейки
    print("*" + " " * (n - 2) + "*")
