import pickle
import os


def write_result(result, path='storage/result.set'):
    with open(path, 'wb') as file:
        pickle.dump(result, file)


def read_result(path='storage/result.set'):
    if not os.path.exists(path):
        return set()
    else:
        with open(path, 'rb') as file:
            return pickle.load(file)
