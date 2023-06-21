# Monte Carlo techniques can be used to estimate the value of pi. Suppose you have a round dartboard that just fits inside of a square cabinet. 
# If you throw darts randomly, the proportion that hit the dartboard vs. 
# those that hit the cabinet (in the corners not covered by the board) will be determined by the relative area of the dartboard and the cabinet. 
# If n is the total number of darts randomly thrown (that land within the confines of the cabinet), and h is the number that hit the board, it is easy to show that    
# pi ≈ 4（h/n)  Write a program that accepts the "number of darts" as an input and then performs a simulation to estimate pi.  
# Hint: You can use 2*random ()- 1 to generate the x and y coordinates of a random point inside a 2x2 square centered at (0, 0). 
# The point lies inside the inscribed circle if x2 +y2 < =1.

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
