"""
Description: Script entry point

"""
import math

class Advent:
    def __init__(self, inputList):
        self.inputList = inputList 

    def start(self):
        #self.__runPartOne()
        self.__runPartTwo()

    def __runPartOne(self):
        calcFuelNeeded = lambda m : math.floor(m / 3) - 2
        sumFuelNeeded = 0

        for mass in self.inputList:
            fuel = calcFuelNeeded(mass)
            print("Mass {} needs fuel of {}".format(mass, fuel))
            sumFuelNeeded += fuel

        print("Sum of fuel needed is {}".format(sumFuelNeeded))

    def __runPartTwo(self):
        sumFuelNeeded = 0

        for mass in self.inputList:
            fuel = self.__recurseCalcFuelNeeded(mass)
            print("Mass {} needs fuel of {}".format(mass, fuel))
            sumFuelNeeded += fuel

        print("Sum of fuel needed is {}".format(sumFuelNeeded))

    def __recurseCalcFuelNeeded(self, mass):
        calcFuelNeeded = lambda m : math.floor(m / 3) - 2
        
        fuel = calcFuelNeeded(mass)

        if fuel <= 0:
            return 0

        fuel += self.__recurseCalcFuelNeeded(fuel)

        return fuel
