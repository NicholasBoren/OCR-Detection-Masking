import torch
from torch.utils.data import Dataset
from doctr.datasets import SROIE
from pathlib import Path

from .file_utils import get_main_path

def load_dataset(dataset: str):
    data_path = get_main_path() / 'data'

    if dataset.lower() == 'sroie':
        train_set = SROIE(train=True, download=True)


if __name__ == '__main__':
    load_dataset('SROIE')
