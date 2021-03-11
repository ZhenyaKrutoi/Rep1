list_per = list(map(float, input("Введите числа:"
                                 " ").split()))
a = round(sum(list_per), 2)
b = max(list_per)
for i in range(1, len(list_per)+1):
    round(list_per[i-1])
print("ваши округленные числа:\n", list_per)
print("Сумма трех чисел: %s \n"
      "Максимальное число: %s \n" % (a, b))
