import sqlite3
import os.path

DB_NAME = "main_db.sqlite3"


def connect_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, DB_NAME)
    return sqlite3.connect(db_path)


def set_session(timestamp):
    db = connect_db()
    db.execute("INSERT INTO main_survey_logtable (session) VALUES (?)",(str(timestamp),));
    db.commit()
    db.close()
    return str(timestamp)

def store_in_db(what, where_):
    db = connect_db()
    db.execute("INSERT INTO main_survey_logtable ("+where_+") VALUES (?)",(str(what),));
    db.commit()
    db.close()



def decode_where_syntax(page_id):
    if page_id==None or page_id==0:
        return 'lang'
    elif page_id==28 or page_id==29:
        return 'valid'
    else:
        return str('l'+str(page_id))


def page_selector(page_id, request):
    if (page_id in [1,2,10,16]):
        return page_id+1
    elif page_id==3:
        return 4
