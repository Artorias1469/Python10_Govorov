#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_vowels(input_string):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in input_string if char in vowels)

if __name__ == "__main__":
    user_input = input("Введите строку: ")

    result = count_vowels(user_input)
    print(f"Количество гласных в введенной строке: {result}")
