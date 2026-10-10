#*****************************************************************************
# Author:        Robyn Washburn
# Assignment:    Lab 3
# Date:          October 9, 2026
# Description:   This program calculates an unweighted grade point average
#                based on user input.
# Inputs:        str courseGrades, str letterGrade, float courseCredit
#                , int numCourses
# Outputs:       float resultGPA, float gradePoints, float creditHours
# Sources:       Chapter 3, assignment 3 specs, CIS 133Y Python Style Guide
# GitHub:        https://github.com/washburnr/Lab_3_GPA_Calculator_2026.git
#*****************************************************************************

def main():
    resultGPA = 0.0

    print("=============================================================")
    print("               WELCOME TO THE GPA CALCULATOR!                ")
    print("=============================================================")
    print(" Enter the letter grade and credit hour for each course      ")
    print(" you've completed, and an unweighted GPA will be calculated  ")
    print(" using the following grading table:                          \n")
    print(" A+ = 4.00    A  = 4.00    A- = 3.67   B+ = 3.33   B  = 3.00 ")
    print(" B- = 2.67    C+ = 2.33    C  = 2.00   C- = 1.67   D+ = 1.33 ")
    print(" D  = 1.00    D- = 0.67    F  = 0.00                         ")
    print("-------------------------------------------------------------\n")

    #gradePoints, creditHours = getGrades()
    #resultGPA = calcGPA(gradePoints, creditHours)
    #printResults(resultGPA)
    print("\nThank you!")

    #Collect grade and credit hours from user inputs
    def getGrades():
        numCourses = int(input("How many courses do you need to include "
                               "in the calculation? "))
        gradePoints = 0.0
        creditHours = 0.0

        for i in range(numCourses):
            letterGrade = input("Enter the letter grade "
                                "(A+ through F): ").upper()
            creditHours = float(input("Enter the credit "
                                      "hours for the course: "))
            creditHours += creditHours
            if letterGrade == "A+":
                gradePoints += 4.33
            elif letterGrade == "A":
                gradePoints += 4.00
            elif letterGrade == "A-":
                gradePoints += 3.67
            elif letterGrade == "B+":
                gradePoints += 3.33
            elif letterGrade == "B":
                gradePoints += 3.00
            elif letterGrade == "B-":
                gradePoints += 2.67
            elif letterGrade == "C+":
                gradePoints += 2.33
            elif letterGrade == "C":
                gradePoints += 2.00
            elif letterGrade == "C-":
                gradePoints += 1.67
            elif letterGrade == "D+":
                gradePoints += 1.33
            elif letterGrade == "D":
                gradePoints += 1.00
            elif letterGrade == "D-":
                gradePoints += 0.67
            elif letterGrade == "F":
                gradePoints += 0.00
            else:
                print("Please enter a valid letter grade")
                continue

        print(f"creditHours: {creditHours}")
        print(f"gradePoints: {gradePoints}")

    getGrades()





main()