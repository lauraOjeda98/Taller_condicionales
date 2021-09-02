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

# 3. Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

inversion1 = float(input("Ingrese la inversión de la 1era persona: "))
inversion2 = float(input("Ingrese la inversión de la 2da persona: "))
inversion3 = float(input("Ingrese la inversión de la 3era persona: "))
total = inversion1 + inversion2 + inversion3

print(f"El porcentaje por la 1era persona es de: {(inversion1/total)*100}%")
print(f"El porcentaje por la 2da persona es de: {(inversion2/total)*100}%")
print(f"El porcentaje por la 3era persona es de: {(inversion3/total)*100}%")

# 4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.

saldoInicial = float(input("Ingrese su saldo inicial: "))
meses = float(input("Ingrese el número de meses: "))
montoAhorrado = 0.015*saldoInicial*meses
saldoFinal = saldoInicial+montoAhorrado

print(f"El monto ahorrado es de: ${montoAhorrado:,}")
print(f"El saldo final es de: ${saldoFinal:,}")

# 5. Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador

sueldo = float(input("Ingrese el saldo base: "))
politica = sueldo*0.01
seguroSocial = sueldo*0.04
seguroForzoso = sueldo*0.005
ahorro = sueldo*0.05
montoTotal = sueldo - politica - seguroSocial - seguroForzoso - ahorro

print(f"El monto a descontar por la ley politica pública es de: ${politica:,}")
print(f"El monto a descontar por el seguro social es de: ${seguroSocial:,}")
print(f"El monto a descontar por seguro forzoso es de: ${seguroForzoso:,}")
print(f"El monto a descontar por caja de ahorro es de: ${ahorro:,}")
print(f"El monto total a pagar al trabajador es de: ${montoTotal:,}")

# 6. El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

numeroPalabras = float(input("Ingrese número de palabras en total: "))
tamaño = float(input("Ingrese tamaño en cm en total: "))
numeroColores = float(input("Ingrese número de colores en total: "))
montoPagar = (numeroPalabras*20000) + (tamaño*15000) + (numeroColores*25000)

print(f"El monto total a pagar por el anuncio es de: ${montoPagar:,}")

# 7. Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa.

años = int(input("Ingrese número de años laborando en la empresa: "))
if años >= 1:
    bono = 100000
    bonoFinal = ((años-1)*120000) + bono
print(f"El monto del bono es de: ${bonoFinal:,}")

# 8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

horasLaborando = float(input("Ingrese el número de horas de trabajo: "))
monto = horasLaborando*20000
descuentoAhorro = monto*0.05
totalPago = monto - descuentoAhorro

print(f"El salario por {horasLaborando} horas es de: ${monto:,}")
print(f"El monto de descuento es de: ${descuentoAhorro:,}")
print(f"El monto de total a pagar al profesor es de: ${totalPago:,}")
