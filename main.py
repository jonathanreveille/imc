#! /usr/bin/env python3
# coding : utf-8

from demo import *


def main():
    person = BMI()
    person.name =  input("Please give me your name   ")
    person.weight = input("Please give me your weight, round number   ")
    person.height = input("Last one, give me your height please in meters, example (155cm =1.55m)  ")
    person.calculate_bmi()
    person.show_info_about_bmi()


if __name__ == "__main__":
    main()