import itertools


class APriory:

    def __init__(self, support):
        self.transactions = None
        self.single_hash_map = None
        self.support = support

    # Read a file and build L1 set
    def process_file(self):
        transactions = []
        hash_map = {}
        with open('./data/T10I4D100K.dat') as file:
            for line in file.readlines():
                basket = line.split()
                for item in basket:
                    if hash_map.get(item) is not None:
                        hash_map[item] += 1
                    else:
                        hash_map[item] = 1
                transactions.append(basket)
        transactions.sort()
        self.transactions = transactions
        self.single_hash_map = self.count_ln_support(hash_map, self.support)
        print("Singleton number: " + str(len(self.single_hash_map)))
        return self.single_hash_map

    # Generate singletons
    @staticmethod
    def generate_l1(ln_list):
        singletons = set()
        for key in ln_list.keys():
            if isinstance(key, tuple):
                for item in key:
                    singletons.add(item)
            else:
                singletons.add(key)
        return singletons

    # Generate Ln set
    def generate_ln_sets(self, ln_1, n):
        ln = {}
        # Generate singletons to check within each basket
        l1 = self.generate_l1(ln_1)
        for basket in self.transactions:
            support_basket = sorted(l1.intersection(basket))
            # Create a next candidates generation
            candidates = sorted(itertools.combinations(support_basket, n))
            for candidate in candidates:
                # Check if a candidate is present in a previous Ln set
                if self.check_smaller_candidates(candidate, ln_1, n):
                    if candidate in ln:
                        ln[candidate] += 1
                    else:
                        ln[candidate] = 1
        # Count supported items
        return self.count_ln_support(ln, self.support)

    @staticmethod
    def count_ln_support(l_map, threshold):
        for key in list(l_map):
            # if isinstance(key, tuple):
            #     key = tuple(sorted(key))
            if l_map.get(key) < threshold:
                del l_map[key]
        return l_map

    @staticmethod
    def check_smaller_candidates(item, ln_1, n):
        combinations = sorted(itertools.combinations(list(item), n - 1))
        for key in combinations:
            # Process 1-tuple
            if len(key) == 1:
                if key[0] not in ln_1:
                    return False
            # Process n-tuple
            elif key not in ln_1:
                return False
        return True
