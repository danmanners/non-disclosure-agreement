import sqlite3, secrets, json
from datetime import datetime

from functions.main import dict_factory

# Create DB file
def check_table_exists(dbName, db_file_name):
    db = sqlite3.connect(db_file_name)
    c = db.cursor()

    # Check if shit exists
    c.execute("SELECT count(name) FROM {database} WHERE type='table' AND name=\'{dbName}\'".format(
        database='sqlite_master',
        dbName=dbName)
    )
    # Check the response
    if c.fetchone()[0]!=1:
        c.close()
        return False
    else:
        c.close()
        return True

def create_table(database, db_file_name):
    db = sqlite3.connect(db_file_name)
    c = db.cursor()

    c.execute("CREATE TABLE {}(date text, HostIP text, hash text, url text)".format(database))

    c.close()
    db.commit()
    db.close()

def add_item(database, db_file_name, request_ip, url):
    j = json.loads(url)['data']
    hashcode = secrets.token_hex(32)
    db = sqlite3.connect(db_file_name)
    db.row_factory = dict_factory
    c = db.cursor()
    now = datetime.now().isoformat(timespec='minutes')
    c.execute("INSERT INTO {}(date,HostIP,hash,url) VALUES(\'{}\',\'{}\',\'{}\',\'{}\')".format(
        database, now, request_ip, hashcode, j
    ))
    c.close()
    db.commit()
    db.close()
    return hashcode

def get_code(database, db_file_name, hashcode):
    db = sqlite3.connect(db_file_name)
    db.row_factory = dict_factory
    c = db.cursor()
    c.execute("SELECT url FROM {} where hash LIKE \'{}\'".format(database, hashcode))
    data = c.fetchall()[0]
    db.commit()
    db.close()

    return str(data['url'])