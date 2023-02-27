import os


class FilesystemIterator:
    def __init__(self, root_dir):
        self.root_dir = os.path.abspath(root_dir)

    def iterate_files(self, directory):
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):
                yield full_path
            elif os.path.isdir(full_path):
                yield from self.iterate_files(full_path)

    def __iter__(self):
        return self.iterate_files(self.root_dir)


n = input('Вставте свой путь: ')
file_iter = FilesystemIterator(n)
for i in file_iter:
    print(i)
