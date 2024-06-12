import random

class Moneda():

    def __init__(self,raro=False,limpio=True,caras=True):

        self.es_raro=raro
        self.es_limpio=limpio
        self.caras=caras

        if self.es_raro ==True:

            self.valor=self.valor_original * 1.25

        else:
            self.valor = self.valor_original

        if self.es_limpio==True:
            self.color = self.color_limpio

        else:
            self.color = self.color_oxidado


    def oxido(self):

        self.color= self.color_oxidado

    def limpiar(self):
        print("Se limpio la moneda")
        self.color=self.color_limpio

    def vueltas(self):

        caras_opciones = [True,False]
        eleccion= random.choice(caras_opciones)
        self.caras= eleccion
        print(self.caras)

    def __del__(self):

        print("Moneda gastada")



class Dolar(Moneda):


    def __init__


    