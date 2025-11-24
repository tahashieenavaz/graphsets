from datasets import CoraDataset


def load_cora(path):
    return CoraDataset().load(path)
