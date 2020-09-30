import os
from test import File

file = File('some_text')
file2 = File('some_text_2')
file.write('hello ')
file2.write(' borys')
file3 = file + file2

print(file2)