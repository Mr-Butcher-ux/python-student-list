#This program tries to simulate a student database.
#The basic functions of this program are: Show all records, geat a specific student record,
#Add a new record to the database and exit the database (without saving changes).
import csv

#This is the defuction included in the homework for read the file
def read_file(record_file):
    dblist = []
    with open(record_file, 'r') as stu_file:
        records = csv.reader(stu_file)
        for row in records:
            dblist.append([int(row[0]), row[1], row[2], row[3], float(row[4])])

    return dblist


student_db = read_file('student_records')

#This is the defuction for show the file in order as the example in the homework.
def show_records():
    print('\n Stu Id\t\t\t    Name\t\t\t   Major\t\t\t  Entry\t\t\t     GPA')
    #Sets the rows and the columns from the file
    for row in student_db:
        for column in range(len(row)):
            print('', f'{row[column]:<18}', end='')

        print()

#This is the defuction to find an specific student in the file.
def show_student():
    id = int(input('Enter the student id: '))
    for row in range(len(student_db)):
        for column in range(len([row])):
            #If the student id is in the file
            if id == student_db[row][0]:
                # print the index of the specific student
                print('Record found with index ', student_db.index(student_db[row]))
                print('\nStu Id Name\t    Major Entry GPA')
                # prints the row of the specific student
                print(*student_db[row][0:5], end='        ' + '\n')
                return

    # If the id is not in the student file will display a message
    if id not in student_db:
        print('\nRecord not found in the database.')


print()

#This is the defuction for add the new student
def add_student():
#This is a list to add the new student information
    new_student = []
    #Ask user input
    id = int(input('Enter the student id (5 digits): '))
    #If the user input is in the file this will print a message and return to the menu
    for row in range(len(student_db)):
        for column in range(len([row])):
            if id == student_db[row][0]:
                print('Student ID', id, 'is in the list. ')
                return

    #If the id is not in the file the program will ask the new student information and then add it to the list new_student.
    if id not in student_db:
        new_student.append(int(id))
        print('Student ID', id, 'not in the list. ')
        name = (str(input('Enter student name:')))
        new_student.append(str(name))
        major = (str(input('Enter student major (4 letters):')))
        new_student.append(str(major))
        semester = (str(input('Enter student semester of entry (5 digits): ')))
        new_student.append(str(semester))
        gpa = (float(input('Enter student GPA (0.00 to 4.00): ')))
        new_student.append(float(gpa))
        print('\nRecord added.')

        #The new student list with the new student information will be add it to the student file.
        student_db.append(new_student)

print()


#This is the defuction for the menu, if the user enters an invalid option the program will ask again, this program ends when
#the user enters 0
def main():
    option = 1
    while option >= 1:
        print('\nWelcome to the student data management system\n\nStudent Record Menu System:\n'
              '(1) display all records\n(2) Get a student record\n(3) Add new student record\n(0) Exit')
        option = int(input('Enter option code: '))
        if option == 1:
            print(show_records())
        elif option == 2:
            print(show_student())
        elif option == 3:
            print(add_student())
        elif option == 0:
            print('\nExiting the database.')
        else:
            print("Invalid option, try again\n")


main()
