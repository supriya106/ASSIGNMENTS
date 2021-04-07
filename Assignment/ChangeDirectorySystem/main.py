class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        new_split = new_path.split("/")
        old_split = self.current_path.split("/")
        for i in new_split:
            if i == "..":
                new_split.pop(0)
                old_split = old_split[:-1]
        old_split += new_split
        self.current_path = "/".join(old_split)

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path) # /a/b/c/x