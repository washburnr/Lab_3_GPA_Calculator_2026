#*****************************************************************************
# Author:        Robyn Washburn
# Assignment:    Lab 3
# Date:          October 9, 2026
# Description:   This program calculates an unweighted grade point average
#                based on user input.
# Inputs:        str courseGrades, str letterGrade, float courseCredit,
#                int numCourses, float creditHours
# Outputs:       float resultGPA, float gradePoints, float sumHours
# Sources:       Chapter 3, assignment 3 specs, CIS 133Y Python Style Guide,
#                https://docs.python.org/3/tutorial/errors.html,
#                I also Googled how to validate a list of choices from a
#                string input.
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
    print("-------------------------------------------------------------\n")
    # Uses an outer loop to rerun the program.
    choice = "y"
    while choice.lower() == "y":
        qualityPoints, sumHours = getGrades()
        resultsGPA = calcGPA(qualityPoints, sumHours)
        printResults(resultsGPA)
        choice = input("Would you like to calculate another GPA? (y/n) ")
    print("\nThank you!")

#Collect grade and credit hours from user inputs
def getGrades():
    qualityPoints = 0.0
    sumHours = 0.0

    while True:
        try:
            numCourses = int(input("How many courses do you need to include "
                                   "in the calculation? "))
            break
        except ValueError:
            print("Valid number required. Try again...")
    #  Uses a loop to prompt for input until the user is done.
    for i in range(numCourses):
        validGrade = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-"
            , "D+", "D", "D-" "F"]
        # Accepts a numeric and a string value.
        letterGrade = input("Enter the letter grade for the course: ").upper()
        while letterGrade not in validGrade:
            print("Invalid letter grade. Try again...")
            letterGrade = input("Enter the letter grade for the course: ").upper()

        while True:
            try:
                credHour = float(input("Enter the credit "
                                        "hours for the course: "))
                break
            except ValueError:
                print("Valid number required. Try again...")

        if letterGrade == "A+" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 4.33 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "A" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 4.00 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "A-" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 3.67 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "B+" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 3.33 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "B" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 3.00 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "B-" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 2.67 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "C+" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 2.33 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "C" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 2.00 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "C-" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 1.67 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "D+" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 1.33 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "D" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 1.00 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "D-" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 0.67 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        elif letterGrade == "F" and credHour > 0.0 and credHour <= 5.0:
            gradePoints = 0.00 * credHour
            qualityPoints = qualityPoints + gradePoints
            sumHours += credHour
        else:
            pass
    return qualityPoints, sumHours

# Performs calculations when input is done.
def calcGPA(qualityPoints, sumHours):
    if sumHours > 0:
        resultsGPA = round(qualityPoints / sumHours, 2)
    else:
        resultsGPA = 0
    return resultsGPA

def printResults(resultsGPA):
    print(f"Unweighted GPA: {resultsGPA}")
    if resultsGPA >= 3.75:
        print("A GPA of 3.75 or better is High Honors!")
    elif resultsGPA < 3.75 and resultsGPA >= 3.00:
        print("A GPA above 3.00 is Honors status!")
    elif resultsGPA < 3.00 and resultsGPA >= 2.00:
        print("A GPA of 2.00 or better is in Good Academic Standing.")
    else:
        print("A GPA under 2.00 falls under Good Academic Standing.")

main()
