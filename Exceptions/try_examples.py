""""""

try:
    with open('my_file.txt') as fh:
        file_data = fh.read()
        print(file_data)
except FileNotFoundError:
    print("There's no 'my_file.txt' mate")
except PermissionError:
    print("Don't have permission to open this")
except Exception as ex:
    print('Request could not be completed. An exception occured: ', str(ex))
