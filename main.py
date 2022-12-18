import sqlite3
import tkinter
# By Team Blue

mainwindow = tkinter.Tk()
BottomFrame = tkinter.Frame(mainwindow, height=30, width=30)
TopFrame = tkinter.Frame(mainwindow, height=30, width=30)
conn = sqlite3.connect('StudentDatabase.db')
curs = conn.cursor()
info = tkinter.StringVar()
OutLabel = tkinter.Label(BottomFrame, textvariable=info)


def Database():
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
    curs.execute('''SELECT * From StudentDatabase''')
    Info = tkinter.Label(TopFrame, text="Student Database. Please select Input to input more data, \nor Read to read existing data")
    InputButton = tkinter.Button(TopFrame, text="Input", command=Insert)
    ReadButton = tkinter.Button(TopFrame, text="Read", command=Request)
    Info.pack()
    InputButton.pack()
    ReadButton.pack()
    TopFrame.pack()
    BottomFrame.pack()
    tkinter.mainloop()
    conn.commit()
    conn.close()

def Request():
    List = str(curs.fetchone())
    while List != "None":
        List += "\n"
        List += str(curs.fetchone())
    OutLabel.pack()
    info.set(List)


def Insert():
    info.set("Would you like to update existing data, delete an existing student, or create a new student?")
    OutLabel.pack()
    UpdateDataButton = tkinter.Button(BottomFrame, text="Update Data", command=UpdateData)
    NewStudentButton = tkinter.Button(BottomFrame, text="Create New Student", command=NewStudent)
    DeleteStudentButton = tkinter.Button(BottomFrame, text="Delete Student", command=DeleteStudent)
    UpdateDataButton.pack(side="right")
    DeleteStudentButton.pack(side="left")
    NewStudentButton.pack()


def UpdateData():
    pass

def NewStudent():
    pass


def DeleteStudent():
    pass

if __name__ == '__main__':
    Database()
