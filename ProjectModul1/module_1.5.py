'''
1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_5.py' и напишите весь код в нём.

2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
'''
immutable_var = 1 , 2 , 3 , True , 'Жёп'
print(immutable_var)

# даже пытаться не буду ,кортёж нельзя менять, если в нем нет изменяемого списка

mutable_list = ['A' , 'B' , 'C' , 'D']
mutable_list.remove('A')
mutable_list.append(13)
mutable_list.remove('B')
mutable_list.append(69)
mutable_list.remove('C')
mutable_list.append('Ilya')
mutable_list.remove('D')
mutable_list.append('Luchshi')
print(mutable_list)