import sqlite3
import tkinter
# By Team Blue

mainwindow = tkinter.Tk()
BotomFrame = tkinter.Frame(mainwindow, height=30, width=30)
TopFrame = tkinter.Frame(mainwindow, height=30, width=30)
conn = sqlite3.connect('StudentDatabase.db')
curs = conn.cursor()

def Database():
    Done = False
    Input = False
    Read = False
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
    curs.execute('''SELECT * From StudentDatabase''')
    Info = tkinter.Label(TopFrame, text="Student Database. Please select Input to input more data, \nor Read to read existing data")
    InputButton = tkinter.Button(TopFrame, text="Input")
    ReadButton = tkinter.Button(TopFrame, text="Read", command=Request)
    while not Done:
        print("test")
        if Input == True:
            print("test")
            Input = False
            conn.commit()
        Done=True

    Info.pack()
    InputButton.pack()
    ReadButton.pack()
    TopFrame.pack()
    BotomFrame.pack()
    tkinter.mainloop()
    conn.commit()
    conn.close()

def Request():
    info = tkinter.StringVar()
    List = str(curs.fetchone())
    OutLabel = tkinter.Label(BotomFrame, textvariable=info)
    while List != "None":
        List += "\n"
        List += str(curs.fetchone())
    OutLabel.pack()
    info.set(List)

if __name__ == '__main__':
    Database()
