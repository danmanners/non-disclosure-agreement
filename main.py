import os, time, json
from flask import Flask, redirect, request, make_response

import redis

from functions.routes import main_page
from functions.redis_Call import add_item, get_item, del_item

# Start NDA
nda = Flask(__name__)

# Route to Main Page
nda.add_url_rule("/", "main_page", main_page)

# Create New Token
@nda.route('/new/', methods=['GET','POST'])
def create_hash():
    if request.method == 'POST':
        data = request.get_data().decode("utf-8")

        return str(add_item(data, request.remote_addr))

    elif request.method == 'GET':
        return "Null"

# Retrieve or Delete Existing Token
@nda.route('/<token_id>', methods=['GET','POST','DELETE'])
def token_return(token_id):
    # Retrieving data from the token
    if request.method == 'GET':
        output = get_item(token_id)
        # URL Redirection
        try:
            if type(output) is dict:
                data = json.dumps(output['data'])

                if data.startswith("http"):
                    print("True")
                elif data.startswith("\""):
                    print("False")
                else:
                    print("False")

                if data.startswith("http"):
                    return redirect(data, code=302)
                if data.startswith("www."):
                    return redirect(str("http://" + data), code=302)
                # Bog-standard return of the output
            else:
                return output
        except:
            return output
    # You're not allowed to POST here.
    elif request.method == 'POST':
        return "Null"
    # Trying to figure out what kind of server is responding. Nope.
    elif request.method == 'HEAD':
        resp = make_response()
        resp.headers['Server'] = 'Trying to get some head?'
        return resp
    # Attempting to Delete
    elif request.method == "DELETE":
        output = del_item(token_id)
        return output
    else:
        return "Big Nope, my dude."

# If Running as the primary application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    nda.run(host='0.0.0.0', port=port)
