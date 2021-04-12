#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    studentNumber = ""
    grade = int("")
    getCourses = list("")
    getGrades = list("")

    # properties should be listed first

    def __init__(self, name, id, level, subjects, points): # You will need to create your own input parameters for all methods
        self.name = name 
        self.id = studentNumber
        self.level = grade
        self.subjects = getCourses
        self.points = getGrades
        print("Student name: " + self.name)

    def __del__(self):
        print("Identification ended.")

    def command(self):
        print("Please enter he number to show the desired information.")
        print("1. Average grade of all courses.")
        print("2. Honor roll.")
        print("3. List of courses.")
        print("4. Course's name and grade.")
        print("5. ")
    def average(self):
        print("")
    
    def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()