import sqlite3
import os 
dir_proj='./'
path_db = os.path.join(dir_proj,'proj.db')
if os.path.exists (path_db):
   os.remove(path_db)
cx = sqlite3.connect(path_db)

