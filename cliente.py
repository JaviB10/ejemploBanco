#! /usr/bin/python3
#Ponemos a disposiciÃ³n de este archivo las dos clases que utilizaremos.
from cajaAhorro import CajaAhorro
from cuentaCorriente import CuentaCorriente
from cajaAhorroEspecial import CajaAhorroEspecial

#Solicitamos datos:
nombre = input("Ingrese el nombre del titular de la cuenta ")
saldo = int(input("Ingrese el depÃ³sito inicial "))
tipo = int(input("Ingrese el tipo de cuenta: 1:Caja de Ahorro 2:CtaCte 3:Caja de Ahorro Especial "))
tope = int(input("Ingrese el tope de extracciÃ³n/descubierto "))


#SegÃºn el valor recibido en tipo, instanciamos de CajaAhorro o CuentaCorriente.
if tipo == 1:
    cuenta = CajaAhorro(nombre, saldo, tope)
elif tipo == 2:
    cuenta = CuentaCorriente(nombre, saldo, tope)
elif tipo == 3:
    depositoMinimo = int(input("Ingrese el deposito minimo: "))
    cuenta = CajaAhorroEspecial(nombre, saldo, tope, depositoMinimo)
else:
    print("Error: ingrese el tipo 1 , 2 o 3")
    exit()

#Este bucle nos permite realizar muchas operaciones.
continuar = "s"
while continuar == "s" or continuar == "S":
    print("El saldo de la cuenta es $", cuenta.saldo)
    #Solicitamos el tipo de operaciÃ³n y el monto.
    operacion = input("Ingrese el tipo de operaciÃ³n (D/E)")
    monto = int(input("Ingrese el monto de la operaciÃ³n"))

    #Invocamos al mÃ©todo polimÃ³rfico correspondiente.
    if operacion == "D" or operacion == "d":
        print(cuenta.depositar(monto))
    elif operacion == "E" or operacion == "e":
        print(cuenta.extraer(monto))
    else:
        print("Error: tipo de operaciÃ³n errÃ³nea")
    continuar = input("Â¿Realizar otra operaciÃ³n? (S/N) ")

#Para finalizar, mostramos el saldo con el que quedÃ³ la cuenta:
print("El saldo final de la cuenta es $", cuenta.saldo)
