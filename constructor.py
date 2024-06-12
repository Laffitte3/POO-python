import random

class Dolar():

    def __init__(self,raro=False):

        self.raro=raro

        if self.raro:
            self.valor=1.25
            print("Es super rara")
        else:
            self.valor= 1.0

        self.color= "dorado"
        self.num_bordes= 22.5
        self.grosor= 3.15
        self.caras = True #Si es True es cara y si es False cruz

    def oxido(self):

        self.color= "verdoso"

    def limpiar(self):
        print("Se limpio la moneda")
        self.color="dorado"

    def vueltas(self):

        caras_opciones = [True,False]
        eleccion= random.choice(caras_opciones)

        self.caras= eleccion
        print(self.caras)

    def __del__(self):

        print("Moneda gastada")


moneda1= Dolar()
moneda2= Dolar()


moneda1.vueltas()
moneda1.vueltas()
moneda1.vueltas()
moneda1.vueltas()

del moneda1

print(moneda1)

del moneda2
print(moneda2)




