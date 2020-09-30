import os

class FileReader:
    def __init__(self, path):
        self.path = path

    def open_read(self):
        try:
            with open(self.path, 'r') as f:
                print(f.read())
        except OSError:
            print('')

    # path = property()
    
    # @path.setter
    # def path(self, value):
    #     if os.path.exists(value):
    #         self.path = value 
    #     else:
    #         return ''

    # @path.getter
    # def path(self):
    #     return self.path

reader = FileReader(r'D:\Learn\python\links.txt')
reader.open_read()