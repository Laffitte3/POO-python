class Dolar():

    valor= 1.0
    color= "dorado"
    num_bordes= 22.5
    grosor= 3.15
    caras = True #Si es True es cara y si es False cruz



moneda1= Dolar()

print(type(moneda1))
print(moneda1.color)
print(moneda1.grosor)

moneda1.color= "verde"
print(moneda1.color)

moneda2= Dolar()

print(moneda2.color)