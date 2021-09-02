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

# 9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.

montoInicial = float(input("Ingrese el monto inical de la tarjeta: "))
montoFinal = float(input("Ingrese el monto final de la tarjeta: "))
costoLlamada = (montoInicial - montoFinal) + (montoInicial - montoFinal)*1.2

print(f"El costo de la llamada es de: ${costoLlamada:,}")

# 10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).

CantFotos = int(input("Ingrese la cantidad de fotos en el rollo: "))
valorFotos = CantFotos * 1500
ivaFotos = valorFotos * 0.16
valorTotal = valorFotos + ivaFotos

print(f"El monto total por el rollo es de: ${valorTotal:,}")

# 11. En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte conforme a la
# siguiente tabla: Area | Porcentaje Presupuestal
# Ginecología | 40%
# Traumatología | 30%
# Pediatría | 30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal.

montoPresupuestal = float(input("Ingrese el monto presupuestal: "))
ginecologia = montoPresupuestal * 0.4
traumatologia = montoPresupuestal * 0.3
pediatria = montoPresupuestal * 0.3

print(f"El monto para ginecología es de: ${ginecologia:,}")
print(f"El monto para traumatología es de: ${traumatologia:,}")
print(f"El monto para pedriatría es de: ${pediatria:,}")

# 12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a pagar.

totalPeliculas = int(input("Ingrese el número de peliculas a alquilar: "))
diasAlquiler = int(input("Ingrese el número de días de alquiler: "))

if totalPeliculas >= 2:
    montoPeliculas = (totalPeliculas - 1) * 1500 * diasAlquiler
elif totalPeliculas == 1:
    montoPeliculas = diasAlquiler * 1500

print(f"El monto total de alquiler es de: ${montoPeliculas:,}")

# 13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.

cantPersonas = int(input("Ingrese número total de personas: "))
diasTour = int(input("Ingrese número de días de tour: "))
tour = (cantPersonas * 25000 * diasTour)
ivaTour = tour * 0.12
montoTour = tour + ivaTour

print(f"El monto del tour por Cartagena es de: ${montoTour:,}")

# 14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un algoritmo que determine el valor
# total a pagar por la habitación si la estadía fue de varios días.

diasEstadia = int(input("Ingrese número de días de estadía: "))

if diasEstadia > 1:
    totalHab = ((diasEstadia - 1) * 200000) + 100000
else:
    totalHab = 100000

print(f"El total a pagar por la habitación es de: ${totalHab:,}")

# 15. El banco del Pueblo da microcréditos a empresarios para ser cancelados
# en un lapso de 2 años (24 meses). Al monto del préstamo se le cobra un
# interés del 24%. El empresario debe pagar la mitad del préstamo en 4 cuotas
# especiales y la otra mitad en 20 cuotas ordinarias. Realice un algoritmo que
# teniendo como dato de entrada el monto del préstamo, determine el monto
# total a pagar por el préstamo, el monto de las cuotas especiales y el monto
# de las cuotas ordinarias.

montoPrestamo = float(input("Ingrese el monto del préstamo: "))
interesP = montoPrestamo * 1.24
cuotasEsp = (interesP / 2) / 4
cuotasOrd = (interesP / 2) / 20

print(f"El monto total a pagar por el préstamo es de: ${interesP:,}")
print(f"El monto de las cuotas especiales es de: ${cuotasEsp:,}")
print(f"El monto de las cuotas ordinarias es de: ${cuotasOrd:,}")
