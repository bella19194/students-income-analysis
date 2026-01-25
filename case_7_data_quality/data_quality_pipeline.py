import pandas as pd
import logging
from pathlib import Path

LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / 'pipeline.log',
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)

def main():
    logging.info('Pipeline started')

    raw_path = Path('data/raw')
    files = raw_path.glob('*.csv')

    dfs = []
    for file in files:
        logging.info(f'Reading file: {file.name}')
        df = pd.read_csv(file)
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    total_rows = len(df)

    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    data_quality_mask = (
        df['product'].notna() &
        (df['quantity'] > 0) &
        (df['price'] > 0)
    )

    valid_df = df[data_quality_mask].copy()
    invalid_df = df[~data_quality_mask]

    valid_rows = len(valid_df)
    invalid_rows = len(invalid_df)
    defect_percent = round(invalid_rows / total_rows * 100, 2)

    clean_path = Path('data/clean/sales_clean.csv')
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    valid_df.to_csv(clean_path, index=False)

    valid_df['revenue'] = valid_df['quantity'] * valid_df['price']

    report = (
        valid_df
        .groupby('product')
        .agg(
            total_quantity=('quantity', 'sum'),
            total_revenue=('revenue', 'sum')
        )
        .sort_values('total_revenue', ascending=False)
    )

    report_path = Path('data/reports/monthly_report.csv')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(report_path)

    logging.info(f'Total rows: {total_rows}')
    logging.info(f'Valid rows: {valid_rows}')
    logging.info(f'Invalid rows: {invalid_rows}')
    logging.info(f'Defect percent: {defect_percent}%')
    logging.info('Pipeline finished successfully')

    print('Pipeline finished')
    print('Всего строк:', total_rows)
    print('Валидных:', valid_rows)
    print('Невалидных:', invalid_rows)
    print('Процент брака:', defect_percent, '%')


if __name__ == '__main__':
    main()



