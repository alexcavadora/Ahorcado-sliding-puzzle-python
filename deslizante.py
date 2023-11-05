#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:31:43 2023

@author: navi

"""

import random as rn
n = 1
seguir = 's'
print('Instrucciones: puedes controlar el número 0, mediante las teclas w, a, s, d, que indican arriba, izquierda, abajo y derecha respectivamente. Ordena los números del 1 al 15 dejando el 0 en la última casilla.')

#repite el juego tantas veces quieras
while seguir == 's':
    while n % 2 == 1:
        n = 0
        
        numbers = [i+1 for i in range(15)] #se genera una lista con los números del 1 al 15
        rn.shuffle(numbers) # se randomiza la lista (2D), si se comenta se puede debuggear la victoria.
        for i in range(len(numbers)):
            for j in range(i):
                if numbers[j] > numbers [i]: #se comprueba que sea posible resolver, de lo contrario genera una distinta hasta hallar una.
                    n+=1
    numbers.append(0) #al final del todo, se agrega el 0 y se convierte en matriz 4x4
    matrix = [numbers[:4],
              numbers[4:8],
              numbers[8:12],
              numbers[12:16]]
    x, y = 3, 3 #se inicializan las coordenadas del hueco, están siempre en la esquina inferior derecha
    solved = False #está no resuelto, (la mayoría del tiempo)
    while not solved:
        for i in matrix: # se imprime la matriz, se usa un operador ternario para imprimir los números de 2 dígitos sin espacio y los de 1 con espacio
            print('╔═══╗╔═══╗╔═══╗╔═══╗')
            print(f'║ {i[0]}{(" ","")[i[0] > 9]}║║ {i[1]}{(" ","")[i[1] > 9]}║║ {i[2]}{(" ","")[i[2] > 9]}║║ {i[3]}{(" ","")[i[3] > 9]}║')
            print('╚═══╝╚═══╝╚═══╝╚═══╝')
        print('\n')
        
        prev = 0
        solved = True
        for i in matrix: #se comprueba que esté resuelto, al comprobar que los números siguan una secuencia ascendente
            for j in i:
                if j != prev+1 and j != 0:
                    solved = False
                else:
                    prev = j
        if solved:
            continue
        
        #se pide un movimiento
        move = input('move (↑w, ←a, ↓s, →d): ').lower()
        
        #lógica de movimiento, se intercambia la casilla en la dirección elegida, de ser posible lo hace, de lo contrario da error.
        if move == 'w':
            if y > 0:
                matrix[y][x] = matrix[y-1][x]
                matrix[y-1][x] = 0
                y -= 1
            else:
                print('¡No se puede mover más hacia arriba!')
            
        elif move == 'a':
            if x > 0:
                matrix[y][x] = matrix[y][x-1]
                matrix[y][x-1] = 0
                x -= 1
            else:
                print('¡No se puede mover más la izquierda!')
            
        elif move == 's' :
            if y < 3:
                matrix[y][x] = matrix[y+1][x]
                matrix[y+1][x] = 0
                y += 1
            else:
                print('¡No se puede mover más hacia abajo!')
            
        elif move == 'd':
            if x < 3:
                matrix[y][x] = matrix[y][x+1]
                matrix[y][x+1] = 0
                x += 1
            else:
                print('¡No se puede mover más la derecha!')
        else:
            print('Tecla desconocida.')
        
    else:
        print('¡Felicidades!, has ganado')
        seguir = input('¿Desea jugar otra vez? (s/n): ').lower()

    


