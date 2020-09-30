import os.path
import traceback                # можно получить стек вызовов из этого модуля

filename = "/file/not/found"

# try:
#     with open("/file/not/found") as f:
#         content = f.read()
# except OSError as err:
#     print(err.errno, err.strerror)

# try:
#     if not os.path.exists(filename):
#         raise ValueError("file not exist", filename)
# except ValueError as err:
#     message, filename = err.args[0], err.args[1]
#     print(message)


# try:
#     with open("/file/not/found") as f:
#         content = f.read()
# except OSError as err:
#     trace = traceback.print_exc()
#     print(trace)

# try:
#     raw = input('enter num: ')
#     if not raw.isdigit():
#         raise ValueError
# except ValueError:
#     print('xz')

# try:
#     raw = input('enter num: ')
#     if not raw.isdigit():
#         raise ValueError("bad num ", raw)
# except ValueError as err:
#     print('xz', err)
#     raise


# try:
#     raw = input('enter num: ')
#     if not raw.isdigit():
#         raise ValueError("bad num ", raw)
# except ValueError as err:
#     print('error', err.args[0], err.args[1])
#     raise TypeError("my error") from err

# assert True
# assert 1==0
# assert 1 == 0, '1 not 0'




def get_user_by_id(id):
    assert isinstance(id, int), 'id must be integer'
    print('search')

if __name__ == "__main__":
    get_user_by_id('foo')