import pandas as pd

chunk_size = 1000
batch_no = 1

# Use raw string literal for file path
file_path = r'E:\Data analytics\Spotify\dataset.csv'

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    chunk.to_csv(f'dataset{batch_no}.csv', index=False)
    batch_no += 1
