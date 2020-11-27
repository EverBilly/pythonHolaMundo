print('----------------------------------------------------------------------')
import math
import os
import random
import re
import sys
#odd = impar
#even = par
def hr(nn):
    if nn % 2 == 0 and(nn in range(2,6) or nn > 20):
        print('Not Weird')
    else: 
        print('Weird')

hr(52)
hr(53)