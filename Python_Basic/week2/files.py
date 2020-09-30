f = open('filename')

text_modes = {
    'r': 'read',
    'w': 'write',
    'a': 'append',
    'r+': 'read and write'
}

binary_modes = ['br', 'bw', 'ba', 'br+']

f = open('filename', 'w')

f.write('string.\n')
f.close()

f = open('filename', 'r+')
f.read()

f.tell()

f.read() # не прочтет, так как файл уже прочтен и мы на последней строк. поэтому надо использовать seek()

f.seek(0)
f.read()

f.seek(0)
f.tell()

print(f.read())
f.close()

f = open('filename', 'r+')
f.readline()
f.close()

f = open('filename', 'r+')
f.readline()
f.close()

with open('filename') as f:
    print(f.read())