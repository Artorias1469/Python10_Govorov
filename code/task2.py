#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
 string1 = input("Введите первую строку: ")
 string2 = input("Введите вторую строку: ")

 set1 = set(string1)
 set2 = set(string2)

 common_characters = set1.intersection(set2)

 if common_characters:
    print(f"Общие символы: {', '.join(common_characters)}")
 else:
    print("Общих символов нет.")
