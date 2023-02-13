from os import *
from re import compile


class FileSystemIterator:
    def __init__(self, root: str, pattern: str = "\S*", only_files: bool = False, only_dirs: bool = False):
        self.main_iter = walk(root)
        self.pattern = pattern
        self.only_files = only_files
        self.only_dirs = only_dirs
        if only_files and only_dirs:
            self.only_dirs = False
        self.elem_iter = None
        self.system_path = root

    def __next__(self):
        if self.elem_iter is not None:
            try:
                cur_elem = next(self.elem_iter)
                while not (compile(self.pattern).match(cur_elem) is not None
                           and (self.only_files and path.isfile(f"{self.system_path}\\{cur_elem}")
                                or self.only_dirs and path.isdir(f"{self.system_path}\\{cur_elem}")
                                or not (self.only_files or self.only_dirs))):
                    cur_elem = next(self.elem_iter)
                return f"{self.system_path}\\{cur_elem}"
            except StopIteration:
                pass
        self.system_path, dirs, files = next(self.main_iter)
        self.elem_iter = (i for i in dirs + files)
        return next(self)

    def __iter__(self):
        return self


path_root = input('')  # Вставте ваш путь
for file in FileSystemIterator(path_root):
    print(file)
