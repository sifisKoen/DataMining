class CompareSignatures:

    @staticmethod
    def compare(signature1, signature2):
        intersection = 0
        for i in range(len(signature1)):
            if signature1[i] == signature2[i]:
                intersection = intersection + 1
        return round(intersection / len(signature1), 3)
