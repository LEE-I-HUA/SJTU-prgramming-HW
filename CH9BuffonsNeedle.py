# LEE I HUA
# 正方形邊長=2;center(0.0); h = 投針正中圓範圍內的數目 ; n = 投擲針數 ; pi = 4*h/n
from math import sqrt
import random
def count_pi(n):
    h = 0
    for i in range (n):
        # -1 <= x <= 1 ; -1 <= y <= 1
        x,y = random.uniform(-1, 1), random.uniform(-1, 1)
        if sqrt(x**2 + y**2) <= 1:
            h+= 1
        else :
            h = h
    pi = 4*h/n
    return pi

def main():
    n = int(input("darts number:"))
    print ("pi is around", count_pi(n),"in this test.")
main()
input()
