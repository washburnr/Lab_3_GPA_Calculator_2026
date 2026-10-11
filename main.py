#*****************************************************************************
# Author:        Robyn Washburn
# Assignment:    Lab 3
# Date:          October 9, 2026
# Description:   This program calculates an unweighted grade point average
#                based on user input.
# Inputs:        str courseGrades, str letterGrade, float courseCredit,
#                int numCourses, float creditHours
# Outputs:       float resultGPA, float gradePoints, float sumHours
# Sources:       Chapter 3, assignment 3 specs, CIS 133Y Python Style Guide
# GitHub:        https://github.com/washburnr/Lab_3_GPA_Calculator_2026.git
#*****************************************************************************

def main():

    print("=============================================================")
    print("               WELCOME TO THE GPA CALCULATOR!                ")
    print("=============================================================")
    print(" Enter the letter grade and credit hours for each course      ")
    print(" you've completed, and an unweighted GPA will be calculated  ")
    print(" using the following grading table:                          \n")
    print(" A+ = 4.00    A  = 4.00    A- = 3.67   B+ = 3.33   B  = 3.00 ")
    print(" B- = 2.67    C+ = 2.33    C  = 2.00   C- = 1.67   D+ = 1.33 ")
    print(" D  = 1.00    D- = 0.67    F  = 0.00                         \n")
    print(" Please note: Letter grades and credit hours must be entered \n")
    print(" correctly in order for the calculation to run.                ")
    print("-------------------------------------------------------------\n")

    qualityPoints, sumHours = getGrades()
    resultsGPA = calcGPA(qualityPoints, sumHours)
    printResults(resultsGPA)
    print("\nThank you!")

#Collect grade and credit hours from user inputs
def getGrades():
    numCourses = int(input("How many courses do you need to include "
                            "in the calculation? "))
    qualityPoints = 0.0
    sumHours = 0.0

    for i in range(numCourses):
        letterGrade = input("Enter the letter grade "
                            "(A+ through F): ").upper()
        creditHour = float(input("Enter the credit "
                                  "hours for the course: "))
        if letterGrade == "A+" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 4.33 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "A" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 4.00 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "A-" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 3.67 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "B+" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 3.33 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "B" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 3.00 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "B-" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 2.67 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "C+" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 2.33 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "C" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 2.00 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "C-" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 1.67 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "D+" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 1.33 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "D" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 1.00 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "D-" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 0.67 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        elif letterGrade == "F" and creditHour > 0.0 and creditHour <= 5.0:
            gradePoints = 0.00 * creditHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += creditHour
        else:
            print("Invalid valid letter grade or credit hours.")
            continue
    return qualityPoints, sumHours

def calcGPA(qualityPoints, sumHours):
    resultsGPA = round(qualityPoints / sumHours, 2)
    return resultsGPA

def printResults(resultsGPA):
    print(f"Unweighted GPA: {resultsGPA}")
    if resultsGPA >= 3.75:
        print("Congratulations! You've achieved High Honors!")
    elif resultsGPA < 3.75 and resultsGPA >= 3.00:
        print("Congratulations! You are on the Honor Roll!")
    elif resultsGPA < 3.00 and resultsGPA >= 2.00:
        print("You are in Good Academic Standing.")
    else:
        print("A GPA under 2.00 falls under Good Academic Standing.\n"
              "Please reach out to your advisor to access\n"
              "additional academic support for next term.")

main()
