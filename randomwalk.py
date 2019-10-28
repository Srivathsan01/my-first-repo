import random
import matplotlib.pyplot as plt

s = 1000
n = 10000
for i in range(s):
    x = 0
    for j in range(n):
        p = random.random()
        if(p > 0.5):
            x = x + 1
        else:
            x = x - 1
