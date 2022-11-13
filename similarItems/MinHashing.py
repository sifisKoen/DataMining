import random


class MinHashing:

    def __init__(self, number_of_hash_functions):
        # Hash function (ax + b) / c
        self.a = self.random_list(number_of_hash_functions)
        self.b = self.random_list(number_of_hash_functions)
        self.c = pow(2, 32) - 1

    # Build min hash signatures
    # From each shingle set, we choose N min hashed shingles
    # [123, 345] -> [567, 986]
    def build_min_hash_signature(self, hashed_shingles, number_of_hash_functions):
        shingle_signature = []
        for i in range(0, number_of_hash_functions):
            min_hash = pow(2, 64) - 1
            # Find min hash for each shingle
            for shingle in hashed_shingles:
                min_hash_value = self.local_hash(shingle, i)
                if min_hash_value < min_hash:
                    min_hash = min_hash_value
            shingle_signature.append(min_hash)
        return shingle_signature

    def local_hash(self, shingle, i):
        return (self.a[i] * shingle + self.b[i]) % self.c

    @staticmethod
    def random_list(n):
        random_list = []
        for i in range(n):
            random_list.append(random.randint(1, 256))
        return random_list
