class Node:
    def __init__(self, filename, filesize):
        self.filename = filename
        self.filesize = filesize
        self.left = None
        self.right = None

class FolderSearch:
    def __init__(self):
        self.root = None
        self.total_size = 0

    def insert(self, filename, filesize):
        
        self.root = self._insert(self.root, filename, filesize)
        self.total_size += filesize

    def _insert(self, current, filename, filesize):
        if current is None:
            return Node(filename, filesize)

        if filename < current.filename:
            current.left = self._insert(current.left, filename, filesize)
        elif filename > current.filename:
            current.right = self._insert(current.right, filename, filesize)
        
        else:
            self.total_size -= current.filesize  
            current.filesize = filesize

        return current

    def find(self, filename):
        return self._find(self.root, filename) is not None

    def _find(self, current, filename):
        if current is None:
            return None
        if filename == current.filename:
            return current
        elif filename < current.filename:
            return self._find(current.left, filename)
        else:
            return self._find(current.right, filename)

    def file_size(self, filename):
        
        node = self._find(self.root, filename)
        if node:
            return node.filesize
        else:
            return None  

    def folder_size(self):
        if self.total_size == self.filesize:
            return self.filesize
        else:
            return self.total_size

filedata = [
    (13968, 'qml'),
    (130280, 'include'), 
    (93696, 'bin'), 
    (0, 'envs'), 
    (8, 'condabin'), 
    (37704, 'libexec'), 
    (2064, 'share'), 
    (31360, 'conda-meta'), 
    (3234088, 'lib'), 
    (632, 'phrasebooks'), 
    (64, 'etc'), 
    (30536, 'plugins'), 
    (48488, 'man'), 
    (64, 'licensing'), 
    (1064, 'doc'), 
    (2130864, 'pkgs'), 
    (5408, 'mkspecs'), 
    (728, 'sbin'), 
    (7928, 'python.app'), 
    (24, 'LICENSE.txt')]
folder = FolderSearch()
print(folder.find ("bin"))