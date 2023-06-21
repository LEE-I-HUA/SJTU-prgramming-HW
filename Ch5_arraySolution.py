# Python程序設計第五章編成練習三：
# A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 
# 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts an exam score as input and 
# prints out the corresponding grade.

def main():
    grade =["F", "D", "C", "B", "A"]
    score = eval(input ("please enter the student's CS score:"))
    # 取分數商數
    transformS = (score//10)-5
    if transformS > 4:
        transformS = 4
    elif transformS < 0:
        transformS = 0
    print(grade[transformS])
main()
input()
