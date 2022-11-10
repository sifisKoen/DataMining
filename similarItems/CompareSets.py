class CompareSets:

    @staticmethod
    def compare(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return round(len(set1.intersection(set2)) / len(set1.union(set2)), 2)
