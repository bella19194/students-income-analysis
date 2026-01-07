import pandas as pd
from pathlib import Path

def main():
    df = pd.read_csv('data/raw/subscriptions_raw.csv')

    df['months'] = pd.to_numeric(df['months'], errors = 'coerce')
    df['price'] = pd.to_numeric(df['price'], errors = 'coerce')

    valid_mask = (
        df['plan'].notna() &
        (df['months'] > 0) &
        (df['price'] > 0)
    )

    valid_df = df[valid_mask].copy()

    clean_path = Path('data/clean/subscriptions_clean.csv')
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    valid_df.to_csv(clean_path, index=False)

    valid_df['revenue'] = valid_df['months'] * valid_df['price']

    report = (
        valid_df
        .groupby('plan')
        .agg(
            total_months = ('months', 'sum'),
            total_revenue = ('revenue', 'sum')
        )
    )

    report_path = Path('data/reports/revenue_report.csv')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(report_path)

    print('Pipeline finished successfully')
    print('Clean data saved to:', clean_path)
    print('Report saved to:', report_path)

if __name__ == '__main__':
    main()
