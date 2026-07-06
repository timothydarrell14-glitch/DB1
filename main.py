#-----------Importing sqlite and panda--------------#

import sqlite3
import pandas as pd

#-----------Linking py file with sqlite file--------------#

conn = sqlite3.connect("db.sqlite")

cur = conn.cursor()

cur.close()
conn.close()