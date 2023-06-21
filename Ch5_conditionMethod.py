# Python程序設計第五章編成練習三：
# A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 
# 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts an exam score as input and 
# prints out the corresponding grade.

def main():
    print("change the student's grade to score")
    score = eval (input("student's score:"))

    if (score <= 100 and score >= 90):
        grade = "A"
    elif(score < 90  and score >= 80):
        grade = "B"
    elif(score < 80  and score >= 70):
        grade = "C"
    elif(score < 70  and score >= 60):
        grade = "D"
    else:
        grade = "F"
    print("the student's grade is", grade)
main()
input()
