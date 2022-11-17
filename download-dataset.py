# Downloads dataset from https://github.com/sola-st/WasmBench/releases/download/v1.0/filtered-binaries-metadata.7z

import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))


def show_progress(block_num, block_size, total_size):
    print(
        f'Downloading dataset: {round(block_num * block_size / total_size * 100, 1):.1f}%', end="\r")


if __name__ == "__main__":

    # create dataset directory if it doesn't exist
    if not os.path.exists(f'{dir_path}/dataset'):
        os.makedirs(f'{dir_path}/dataset/unfiltered/uncompressed')
        os.makedirs(f'{dir_path}/dataset/unfiltered/binaries')

    # download the dataset
    urllib.request.urlretrieve(
        "https://github.com/sola-st/WasmBench/releases/download/v1.0/filtered-binaries-metadata.7z", "dataset/unfiltered/filtered-binaries-metadata.7z", show_progress)

    # uncompress the dataset
    print('Uncompressing dataset...')
    os.system(
        '7z x dataset/unfiltered/filtered-binaries-metadata.7z -o./dataset/unfiltered/uncompressed')

    # move binaries to binaries folder
    os.system(
        f'mv {dir_path}/dataset/unfiltered/uncompressed/filtered/* {dir_path}/dataset/unfiltered/binaries/')
    os.system(
        f'mv {dir_path}/dataset/unfiltered/uncompressed/filtered.pretty.json {dir_path}/dataset/unfiltered/metadata.json')
    os.system(
        f'rm -r {dir_path}/dataset/unfiltered/uncompressed {dir_path}/dataset/unfiltered/filtered-binaries-metadata.7z')
