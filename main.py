#-----------Importing sqlite--------------#

import sqlite3
# import pandas as pd

#-----------Linking py file with sqlite file--------------#

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

# cur.execute("""
# CREATE TABLE tasks (
#         id INTEGER PRIMARY KEY,
#         title TEXT NOT NULL,
#         description TEXT,
#         completed BOOLEAN DEFAULT 0,
#         created_at TIMESTAMP DEFAULT NOW);
# """)

cur.execute("""
    INSERT INTO tasks (title, completed)
            VALUES
            ('Fix login bug', 0),
            ('Write unit tests', 0),
            ('Deploy to staging', 1),
            ('Update README', 0),
            ('Code review PR #42', 1);
         """)
conn.commit()

def get_all_tasks():
    cur.execute('SELECT * FROM tasks')
    return cur.fetchall()

def get_task(task_id):
    cur.execute('SELECT * FROM tasks WHERE id=?',
               (task_id,))
    return cur.fetchone()

def get_incomplete_tasks():
    cur.execute('SELECT * FROM tasks WHERE completed=0 '
                'ORDER BY created_at DESC')
    return cur.fetchall()

# print(get_all_tasks())
# print(get_task(2))
# print(get_incomplete_tasks())

cur.close()
conn.close()