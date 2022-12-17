import sqlite3
import tkinter
# By Team Blue


def Database():
    Done = False
    Input = False
    Read = True
    student_info = []
    mainwindow=tkinter.Tk()
    MainFrame=tkinter.Frame(mainwindow, height=30, width=30)
    info = tkinter.StringVar()
    x = 1
# Create connection
    conn = sqlite3.connect('StudentDatabase.db')
# Setup Cursor
    curs = conn.cursor()
# Create a table within the database if it doesn't exist already
# Using a multiline string simplifies the execute command
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase (student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
    curs.execute('''SELECT * From StudentDatabase''')
    List = str(curs.fetchone())
    while Done == False:
        if Input == True:
            Input = False
            conn.commit()
        if Read == True:
            label = tkinter.Label(MainFrame, textvariable=info)
            while List != "None":
                List += str(curs.fetchone())
            label.pack()
            info.set(List)
            Read = False
        Done=True
    MainFrame.pack()
    print("test")
    tkinter.mainloop()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    Database()