# ch06ex04.  Write definitions for the following two functions:  sumN (n) returns the sum of the first n natural numbers. 
# sumNCubes (n) returns the sum of the cubes of the first n natural numbers.  
# Then use these functions in a program that prompts a user for an n and prints out the sum of the first n natural numbers and the sum of the cubes of the first n natural numbers.


# LeeIHua
def sumN(n):
    sumN = 0
    for i in range (n+1):
        sumN = sumN +i
    return sumN    

def sumNCubes(n):
    sumNCubes = 0
    for i in range(1,n+1):
        cubicNumber = i**3
        sumNCubes = sumNCubes+cubicNumber
    return sumNCubes

def main():
    n = int(input("please enter the number:"))
    print("the sum of the first n natural numbers is"
          ,sumN(n))
    print("the sum of the cubes of the first n natural numbers is",sumNCubes(n))
main()
input()
