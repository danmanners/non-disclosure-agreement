import os, time
from flask import Flask, redirect, request, make_response

from routes.routes import main_page
from db.sqlite import check_table_exists, create_table, add_item, get_code

nda = Flask(__name__)

# Route to Main Page
nda.add_url_rule("/", "main_page", main_page)

# Route to Hashcode
@nda.route('/<hashcode>', methods=['GET','POST'])
def hash_return(hashcode):
    if request.method == 'GET':
        output = get_code(database, db_file_name, hashcode)
        if output.startswith("http"):
            return redirect(output, code=302)
        else:
            return output
    elif request.method == 'POST':
        return "Nope, fuck you."
    elif request.method == 'HEAD':
        resp = make_response()
        resp.headers['Server'] = 'Trying to get some head?'
        return resp
    else:
        return "Big Nope, my dude."

@nda.route('/new/', methods=['GET','POST'])
def create_hash():
    if request.method == 'POST':
        data = request.get_data().decode("utf-8")

        return add_item(
            database,
            db_file_name,
            request.remote_addr,
            data
        )
    elif request.method == 'GET':
        return "Nope, fuck you."

# If Running as the primary application
if __name__ == '__main__':

    database     = os.getenv('NDA_DB_NAME','nda_items')
    db_file_name = os.getenv('NDA_DB_FILE','nda.db')

    while check_table_exists(database,db_file_name) is False:
        print("❌ Database '{}' not found. Creating it now.".format(database))
        create_table(database,db_file_name)

    print("✔  Database '{}' found. Starting server.".format(database))

    port = int(os.environ.get('PORT', 3000))
    nda.run(host='0.0.0.0', port=port)