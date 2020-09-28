#! /usr/bin/python3

class CajaAhorro:
    """Cuenta bancaria que tiene un tope de extracci�n (no se puede extraer
    m�s de cierto monto por cada operaci�n"""

    def __init__(self, titular, saldoInicial, topeExtraccion):
        self.titular = titular
        self.saldo = saldoInicial
        self.topeExtraccion = topeExtraccion

    def extraer(self, monto):
        if monto > self.topeExtraccion or monto > self.saldo:
            return "Error. Excede tope de extracci�n o saldo"
        else:
            self.saldo = self.saldo - monto
            return "Extracci�n exitosa. Saldo $" + str(self.saldo)    
    
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        return "Dep�sito exitoso. Saldo $" + str(self.saldo)

