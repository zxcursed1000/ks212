# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]



mode = input("Введите режим работы интерфейса (access/trunk): ")
type_int = input("Введите тип и номер интерфейса: ")

if mode == 'access':
    number = input('Введите номер VLAN:')
    print("interface", type_int)
    print("switchport mode access",
    f"switchport access vlan {number}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable" ,sep =("\n"))

elif mode == 'trunk':
    number = input('Введите разрешенные VLANы: ')
    print("interface", type_int)
    print("switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    f"switchport trunk allowed vlan {number}" , sep=("\n"))