import logging

import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CSV_FILE_PATH = Path(__file__).parents[1] / 'data.csv'
PARQUET_FILE_PATH = Path(__file__).parents[1] / 'data.parquet'


def main():
    logger.info(f'Starting...')

    file_path = Path(CSV_FILE_PATH)
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10]})
    df.to_parquet(file_path)

    df = pd.read_parquet(file_path)
    logger.info(df)

    logger.info(f'Finished!')


if __name__ == '__main__':
    main()
