import os
import json

class AzWiki:
    def __init__(self, folder):
        self.folder = folder
        self.files = os.listdir(self.folder)
        self.current = 0
        self.max = len(self.files) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max:
            self.current += 1

            filename = self.files[self.current]
            filepath = os.path.join(self.folder, filename)

            with open(filepath, "r") as f:
                content = json.load(f)

            return content
            
        raise StopIteration

    def __call__(self):
        for i in range(self.max):
            sample = next(self)

            yield sample
