import time

from frequent.APriory import APriory
from frequent.Associations import Associations

if __name__ == '__main__':
    support = 200
    confidence = 0.5
    apriory = APriory(support)
    frequent_items = []

    start = time.time()
    # Created transactions and supported singletons
    ln = APriory.process_file(apriory)

    # Run until no supported sets are left
    n = 2
    while len(ln) > 0:
        k = 0
        for item in ln:
            k += 1
            print("Items  " + str(k) + ": " + str(item) + " -> " + str(ln.get(item)))
        frequent_items.append(ln)
        ln = APriory.generate_ln_sets(apriory, ln, n)
        n += 1

    end = time.time() - start
    print("Spent time " + str(round(end, 3)) + "s.")

    rules = Associations.get_rules(Associations(), frequent_items, confidence)
    k = 0
    for rule in rules:
        k += 1
        print("Rule " + str(k) + ": " + str(rule) + " -> " + str(rules.get(rule)))
