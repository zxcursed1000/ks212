# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение).

В данном случае, результатом должен быть такой список: ['1', '3', '8']

Записать итоговый список в переменную result. (именно эта переменная будет
проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
i = 0
y = 0
pre_result1 = []
pre_result2 = []
lenght1 = (len(command1))
lenght2 = (len(command2))
while i < lenght1:
    s_int = ''
    while i < lenght1 and '0' <= command1[i] <= '9':
        s_int += command1[i]
        i += 1
    i += 1
    if s_int != '':
        pre_result1.append(str(s_int))

while y < lenght2:
    s_int = ''
    while y < lenght2 and '0' <= command2[y] <= '9':
        s_int += command2[y]
        y += 1
    y += 1
    if s_int != '':
        pre_result2.append(str(s_int))

def intersection(pre_result1, pre_result2):
    return list(set(pre_result1) & set(pre_result2))
result = sorted(intersection(pre_result1, pre_result2))
print(result)
