# -*- coding: utf-8 -*-

import time
from sys import stdin
from labb6 import *

# sets indata to input from user
indata = stdin.readline()

# while there is indata
while indata:
  # break if input is #
  if "#" in indata:
    break
  # while input is not #, continue
  try:
    # try to read the indata as a formula and if correct print message
    readFormel(indata)
    print("Formeln ar syntaktiskt korrekt")
  except SyntaxError as felet:
    # if it fails then return correct error message
    print(felet)
  indata = stdin.readline()
