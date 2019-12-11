#!/usr/bin/env python3

from advent import Advent
#from advent.inputhandlers import LoadMockInput
from advent.inputhandlers import LoadInputFromFile

FILE = "./input.txt"

#advent = Advent(LoadMockInput())
advent = Advent(LoadInputFromFile(FILE))

advent.start()
