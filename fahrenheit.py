# 第二章课后习题-编程练习第4题Modify the convert. py program (Section 2.2) with a loop so that it executes 5 times before quitting. 
# Each time through the loop, 
# the program should get another temperature from the user and print the converted value. 
def main():
    for i in range(5):
        celsius = eval(input("What is the Celsis temperature?"))
        fahrenheit = 9/5*celsius +32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
input()
