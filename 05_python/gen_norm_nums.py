from random import gauss
import sys
from math import *
from statistics import *

if __name__ == "__main__":
    argues = []
    for a in sys.argv:
        argues.append(a)
    if len(argues) != 5:
        print("Wrong count of values, try again!")
    fileName = argues[1]
    size = int(argues[2])
    mu = float(argues[3])
    sd = float(argues[4])
    if size <= 0:
        print(f"The size of numbers must be larger than 0")
    vs = [gauss(mu = mu, sigma = sd) for i in range(size)]
    content = []
    content.append(f"Size:   {size}")
    content.append(f"Mean:   requested={round(mu, 1)}, generated={mean(vs)}")
    content.append(f"Stddev: requested={round(sd, 1)}, generated={stdev(vs)}")
    
    with open(file=fileName, mode="w") as f:
        for l in content:
            f.write( l )                   
            f.write( "\n" )