#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ввести список А из 10 элементов, найти разность положительных элементов кратных 11, их
# количество и вывести результаты на экран.
if __name__ == '__main__':
    lst = [0] * 10
    count = 0
    dif = 0
    b = 0
for i in range(10):
    print("Введите", i+1, "элемент")
    lst[i] = int(input())
    if lst[i] > 0:
      if b == 0 and lst[i] % 11 == 0:
        b = lst[i]
      if lst[i] % 11 == 0:
        dif -= lst[i]
        count += 1
print("Изначальный список: ", lst, "разность положительных элементов кратных 11:", dif + (b * 2), "количество", count)