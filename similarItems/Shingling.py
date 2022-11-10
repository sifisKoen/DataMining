class Shingling:

    def __init__(self, file_name):
        self.file_name = file_name
        self.document = None
        self.shingles = None
        self.hashed_shingles = None

    def read_file(self):
        print("Trying to read: " + str(self.file_name))
        with open(self.file_name) as file:
            self.document = file.read()
            print("Successful read: " + str(self.file_name))

    def build_shingles(self, k):
        shingles = []

        for i in range(0, len(self.document) - k):
            shingles.append(self.document[i: i + k])

        print("Number of shingles from file " + str(self.file_name) + ": " + str(len(shingles)))
        list.sort(shingles)
        self.shingles = shingles

    def hash_shingles(self):
        hashed_shingles = []

        for i in range(0, len(self.shingles)):
        #     print("Shingle: " + str(self.shingles[i]))
            hashed_shingles.append(hash(self.shingles[i]))

        self.hashed_shingles = hashed_shingles
