import psutil
from shutil import move


def write_name(name, path):
    try:
        file = open(path, 'w')
        file.write(name + '\n')
        file.close()
        print("Name has been written to file")
    except Exception as e:
        print(e)


def read_name(path):
    try:
        file = open(path, 'r')
        print(file.read())
        file.close()
    except Exception as e:
        print(e)


def free_disk_size():
    total_size = psutil.disk_usage('C:').free
    print('Total Size:', total_size, ' GB')


def move_file(source, destination):
    try:
        move(source, destination)
        print("File has been moved")
    except Exception as e:
        print(e)


write_name("Yoel", r'c:\temp\file.txt')
read_name(r'c:\temp\file.txt')
print(free_disk_size())
move_file(r'c:\temp\file.txt', r'c:\temp\new_folder\file.txt')
