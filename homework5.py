numbers = []
while True:
 user_input = input("Введите число (либо введите 'stop' для завершения): ")
 if user_input == 'stop':
  break
 elif user_input.isdigit():
  numbers.append(int(user_input))
 else:
  print("Некорректный ввод. Введите число или 'stop'.")
if numbers:
 total_sum = sum(numbers)
 print(f"Сумма чисел: {total_sum}")
else:
 print("Не было введено ни одного числа.")
