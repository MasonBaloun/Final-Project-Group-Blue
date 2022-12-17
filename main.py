import sqlite3
import tkinter
# By Team Blue


class Database:
    Done=False
    Input=False
    Read=False
    student_info = []
    mainwindow=tkinter.Tk()
    info = tkinter.StringVar()
    x=1
# Create connection
    conn = sqlite3.connect('StudentDatabase.db')
# Setup Cursor
    curs = conn.cursor()
# Create a table within the database if it doesn't exist already
# Using a multiline string simplifies the execute command
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase (student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
    while Done == False:
        if Input == True:
            Input = False
        if Read == True:
            curs.execute('''SELECT * From StudentDatabase''')
            DatabaseList=curs.fetchall()
            info.set(DatabaseList[0])
            tkinter.Label(mainwindow, textvariable=info)
            while info != "None":
                info.set(DatabaseList[x])
                tkinter.Label(mainwindow, textvariable=info)
                x+=1
            Read = False
# Add values into the database if they don't already exist
    curs.executemany('INSERT OR REPLACE INTO Something VALUES (?, ?, ?, ?, ?, ?, ?)', student_info)
    conn.commit()
    conn.close()