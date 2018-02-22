"""
    File:  quizGrader.py
    Author: Andrew Walker
    Description: Reads quizs from a directory and generates a file "gradeReport.txt".
                 This file lists the students names and their quiz percentages.

"""

from os.path import exists
import os

# global so functions can add to and reference quiz scores
STUDENTS_DICT = {
    "Doe, Jane" : 0,
    "Jones, Tom" : 0,
    "Kidd, Billy" : 0,
    "Smith, Sally" : 0,
    "Answers" : 0 # stores how many questions have been asked
}

def main():
    """ Runs all necessary functions and outputs student quiz scores. """
    directList = getQuizzes()
    studentDotTxtList = getStudentsDotText() # so we can cycle through the students .txt files in the quiz directories
    studentsFormatted = getStudentsFormatted() # so we can add quiz scores to STUDENTS_DICT
    for direct in directList:
        gradedQuiz = quizReader(direct, studentDotTxtList)
        STUDENTS_DICT["Answers"] += gradedQuiz.pop()
        for student in range(len(gradedQuiz)):
            STUDENTS_DICT[studentsFormatted[student]] += gradedQuiz[student][1]
    printResults()

def getStudentsDotText():
    """ Finds a file called 'students.txt' and creates a list of their names in .txt format. """
    if exists("students.txt"):
        studentList= []
        nameList = []
        file = open("students.txt", "r")
        for line in file:
            line = line.rstrip()
            nameList.append(line.split(",")) # adds the student names to be formatted
        for name in nameList:
            formattedName = str(name[0]).lower() + "_" + str(name[1].lower().lstrip() + ".txt") # formats the names into
            studentList.append(formattedName)                                                   # text file format
    return studentList

def getStudentsFormatted():
    """ Finds a file called 'students.txt' and creates a list of their names in Lastname, Firstname format """
    if exists("students.txt"):
        nameList = []
        file = open("students.txt", "r")
        for line in file:
            line = line.rstrip()
            nameList.append(line)
    return nameList

def getQuizzes():
    """ Creates list of quiz directories """
    directList = []
    tempDirectList = os.listdir('.') # creates list of directories in current directory to filter quizzes out of
    for item in tempDirectList:
        if item[:4] == "quiz": # selectively picks the directories that start with 'quiz'
            directList.append(item)
    return directList

def quizReader(directory, students):
    """ Goes over quiz directories and reads the student quizzes and compares them to the answer key. """

    os.chdir(directory)

    #creates an answer key list to compare student answers against
    answerKeyList = []
    answerKey = open("answers.txt", "r")
    for line in answerKey:
        line = line.rstrip()
        line = line.lower()
        answerKeyList.append(line)
    answerKey.close()

    resultsList = [] # will be list of lists with each sublist containing the students name and number correct
    studentNumber = 0
    for student in students:
        resultsList.append([student, 0]) # creates initial student sublist
        studentAnswersList = []
        # for each student, this will check each of their answers against the answer key, then increment their score
        # by one if they answered correctly
        if exists(student):
            file = open(student, "r")
            for line in file:
                line = line.rstrip()
                line = line.lower()
                studentAnswersList.append(line)
            for answer in range(0, len(studentAnswersList)):
                if studentAnswersList[answer] == answerKeyList[answer]:
                    resultsList[studentNumber][1] += 1 # use student number to change which students score we're updating
            studentNumber += 1
    resultsList.append(len(answerKeyList)) # so we know the highest possible score

    os.chdir("..") # gets us out of the quiz directory and back into the main directory
    return resultsList

def printResults():
    """ Prints a table that lists the students, their total points scored, and their overall percentage answered correct """
    gradeReport = open("gradeReport.txt", "w")

    # Header and labels for the name and scores
    gradeReport.write("Student Quiz Report".center(48) + "\n\n")
    gradeReport.write("%-15s %15s %28s\n" % ("Student", "Total Quiz Points", "Overall Quiz Percent"))
    gradeReport.write("-" * 63 + "\n")

    # prints name and their scores
    totalPossible = STUDENTS_DICT["Answers"]
    for key in STUDENTS_DICT:
        if key != "Answers":
            name = key
            totalQuizPoints = STUDENTS_DICT[key]
            overallQuizPercent = (totalQuizPoints / totalPossible) * 100
            gradeReport.write("%-15s %9d %28.2f\n" % (name, totalQuizPoints, overallQuizPercent))

    gradeReport.close()


main()