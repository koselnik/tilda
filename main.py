# -*- coding: utf-8 -*-

import time
from labb6 import *
t = time.time()

with open('incorrect_sample.in') as text:
  for line in text:
    try:
      readFormel(line)
      print("Formeln ar syntaktiskt korrekt")
    except SyntaxError as felet:
      print(felet)

print(time.time() - t)
