import itertools

from similarItems.CompareSignatures import CompareSignatures


class LSH:

    def __init__(self, candidates):
        self.candidates = candidates
        self.document_dict = dict()
        for candidate in candidates:
            self.document_dict[candidate.file_name] = candidate

    def find_similar_pairs(self, k_bands, threshold):
        bands = self.band_signatures(self.candidates, k_bands)
        candidates_lists = []
        candidates_pairs = []
        for i in range(k_bands):
            buckets = dict()
            # Choose the same bucket from each document and hash it.
            for doc_name, band_list in bands.items():
                local_hash = self.lsh_hash(band_list[i], 2048)
                if buckets.get(local_hash) is None:
                    buckets[local_hash] = []
                buckets.get(local_hash).append({doc_name: band_list[i]})

            for bucket in buckets.values():
                if len(bucket) > 1:
                    bucket_candidates = []
                    for item in bucket:
                        keys = list(item.keys())
                        for key in keys:
                            bucket_candidates.append(key)
                    candidates_lists.append(bucket_candidates)

            for candidate_list in candidates_lists:
                candidates_pairs.append(list(itertools.combinations(candidate_list, 2)))

        final_candidates_pairs = self.unfold_list(candidates_pairs)
        return self.filter_candidates(final_candidates_pairs, threshold)

    def filter_candidates(self, candidates, threshold):
        lsh_docs = []
        for pair in candidates:
            similarity = CompareSignatures.compare(self.document_dict[pair[0]].hashed_signatures, self.document_dict[pair[1]].hashed_signatures)
            if similarity >= threshold:
                lsh_docs.append(SimilarDocument(pair[0], pair[1], similarity))
                print("LSH signature similarity for documents " + str(pair[0]) + " and " + str(
                    pair[1]) + ": " + str(similarity))
        return lsh_docs

    # Input data structure:
    # signatures -> [doc_sign1, doc_sign2, ..]
    #   docSignN ->[n1, n2, .., N]
    #
    # Output data structure:
    # document_bands -> [file_name1: doc_sign1, file_name2: doc_sign2, ..]
    #   docSignN ->[band1, band2, .., N]
    #       bandN -> [n1, n2, ..., N]
    @staticmethod
    def band_signatures(signatures, partition):
        if len(signatures[0].hashed_signatures) % partition != 0:
            raise Exception("Each band should be of equal size")
        row = int(len(signatures[0].hashed_signatures) / partition)
        document_bands = {}
        for document in signatures:
            bands = []
            for i in range(0, partition):
                band = []
                for j in range(0, row):
                    band.append(document.hashed_signatures[i * row + j - 1])
                bands.append(band)
            document_bands[document.file_name] = bands
        return document_bands

    @staticmethod
    def lsh_hash(band, k_buckets):
        list_to_tuple = tuple(band)
        return hash(list_to_tuple) % k_buckets

    @staticmethod
    def unfold_list(input_list):
        unfolded = []
        for sublist in input_list:
            for element in sublist:
                unfolded.append(element)
        return list(set(unfolded))


class SimilarDocument:

    def __init__(self, doc1, doc2, similarity):
        self.doc1 = doc1
        self.doc2 = doc2
        self.similarity = similarity
