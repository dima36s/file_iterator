import os


class FileIterator:
    def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

    def __iter__(self):
        return self.file_iter(self.root)

    def file_iter(self, root):
        for filename in os.listdir(root):
            path = os.path.join(root, filename)
            if os.path.isdir(path):
                if not self.only_files and (not self.only_dirs or self.only_dirs and self._match_pattern(filename)):
                    yield path
                    yield from self.file_iter(path)
            elif not self.only_dirs and (not self.only_files or self.only_files and self._match_pattern(filename)):
                yield path

    def _match_pattern(self, filename):
        if self.pattern:
            return self.pattern in filename
        else:
            return os.path.isfile(os.path.join(self.root, filename))


n = input('Вставте свой путь: ')
for filename in FileIterator(n):
    print(filename)
