import itertools


class Associations:

    # frequent_items ->[
    #   {"k1":"v1" .., "kn":"vn"},
    #   {"k1, k11": "v1".., "kn, knn": "vn"}]
    def get_rules(self, frequent_items, confidence):
        rules = {}
        for i in range(len(frequent_items) - 1, 0, -1):
            for key in frequent_items[i]:
                combinations = list(itertools.combinations(key, i))
                for combination in combinations:
                    then_item = (set(key) - set(combination)).pop()
                    if len(combination) == 1:
                        combination = combination[0]
                    local_confidence = round(frequent_items[i].get(key) / frequent_items[i - 1].get(combination), 3)
                    if local_confidence > confidence:
                        rules[tuple((combination, then_item))] = local_confidence
        return rules
