import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":

    # return error if dataset does not exist
    if not os.path.exists(f'{dir_path}/dataset'):
        print('Dataset directory does not exist. Please run download-dataset.py first.')
        exit(1)

    # create binaries directory if it doesn't exist
    if not os.path.exists(f'{dir_path}/dataset/filtered'):
        os.makedirs(f'{dir_path}/dataset/filtered/binaries')

    # load metadata
    metadata_input = open(f'{dir_path}/dataset/unfiltered/metadata.json', 'r')
    data = json.load(metadata_input)

    print('Filtering dataset...\n')
    print(f'{"COLLECTION METHOD":<30} FILE HASH')

    # filter binaries
    binary_count = 0
    for file_hash in data:
        for file_data in data[file_hash]['files']:
            if 'web' in file_data['collection_method']:
                print(f'{file_data["collection_method"]:<30} {file_hash}')
                os.system(
                    f'cp {dir_path}/dataset/unfiltered/binaries/{file_hash}.wasm {dir_path}/dataset/filtered/binaries/{file_hash}.wasm')
                binary_count += 1
                break

    print(f'\nDone filtering dataset. {binary_count} binaries were copied.')

    metadata_input.close()
