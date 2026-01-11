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

# Задача 2 ---------------------------------------------------------------------------------------

print('Задача 2')
h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])

sum_ = h1 + h2
product = h1 * h2
scalar = h1 @ h2
print(f'Для двух векторов:\n'
      f'h1 = {h1}\n'
      f'h2 = {h2}\n'
      f'поэлементная\n'
      f'- сумма: {sum_}\n'
      f'- произведение: {product}\n'
      f'- скалярное произведение: {scalar}\n')

# Задача 3 ---------------------------------------------------------------------------------------

print('Задача 3')
x = np.array([
[20.1, 20.3, 19.8],
[21.0, 20.7, 20.2],
[19.5, 19.8, 19.3],
[20.8, 21.1, 20.6]
])

avg_all = x.mean(axis=0).round(decimals=2)
sum_rows = x.sum(axis=1)
var = x.var(axis=0, ddof=1).round(decimals=2)
min_indices = np.where(var == var.min())[0]
print(f'Для матрицы показания температуры:\n'
      f'{x}\n'
      f'- Среднее по столбцам: {avg_all}\n'
      f'- Сумму по строкам: {sum_rows}\n'
      f'- Дисперсию по столбцам с ddof=1: {var}\n'
      f'- Индекс столбца (сенсора) с минимальной дисперсией: {min_indices}\n')

# Задача 4 ---------------------------------------------------------------------------------------

print('Задача 4')
x = np.array([
[20.1, 20.3, 19.8],
[21.0, 20.7, 20.2],
[19.5, 19.8, 19.3],
[20.8, 21.1, 20.6]
])

min_all_col = x.min(axis=0)
max_all_col = x.max(axis=0)
col_range = max_all_col - min_all_col
xx = (x - min_all_col).round(decimals=2)
xxx = (xx / col_range).round(decimals=2)

print(f'Для матрицы:\n'
      f'{x}\n'
      f'- Минимум и максимум в каждой колонке: мин: {min_all_col}, макс: {max_all_col}\n'
      f'- Размах значений в каждой колонке: {col_range}\n'
      f'- Преобразование 1:\n{xx}\n'
      f'- Преобразование 2: \n{xxx}\n')

# Задача 5 ---------------------------------------------------------------------------------------

print('Задача 5')
ph = np.array([
[7.1, 7.4, 7.0],
[6.9, 7.2, 7.1],
[7.3, 7.5, 7.2],
[7.0, 7.1, 6.8],
[6.8, 6.9, 6.7],
[7.4, 7.6, 7.3]
])
avg_ph_row = ph.mean(axis=1).round(decimals=2)
sum_ph_col = ph.sum(axis=0)
sum_all = ph.sum()
var_sample = ph.var(axis=1, ddof=1).round(decimals=2)

print(f'Для матрицы:\n'
      f'{ph}\n'
      f'- Среднее pH каждой пробы (по строкам): {avg_ph_row}\n'
      f'- Сумма значений pH для каждого образца: {sum_ph_col}\n'
      f'- Сумма значений pH всех образцов: {sum_all}\n'
      f'- Дисперсию по образцам с ddof=1: {var_sample}\n')

# Задача 6 ---------------------------------------------------------------------------------------

print('Задача 6')
consumption = np.array([
[ 8, 6, 5],   # Mon
[10, 7, 6],   # Tue
[ 9, 8, 7],   # Wed
[11, 10, 9],  # Thu
[14, 12, 11], # Fri
[16, 15, 13], # Sat
[12, 11, 10]  # Sun
])
days = np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
houses = np.array(['H1','H2','H3'])

sum_col = consumption.sum(axis=0)
sum_row = consumption.sum(axis=1)
avg_col = consumption.mean(axis=1).round(decimals=2)
max_ind = np.where(sum_row == sum_row.max())[0]
valid_max_ind = max_ind[max_ind < len(days)]
day_max = days[valid_max_ind]
var_col = consumption.var(axis=0, ddof=1).round(decimals=2)
min_ind = np.where(var_col == var_col.min())[0]
valid_min_ind = min_ind[min_ind < len(houses)]
houses_best = houses[valid_min_ind]
explanation = (f'Вывод: В данном доме наблюдается наименьший разброс значений потребления электроэнергии от\n'
               f'        среднего значения, что говорит о кучности данных и предсказуемости потребления электроэнергии')
print(f'Для матрицы:\n'
      f'{consumption}\n'
      f'- Общее энергопотребление за неделю для каждого дома: {sum_col}\n'
      f'- Общее потребление по дням: {sum_row}\n'
      f'- Среднее энергопотребление в каждом доме: {avg_col}\n'
      f'- День с наибольшим суммарным потреблением электроэнергии: ',*day_max,'\n'
      f'- Дисперсия потребления в каждом доме ddof=1: {var_col}\n'
      f'- Наиболее стабильный дом по потреблению: ',*houses_best,'\n\n',explanation,'\n')

# Задача 7 ---------------------------------------------------------------------------------------

print('Задача 7')
sensors = np.array([
[15, 101, 20, 0.5],
[16, 100, 21, 0.6],
[15, 102, 19, 0.4],
[17, 103, 22, 0.7],
[18, 104, 23, 0.6],
[19, 105, 24, 0.8],
[17, 103, 22, 0.5]
])
types = np.array(['TempSensor','PressureSensor','FlowSensor','VibrationSensor'])

sum_each_sensor = sensors.sum(axis=0)
avg_each_sensor = sensors.mean(axis=0).round(decimals=2)
var_each_sensor = sensors.var(axis=0, ddof=1).round(decimals=2)
ind_max_sum_each_sensor = np.where(sum_each_sensor == sum_each_sensor.max())[0]
valid_ind_max_sum_each_sensor = ind_max_sum_each_sensor[ind_max_sum_each_sensor < len(types)]
sensor_type = types[valid_ind_max_sum_each_sensor]
explanation = '''
- 5. Судя по предоставленной информации нам нечего вам рекомендовать, так как:
- мало измерений для аналитических данных;
- представленные датчики разных типов, что говорит о разных величинах измеряемых значений, особенно это касается 
  датчиков - PressureSensor и VibrationSensor и сравнивать их между собой не имеет смысла;
- не известно, являются ли характеристики датчиков одинаковыми;
- входной сигнал никак не может охарактеризовать сам датчик, входной сигнал это характеристика линии сигнала;
- если учитывать, что все представленные датчики имеют одинаковые характеристики и получают каждый день эталонные 
  значения равные их среднему из таблицы:
  16.71  102.57  21.57  0.59 (TempSensor,PressureSensor,FlowSensor,VibrationSensor)
  тогда датчик VibrationSensor будет предпочтительным, так как показывает дисперсию близкую к нулю, что является очень 
  хорошим показателем, другие три датчика показываю умеренную дисперсию, что также является неплохим показателем 
  и их выбор может иметь значение при рассмотрении вопроса цена-качество.
      '''
print(f'Для матрицы:\n'
      f'{sensors}\n'
      f'- 1. Сумма показаний каждого датчика: {sum_each_sensor}\n'
      f'- 2. Среднее показание каждого датчика: {avg_each_sensor}\n'
      f'- 3. Дисперсия каждого датчика: {var_each_sensor}\n'
      f'- 4. Датчики с наибольшей суммарной величиной:', *sensor_type, explanation
      )