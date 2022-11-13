import itertools
import time

from os import walk

from similarItems.CompareSets import CompareSets
from similarItems.CompareSignatures import CompareSignatures
from similarItems.MinHashing import MinHashing
from similarItems.Shingling import Shingling
from similarItems.LSH import LSH


class Runner:

    @staticmethod
    def run(path, num_of_shingles):
        # CONST
        NUMBER_OF_MIN_HASH_FUNCTIONS = 100
        NUMBER_OF_BANDS = 20
        THRESHOLD = 0.8

        # Prepare files
        filenames = next(walk(path))[2]
        documents = []
        for file in filenames:
            print("Got file: " + str(file))
            documents.append(Shingling(path + file))

        #
        #      SHINGLING METHOD
        #
        shingles_start_time = time.time()
        for document in documents:
            # Read files
            document.read_file()
            # Prepare shingles
            document.build_shingles(num_of_shingles)
            document.hash_shingles()

        # Create pairs of shingles
        pairs = list(itertools.combinations(documents, 2))

        # Count Jaccard similarity for shingles
        jaccard = []
        for pair in pairs:
            similarity = CompareSets.compare(pair[0].hashed_shingles, pair[1].hashed_shingles)
            jaccard.append(similarity)
            print("Jaccard similarity for documents " + str(pair[0].file_name) + " and " + str(
                pair[1].file_name) + ": " + str(similarity))

        shingles_spent_time = time.time() - shingles_start_time
        print("Time spent by Shingling method " + str(shingles_spent_time))

        #
        #      MIN HASHING METHOD
        #
        hashing_start_time = time.time()
        min_hashing = MinHashing(NUMBER_OF_MIN_HASH_FUNCTIONS)
        for document in documents:
            document.set_signatures(min_hashing.build_min_hash_signature(document.hashed_shingles, NUMBER_OF_MIN_HASH_FUNCTIONS))

        # Count Jaccard similarity for signatures
        signature_jaccard = []
        for pair in pairs:
            similarity = CompareSignatures.compare(pair[0].hashed_signatures, pair[1].hashed_signatures)
            signature_jaccard.append(similarity)
            print("Jaccard signature similarity for documents " + str(pair[0].file_name) + " and " + str(
                pair[1].file_name) + ": " + str(similarity))

        hashing_spent_time = time.time() - hashing_start_time
        print("Time spent by Min Hashing method " + str(hashing_spent_time))

        #
        #      LSH METHOD
        #
        lsh_start_time = time.time()

        docs = LSH.find_similar_pairs(LSH(documents), NUMBER_OF_BANDS, THRESHOLD)

        lsh_spent_time = time.time() - lsh_start_time
        print("Time spent by LSH method " + str(lsh_spent_time))
