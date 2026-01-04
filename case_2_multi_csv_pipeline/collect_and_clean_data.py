import pandas as pd
from pathlib import Path

def main():
    raw_path = Path('data/raw')
    files = raw_path.glob('*.csv')

    dfs = []
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    before = len(df)


    df['lessons'] = pd.to_numeric(df['lessons'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df.dropna()

    after = len(df)

    df['income'] = df['lessons'] * df['price']

    output_path = Path('data/processed/students_final.csv')
    df.to_csv(output_path, index=False)

    total_income = df['income'].sum()

    print('Строк до очистки:', before)
    print('Строк после очистки:', after)
    print('Общий доход:', total_income)

if __name__ == '__main__':
    main()