import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

even = (n % 2 )
if even != 0:
    print("Weird")
elif n in range(2, 6) and even == 0:
    print("Not Weird")
elif n in range(6, 21) and even == 0:
    print("Weird")
elif n > 20 and even == 0:
    print("Not Weird")