import re


class Shingling:

    def __init__(self, file_name):
        self.file_name = file_name
        self.document = None
        self.shingles = None
        self.hashed_shingles = None
        self.hashed_signatures = None

    # Read file for shingling
    def read_file(self):
        print("Trying to read: " + str(self.file_name))
        with open(self.file_name) as file:
            content = file.read()
            # Clean shingles
            content = content.replace("\n", " ") \
                .replace("  ", " ")
            content = re.sub(r'([^\w\s]|_)', '', content)
            self.document = content

            print("Successful read: " + str(self.file_name))

    # Build shingles from file content
    # document -> [ [s,h,i,n,g,l,e,1], [s,h,i,n,g,l,e,2] ]
    def build_shingles(self, k):
        shingles = []
        for i in range(0, len(self.document) - k):
            shingles.append(self.document[i: i + k])

        print("Number of shingles from file " + str(self.file_name) + ": " + str(len(shingles)))
        list.sort(list(set(shingles)))
        self.shingles = shingles

    # Hash built shingles
    # [ [s,h,i,n,g,l,e,1], [s,h,i,n,g,l,e,2] ] -> [123, 345]
    def hash_shingles(self):
        hashed_shingles = []
        for i in range(0, len(self.shingles)):
            hashed_shingles.append(hash(self.shingles[i]))
        self.hashed_shingles = hashed_shingles

    def set_signatures(self, hashed_signatures):
        self.hashed_signatures = hashed_signatures
