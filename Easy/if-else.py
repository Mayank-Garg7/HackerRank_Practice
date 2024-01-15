#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0 or (n>=6 and n<=20): 
#If n is even and in the inclusive range of 6 to 20, as well as If n is odd then print Weird  
    print("Weird")
else: 
#Else print not weird .
    print("Not Weird")