from frequent.APriory import APriory

if __name__ == '__main__':
    apriory = APriory()
    hash_map = APriory.read_file(apriory)
    APriory.clean_up_map(apriory, hash_map, 1000)
