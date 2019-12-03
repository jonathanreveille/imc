#! /usr/bin/env python3
# coding : utf-8

""" Module qui nous permet de calculer son IMC """

class BMI:
    """Class that gives the imc of a person"""

    def __init__(self):#Initialize class

        self.name = str()
        self.weight = None
        self.height= None
        self.bmi = None


    def __repr__(self):
        """ method that returns a string of the object"""
        return f"{self.name},ton IMC est de{self.bmi},tu mesures {self.height} et ton poids est de {self.weight}"


    def calculate_bmi(self):
        """this method to calculate imc of the person"""

        bmi =  float(self.weight) / (float(self.height) **2)
        self.bmi = float(bmi)


    def show_info_about_bmi(self):
        """ this method returns the state of the person 
        according the his/her BMI """

        while self.bmi != 0:

            if self.bmi < 16.5:
                print(f"You don't eat enough, it's time to order a pizza, btw, your BMI is {self.bmi} your BMI should be between 18.5 and 25")

            elif 16.5 < self.bmi < 18.5:
                print(f"you are very thin, it's time to eat a little more once again, let's order in ! your BMI is {self.bmi} your BMI should be between 18.5 and 25")

            elif 18.5 < self.bmi <= 25:
                print(f"you are in good shape, don't change, your BMI is {self.bmi}")

            elif 25 < self.bmi < 30:
                print(f"you are a little bit overweight according to BMI, your BMI is {self.bmi} your BMI should be between 18.5 and 25")

            elif self.bmi >30:
                print(f"you are definitely overweight, your BMI is {self.bmi} your BMI should be between 18.5 and 25")

            break


def main():
    person = BMI()
    person.name =  input("Please give me your name   ")
    person.weight = input("Please give me your weight, round number   ")
    person.height = input("Last one, give me your height please in meters, example (155cm =1.55m)  ")
    person.calculate_bmi()
    person.show_info_about_bmi()


if __name__ == "__main__":
    main()