
class Dog():
    """A class to represent a general dog"""


    def __init__(self,my_name,my_age,my_gender,my_vida):


        self.name= my_name
        self.age= my_age
        self.gender= my_gender
        self.vida=my_vida
        self.power=40

    def barking(self):
        
        if self.gender == "Male":

            print(f"Soy macho y me llamo {self.name}, WOOF WOOF WOOF")

        elif self.gender == "Hembra":

            print(f"Soy hembra y mi me llamo {self.name}, WOOF WOOF WOOF")

        else:
            print("Compadre se equivoco escribiendo")


    def eat(self):
        print(f"My life is {self.vida} ")
        self.vida+=100
        print(f"Thank you my life now is {self.vida}")


    def train(self, is_weekend,aumento):

        if is_weekend == False:

            print(self.power)
            print(f"Lets go {self.name} vamos a entrenar")
            self.power+= aumento
            print(f"Now my power is {self.power}")

        else:
            print("ES hora de la fiesta, baile improvisado")

    def compute_age(self):

        dog_years= self.age* 7
        print(f"{self.name} age is {dog_years}")



perro1=Dog("carlos",9,"Male",80)

perro1.compute_age()