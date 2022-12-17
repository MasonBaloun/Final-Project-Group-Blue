import sqlite3
import tkinter
# By Team Blue


def main():
    print("test")
    Done = False
    Input = False
    Read = True
    student_info = []
    mainwindow=tkinter.Tk()
    MainFrame=tkinter.Frame(mainwindow)
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
    List = curs.fetchone()
    while Done == False:
        if Input == True:
            Input = False
            conn.commit()
        if Read == True:
            label = tkinter.Label(MainFrame, textvariable=info)
            while List != "None":
                List += curs.fetchone()
            label.pack()
            MainFrame.pack()
            info = List
            Read = False
    curs.executemany('INSERT OR REPLACE INTO Something VALUES (?, ?, ?, ?, ?, ?, ?)', student_info)
    tkinter.mainloop()
    conn.commit()
    conn.close()