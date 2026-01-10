import numpy as np

# Data analysis ДЗ №1
# Задача 1 ---------------------------------------------------------------------------------------

print('Задача 1')
temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])

min_ =  round(temps.min(), 2)
max_ =  round(temps.max(), 2)
avg = round(temps.mean(), 2)
sum_=  round(temps.sum(), 2)
print(f'Характеристики массива temps:\n'
      f'{temps}\n'
      f'- минимальный элемент: {min_}\n'
      f'- максимальный элемент: {max_}\n'
      f'- среднее элементов: {avg}\n'
      f'- сумма всех элементов: {sum_}\n')