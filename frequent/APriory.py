class APriory:

    def __init__(self):
        self.transactions = None

    def read_file(self):

        transactions = []
        hash_map = {}
        with open('./data/T10I4D100K.dat') as file:
            for line in file.readlines():
                basket = line.split()
                for item in basket:
                    if hash_map.get(item) is not None:
                        counter = hash_map.get(item)
                        hash_map[item] = counter + 1
                    else:
                        hash_map[item] = 1
                transactions.append(basket)
        self.transactions = transactions
        print("Successful read.")
        return hash_map

    def clean_up_map(self, hash_map, threshold):
        new_hash_map = {}
        pair_map = {}
        for key in hash_map.keys():
            if hash_map.get(key) > threshold:
                new_hash_map[key] = hash_map.get(key)
        pairs = list(zip(*[iter(new_hash_map.keys())] * 2))

        for pair in pairs:
            for transaction in self.transactions:
                if set(pair).issubset(set(transaction)):
                    if pair_map.get(pair) is not None:
                        counter = pair_map.get(pair)
                        pair_map[pair] = counter + 1
                    else:
                        pair_map[pair] = 1
        return pair_map
