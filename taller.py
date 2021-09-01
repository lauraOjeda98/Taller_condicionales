# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:13:45 2021

@author: Laura Ojeda Méndez
"""

# 1. y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3

# Declaramos 'y' e ingresamos los operandos y valores a operar
y = ((5+2-5)**2 * 5+8/2 - 30) / 2*5-3
print(f"EL valor de Y en el 1er punto es de: {y}")

# 2. z=5, n=3, m= z-n
# y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3

# Declaramos las variables
z = 5
n = 3
m = z - n

# Declaramos 'y' e ingresamos los operandos y valores a operar
y = (((z+2-n)**2 * m+8/2-30) / 2*5-3)**5 + 15*3 - 9/3
print(f"EL valor de Y en el 2do punto es de: {y}")

# 3. z=5, n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3, m= z^2*3+n
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4

# Declaramos las variables, realizamos las operaciones con estas e imprimimos Y
z = 5
n = ((8+2-4)**2 * 5+8+7/2 - 30*5) / 2*5-3
m = z**2 * 3+n
y = ((((z+2-n)**2 * m+8/2-30) / 2*5-3)**5 + 15*3-9/3)**2 - 5/4
print(f"EL valor de Y en el 3er punto es de: {y}")

# --- SEGUNDA SECCIÓN ---

# 1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))

presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f"Con una presion de {presion}")
print(f"Con un volumen de {volumen}")
print(f"Y una temperatura de {temperatura}")
print(f"El resultado de la masa es igual a {masa}")

# 2. Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.

edad = int(input("Ingrese su edad: "))
num_pulsacion = (200 - edad) / 10
print(f"El número de pulsaciones cada 10 seg debe ser de: {num_pulsacion}")
