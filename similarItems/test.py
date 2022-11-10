import itertools

from os import walk

from similarItems.CompareSets import CompareSets
from similarItems.Shingling import Shingling

if __name__ == '__main__':

    # Prepare files
    filenames = next(walk('./data'))[2]
    documents = []
    for file in filenames:
        print("Got file: " + str(file))
        documents.append(Shingling('./data/' + file))

    for document in documents:
        # Read files
        document.read_file()
        # Prepare shingles
        document.build_shingles(10)
        document.hash_shingles()

    # Create pairs
    pairs = list(itertools.combinations(documents, 2))

    # Count Jaccard similarity
    jaccard = []
    for pair in pairs:
        similarity = CompareSets.compare(pair[0].hashed_shingles, pair[1].hashed_shingles)
        jaccard.append(similarity)
        print("Jaccard similarity for documents " + str(pair[0].file_name) + " and " + str(pair[1].file_name) + ": " + str(similarity))




