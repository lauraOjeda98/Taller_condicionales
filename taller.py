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
