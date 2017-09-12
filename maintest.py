# -*- coding: utf-8 -*-

import time
from sys import stdin
from labb6 import *

inrad = stdin.readline()

while inrad:
  if "#" in inrad:
    break
  try:
    readFormel(inrad)
    print("Formeln ar syntaktiskt korrekt")
  except SyntaxError as felet:
    print(felet)
  inrad = stdin.readline()
