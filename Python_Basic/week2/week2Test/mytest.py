import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'r+') as f:
    f.write(json.dumps({'key': 'Borys'}))

def test(key, val):
    my_key = key
    my_val = val
    with open(storage_path, 'r+') as f:
        a = json.loads(f.read())
        print(a)
        


test('key', 'val')