import os, json, secrets, datetime
import redis

r = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=os.environ.get("REDIS_PORT"),
    password=os.environ.get("REDIS_PASS"),
    charset="utf-8",
    decode_responses=True
)

# Create the item in Redis
def add_item(url, request_ip):
    try:
        j = json.loads(url)['data']
    except:
        j = url

    token_id = secrets.token_hex(32)
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    data = json.dumps({
        'data': j,
        'original_ip': request_ip,
        'utc_creation_time': timestamp
    })
    r.set(token_id, data)
    return token_id + "\n"

# Get an item from Redis
def get_item(token_id):
    try:
        data = json.loads(r.get(token_id))
        return data
    except:
        return 'token deleted, or it never existed.'

# Delete an item from Redis
def del_item(token_id):
    r.delete(token_id)
    return 'token deleted, or it never existed.'
