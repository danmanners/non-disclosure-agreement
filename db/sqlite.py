import sqlite3, secrets, json
from datetime import datetime

# Dict Factory, taken from here:
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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

# Create the Table
def create_table(database, db_file_name):
    db = sqlite3.connect(db_file_name)
    c = db.cursor()

    c.execute("CREATE TABLE {}(date text, HostIP text, hash text, url text)".format(database))

    c.close()
    db.commit()
    db.close()

# Create a row in the database
def add_item(database, db_file_name, request_ip, url):
    try:
        j = json.loads(url)['data']
    except:
        j = url

    token_id = secrets.token_hex(32)
    db = sqlite3.connect(db_file_name)
    db.row_factory = dict_factory
    c = db.cursor()
    now = datetime.now().isoformat(timespec='minutes')
    c.execute("INSERT INTO {}(date,HostIP,hash,url) VALUES(?,?,?,?)".format(database), 
        (now, request_ip, token_id, j))
    c.close()
    db.commit()
    db.close()
    return token_id

# Attempt to retrieve data from the database
def get_code(database, db_file_name, token_id):
    db = sqlite3.connect(db_file_name)
    db.row_factory = dict_factory
    c = db.cursor()
    c.execute("SELECT url FROM {} where hash LIKE \'{}\'".format(database, token_id))

    try:
        data = c.fetchall()[0]
    except:
        data = "token deleted, or it never existed."        

    db.commit()
    db.close()

    if isinstance(data, bytes): return data.decode('ascii')
    if isinstance(data, str): return data
    return str(data['url'])

# Attempt to delete a row from the database
def delete_code(database, db_file_name, token_id):
    db = sqlite3.connect(db_file_name)
    db.row_factory = dict_factory
    c = db.cursor()
    c.execute("DELETE FROM {} where hash LIKE \'{}\'".format(database, token_id))
    db.commit()
    db.close()

    return 'token deleted, or it never existed.'