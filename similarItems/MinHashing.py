from random import Random


class MinHashing:

    def __init__(self):
        # Hash function (ax + b) / c
        self.a = Random.randint(1024)
        self.b = Random.randint(1024)
        self.c = Random.randint(1024)

    def build_min_hash_signature(self, hashed_shingles, k):
        shingle_signature = []
        for shingle in hashed_shingles:
            min_hash = 2 ^ 64 - 1
            for i in range(0, k - 1):
                min_hash_value = shingle_signature.append(self.local_hash(shingle))
                if min_hash_value < min_hash:
                    min_hash = min_hash_value
            shingle_signature.append(min_hash)

        return shingle_signature

    def local_hash(self, shingle):
        (self.a * shingle + self.b) % self.c
