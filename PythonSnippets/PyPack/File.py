class FileOwners:

    @staticmethod
    def group_by_owners(files):
        print(files.values())
        for i in files:
            f = open(i, "w+")
            owner = i
        #return None

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Kelly'
}

print(FileOwners.group_by_owners(files))