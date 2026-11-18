# coding: utf-8
"""Fashion-MNIST 불러오기 — 책의 mnist.py와 사용법이 같다.

    from dataset.fashion_mnist import load_fashion_mnist, CLASS_NAMES
    (x_train, t_train), (x_test, t_test) = load_fashion_mnist(normalize=True, one_hot_label=True)

파일 위치: C:\\Deeplerning\\dataset\\fashion\\ 에 .gz 4개
(MNIST와 파일 이름이 같아서 폴더를 따로 둔다)
처음 부를 때 .gz → NumPy 배열로 바꿔서 fashion_mnist.pkl로 저장해 두고, 다음부터는 pkl을 읽는다.
"""
import os
import gzip
import pickle
import numpy as np

dataset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fashion')
save_file = os.path.join(dataset_dir, 'fashion_mnist.pkl')

key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz',
}

# 정답 숫자 0~9가 뜻하는 옷 종류
CLASS_NAMES = ['티셔츠/탑', '바지', '풀오버', '드레스', '코트',
               '샌들', '셔츠', '스니커즈', '가방', '앵클부츠']

img_size = 784


def _load_label(file_name):
    with gzip.open(os.path.join(dataset_dir, file_name), 'rb') as f:
        return np.frombuffer(f.read(), np.uint8, offset=8)


def _load_img(file_name):
    with gzip.open(os.path.join(dataset_dir, file_name), 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    return data.reshape(-1, img_size)


def init_fashion_mnist():
    for name in key_file.values():
        if not os.path.exists(os.path.join(dataset_dir, name)):
            raise FileNotFoundError(f'{name} 이(가) {dataset_dir} 에 없어요. Fashion-MNIST .gz 파일 4개를 넣어 주세요.')
    print('Converting Fashion-MNIST to NumPy Array ...')
    dataset = {
        'train_img': _load_img(key_file['train_img']),
        'train_label': _load_label(key_file['train_label']),
        'test_img': _load_img(key_file['test_img']),
        'test_label': _load_label(key_file['test_label']),
    }
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    print('Done!')


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    T[np.arange(X.size), X] = 1   # 4장의 '짝지어 꺼내기'로 정답 자리만 1
    return T


def load_fashion_mnist(normalize=True, flatten=True, one_hot_label=False):
    """(훈련 이미지, 훈련 레이블), (시험 이미지, 시험 레이블)을 돌려준다. 인자는 load_mnist와 같다."""
    if not os.path.exists(save_file):
        init_fashion_mnist()

    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32) / 255.0

    if one_hot_label:
        for key in ('train_label', 'test_label'):
            dataset[key] = _change_one_hot_label(dataset[key])

    if not flatten:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])
