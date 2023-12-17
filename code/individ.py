#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
 A = {'c', 'e', 'h', 'n'}
 B = {'e', 'f', 'k', 'n', 'x'}
 C = {'b', 'c', 'h', 'p', 'r', 's'}
 D = {'b', 'e', 'g'}

 X = (A - B) & (C | D)
 Y = (A - B) | (C - D)

 print("Результат X:", X)
 print("Результат Y:", Y)
