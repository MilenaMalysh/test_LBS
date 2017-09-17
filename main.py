
def file_reader(filenames):
    def decorator(function):
        def wrapper(*args, **kwargs):
            files = []
            for filename in filenames:
                with open(filename, encoding='utf-8') as filename:
                    lines = filename.readlines()
                lines = [line.split() for line in lines[1:int(lines[0]) + 1]]  # read lines from first to amount defined in line#0
                files.append(lines)
            return function(*args, **kwargs, files=files)
        return wrapper
    return decorator

@file_reader(['task1.txt'])
def task1(files):

    return [' '.join(['Г-жа' if el[2]=='Ж' else 'Г-н', *el[0:2]])for el in sorted(*files, key=lambda x: x[-1])]

@file_reader(['task2_x.txt', 'task2_y.txt'])
def task2(files):
    return [files[0].count(el) for el in files[1]]

if __name__ == '__main__':
    print('Task 1 results\n', task1())
    print('Task 2 results\n', task2())