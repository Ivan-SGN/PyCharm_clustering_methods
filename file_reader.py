import numpy as np

class file_reader:

    def read(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except IOError:
            raise Exception("Error with reader: wrong file path")
        if not lines:
            raise Exception("Error with reader: empty file")
        else:
            return self.prepare_data(lines)

    def prepare_data(self, lines):
        res = []
        for e in lines:
            e = e.split()
            res.append([int(e[0]), int(e[1])])
        return np.array(res)



