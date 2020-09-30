import os

class File:
    def __init__(self, path_name, content=''):
        self.content = content
        if os.path.exists(path_name):
            self.path_name = path_name
        else:
            if '.' in path_name:
                with open(path_name, 'w') as _:
                    pass
                self.path_name = path_name
            else:
                with open(path_name + '.txt', 'w') as _:
                    pass
                self.path_name = path_name + '.txt'

    def __str__(self):
        return os.path.abspath(self.path_name)

    def __add__(self, other):
        new_text = File(
            path_name=self.path_name + '_' + other.path_name,
            content=self.get_content() + other.get_content()
        )
        return new_text.save()

    def read(self):
        with open(self.path_name, 'r') as f:
            print(f.read())

    def write(self, value=str):
        self.content = value
        with open(self.path_name, 'w') as f:
            f.write(self.content)

    def get_content(self):
        with open(self.path_name, mode='r', encoding='utf-8') as f:
            return f.read()

    def save(self):
        with open(self.path_name, mode='w', encoding='utf-8') as f:
            f.write(self.content)
    




    