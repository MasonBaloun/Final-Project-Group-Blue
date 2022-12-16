import sqlite3
# By Team Blue


def main():
# Create connection
    conn = sqlite3.connect('StudentDatabase.db')
# Setup Cursor
    curs = conn.cursor()
# Create a table within the database if it doesn't exist already
# Using a multiline string simplifies the execute command
    curs.execute('''CREATE TABLE IF NOT EXISTS Something (student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
# We need to import student data
    student_info = [(1, 'Oprah', 'Winfrey', 'Computer Science 101', 'Math 101', 'Painting', 'Drawing'),
    (2, 'Angelina', 'Jolie', 'Math 200', 'Arts 101', 'Driving', 'Skydiving'),
    (3, 'Dwayne', 'Johnson', 'Health 100', 'Physical Education 100', 'Acting', 'Eating'),
    (4, 'Chris', 'Prat', 'Theater 101', 'Gender Studies', 'Hiking', 'Swimming')]
# Add values into the database if they don't already exist
    curs.executemany('INSERT OR REPLACE INTO Something VALUES (?, ?, ?, ?, ?, ?, ?)', student_info)
    conn.commit()
    conn.close()