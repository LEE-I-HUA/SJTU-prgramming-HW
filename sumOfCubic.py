#get cubic number

def main():
    
    sumOfCubic = 0
    number = eval(input("Please enter a nuber"))
    number = number+1
    
    for i in range(1,number):
        cubicNumber = i**3
        sumOfCubic = sumOfCubic+cubicNumber

    print("the sum of cubic number is", sumOfCubic)
    
main()
input()
