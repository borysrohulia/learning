import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument('--key', default=1, help='Key')
parser.add_argument('--val', default='value', help='Value')

args = parser.parse_args()
key = args.key
val = args.val


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# with open(storage_path, 'w') as f:
#     f.write('')

with open(storage_path, 'r+') as f:
    a = f.read()
    print(a)
    data = []
    if len(a) == 0:
        my_dict = {
            str(key): val
        }
        data.append(my_dict)
        json.dump(data, f)
    else:
        b = json.loads(a)
        print('else1', b)
        obj = b[0]
        if key in obj:
            print('if2')
            d = obj.get(key)
            print(type(d))
            if type(d) == str:
                c = []
                c.append(d)
                c.append(val)
                obj[key] = c
                data.append(obj)
                print(data)
                delText()
                print(f.read())
                json.dump(data, f)
                print(data)
            else:
                print(type(d))
                print('else2')
                print(obj)
                # a.append(val)
        else:
            print('poka')

# obj[k] = []
# obj[k].append(v)
# obj[k].append(val)
# print(', '.join(obj[k]))
# data = []
# data.append(obj)
# json.dump(data, f)

# obj[k].append(val)
# print(', '.join(obj[k]))
# print(obj)
# data = []
# data.append(obj)
# json.dump(data, f)