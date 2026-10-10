#*****************************************************************************
# Author:        Robyn Washburn
# Assignment:    Lab 3
# Date:          October 9, 2026
# Description:   This program calculates an unweighted grade point average
#                based on user input.
# Inputs:        str courseGrade, str enterDetail, float courseCredit
# Outputs:       float resultGPA
# Sources:       Chapter 3, assignment 3 specs, CIS 133Y Python Style Guide
# GitHub:        https://github.com/washburnr/Lab_3_GPA_Calculator_2026.git
#*****************************************************************************

def main():
    enterDetail = 'Y'
    courseCredit = 0.0
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

main()