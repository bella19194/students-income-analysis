import pandas as pd
from pathlib import Path

COLUMN_MAP = {
    'order_id': 'order_id',
    'id': 'order_id',
    'order': 'order_id',

    'product': 'product',
    'product_name': 'product',

    'quantity': 'quantity',
    'qty': 'quantity',

    'price': 'price',
    'unit_price': 'price'
}


def main():
    files = Path('data/raw').glob('*.csv')
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        df = df.rename(columns=COLUMN_MAP)
        df = df[['order_id', 'product', 'quantity', 'price']]
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)

    combined_df['quantity'] = pd.to_numeric(combined_df['quantity'], errors='coerce')
    combined_df['price'] = pd.to_numeric(combined_df['price'], errors='coerce')

    valid_mask = (
        combined_df['product'].notna() &
        (combined_df['quantity'] > 0) &
        (combined_df['price'] > 0)
    )

    valid_df = combined_df[valid_mask].copy()

    clean_path = Path('data/clean/sales_clean.csv')
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    valid_df.to_csv(clean_path, index=False)

    valid_df['revenue'] = valid_df['quantity'] * valid_df['price']

    report = (
       valid_df
        .groupby('product')
        .agg(
           total_quantity = ('quantity', 'sum'),
           total_revenue = ('revenue', 'sum')
       )
        .sort_values('total_revenue', ascending=False)
    )

    report_path = Path('data/reports/monthly_report.csv')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(report_path)

    print('Ingestion pipeline finished successfully')
    print('Clean data saved to:', clean_path)
    print('Report saved to:', report_path)

if __name__ == '__main__':
    main()

