import sqlite3

class CourseNotAllowedException(Exception):
    pass

def get_db_connection():
    return sqlite3.connect('enrollment.db')
