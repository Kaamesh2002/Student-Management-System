
import sys
studentname = []
studentrollno = []
studentadd= []
studentgmail = []
studentage= []
studentmobileno = []
studentclass = []


class Management:
    @staticmethod
    def add_student_info():
        print("ADDING STUDENT INFORMATION : \n")
        print("ENTER STUDENT NAME :", end=" ")
        name = input().upper()
        studentname.append(name)

        print("ENTER STUDENT ROLL NUMBER :", end=" ")
        rollno = int(input())
        studentrollno.append(rollno)

        print("ENTER STUDENT AGE :", end=" ")
        age = int(input())
        studentage.append(age)

        print("ENTER STUDENT CLASS :", end=" ")
        stdclass = input()
        studentclass.append(stdclass)

        print("ENTER STUDENT E-MAIL ID :", end=" ")
        gmail = input().upper()
        studentgmail.append(gmail)

        print("ENTER STUDENT ADDRESS :", end=" ")
        address = input().upper()
        studentadd.append(address)

        print("ENTER STUDENT MOBILE NUMBER :", end=" ")
        mobileno = input()
        mobileno_len = len(mobileno)

        if mobileno_len < 10:
            print("\t PLEASE ENTER VALID TEN DIGIT MOBILE NUMBER.")
        else:
            studentmobileno.append(mobileno)
            print("\n")
            print("\t STUDENT INFORMATION ADDED SUCCESSFULLY.")
            print("\n")
    @staticmethod
    def delete_info():
        print("DELETING STUDENT INFORMATION : \n")

        if len(studentname) == 0 and len(studentrollno) == 0 and len(studentage) == 0 and len(studentclass) == 0 and len(studentmobileno) == 0 and len(studentadd) == 0 and len(studentgmail) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("ENTER STUDENT'S ROLL NUMBER :", end=" ")
            roll = int(input())
            a = studentrollno.index(a)

            studentrollno.remove(studentrollno[a])
            studentname.remove(studentname[a])
            studentmobileno.remove(studentmobileno[a])
            studentage.remove(studentage[a])
            studentadd.remove(studentadd[a])
            studentgmail.remove(studentgmail[a])
            studentclass.remove(studentclass[a])

            print("\n")
            print("\t\t STUDENT INFORMATION DELETED SUCCESSFULLY.")
            print("\n")
    @staticmethod
    def update_info():
        print("UPDATE STUDENT INFORMATION : \n")

        if len(studentname) == 0 and len(studentrollno) == 0 and len(studentage) == 0 and len(studentclass) == 0 and len(studentmobileno) == 0 and len(studentadd) == 0 and len(studentgmail) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("ENTER STUDENT ATTRIBUTE YOU WANT TO DELETE :", end="\n")
            print("LIKE 'NAME, ROLL NUMBER, AGE, MOBILE NUMBER, ADDRESS, EMAIL, CLASS.")
            print("ENTER HERE :", end=" ")
            update = input()

            if update == 'name':
                print("ENTER 'OLD NAME' :", end=" ")
                oldname = input()
                b = studentname.index(oldname)

                print("ENTER 'NEW NAME' :", end=" ")
                newname = input()
                newname[b] = newname
                print("\t 'NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'roll number':
                print("ENTER 'OLD ROLL NUMBER' :", end=" ")
                oldrollno = int(input())
                c = studentrollno.index(oldrollno)

                print("ENTER 'NEW ROLL NUMBER' :", end=" ")
                newroll = int(input())
                studentrollno[c] = newroll
                print("\t 'ROLL NUMBER UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'age':
                print("ENTER 'OLD AGE' :", end=" ")
                oldage = int(input())
                d = studentage.index(oldage)

                print("ENTER 'NEW AGE' :", end=" ")
                newage = int(input())
                studentage[d] = newage
                print("\t 'AGE UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'address':
                print("ENTER 'OLD ADDRESS' :", end=" ")
                oldadd = input()
                e = studentadd.index(oldadd)

                print("ENTER 'NEW ADDRESS' :", end=" ")
                newadd = input()
                studentadd[e] = newadd
                print("\t 'ADDRESS UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'gmail':
                print("ENTER 'OLD EMAIL' :", end=" ")
                oldgmail = input()
                f = studentgmail.index(oldgamil)

                print("ENTER 'NEW EMAIL' :", end=" ")
                newgmail = input()
                studentgmail[f] = newgmail
                print("\t 'EMAIL - ID UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'class':
                print("ENTER 'OLD CLASS' :", end=" ")
                oldclass = input()
                g = STUDENT_CLASS.index(oldclass)

                print("ENTER 'NEW CLASS' :", end=" ")
                newclass = input()
                studentclass[g] = newclass
                print("\t 'CLASS UPDATED SUCCESSFULLY.")
                print("\n")

            elif update == 'MOBILE NUMBER':
                print("ENTER 'OLD MOBILE NUMBER' :", end=" ")
                oldmoblieno = input()

                print("ENTER 'NEW MOBILE NUMBER' :", end=" ")
                newmobileno = input()
                mobileno_len = len(oldmobileno)
                newmobile_len = len(newlobileno)

                if mobileno_len < 10:
                    print(end="\n")
                    print("PLEASE ENTER TEN DIGIT MOBILE NUMBER.")
                    print("SYSTEM HAS STOP, PLEASE TRY AGAIN.")
                    sys.exit()
                elif newmobile_len < 10:
                    print(end="\n")
                    print("\t PLEASE ENTER VALID TEN DIGIT MOBILE NUMBER.")
                    print("\t SYSTEM WORKING HAS STOP PLEASE TRY AGAIN.")
                    sys.exit()
                else:
                    h = studentmobileno.index(oldmoblieno)
                    studentmobileno[h] = newmobileno
                    print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.")
                    print("\n")
    @staticmethod
    def display_info():
        print("DISPLAYING STUDENTS INFORMATION : \n")

        if len(studentname) == 0 and len(studentrollno) == 0 and len(studentage) == 0 and len(studentclass) == 0 and len(studentmobileno) == 0 and len(studentadd) == 0 and len(studentgmail) == 0:
            print("\n")
            print("\t\t\t 'OOPS ! NOTHING TO DISPLAY, BECAUSE NO DATA IS THERE.")
            print("\n")
        else:
            print("STUDENT'S NAME : ", end="\t")

            for x in studentname:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S ROLL NUMBER :", end="\n")

            for y in studentrollno:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S AGE :", end="\n")

            for z in studentage:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S MOBILE NUMBER :", end="\n")

            for x in studentmobileno:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S EMAIL :", end="\n")

            for y in studentgmail:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S CLASS :", end="\n")

            for z in studentclass:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S ADDRESS :", end="\n")

            for x in studentadd:
                print(x)
            print()

            print(end="\n")


m = Management()

if __name__ == '__main__':
    print("\n")

    print("' WELCOME TO STUDENT MANAGEMENT SYSTEM \n")
    run = True

    while run:
        print("PRESS FROM THE FOLLOWING OPTION : \n")

        print("PRESS 1 : TO ADD STUDENT INFORMATION.")
        print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
        print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")
        print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")
        print("PRESS 5 : TO EXIT SYSTEM.")

        choose = int(input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")

        if choose == 1:
            m.add_student_info()
        elif choose == 2:
            m.delete_info()
        elif choose == 3:
            m.update_info()
        elif choose == 4:
            m.display_info()
        elif choose == 5:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
        else:
            print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
            print("\n")
