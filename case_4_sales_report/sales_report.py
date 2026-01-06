import pandas as pd

def main():
    df = pd.read_csv('data/sales_raw.csv')
    total_rows = len(df)

    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    valid_mask = (
        df['product'].notna() &
        (df['quantity'] > 0) &
        (df['price'] > 0)
    )

    valid_df = df[valid_mask].copy()
    invalid_rows = total_rows - len(valid_df)

    valid_df['revenue'] = valid_df['quantity'] * valid_df['price']

    report = (
        valid_df
        .groupby('product')
        .agg(
            total_quantity = ('quantity', 'sum'),
            total_revenue = ('revenue', 'sum')
        )
        .sort_values('total_revenue', ascending = False)
    )

    total_revenue = report['total_revenue'].sum()
    top_product = report.index[0]

    print('Всего строк в файле:', total_rows)
    print('Невалидных строк:', invalid_rows)
    print('\nОтчёт по продуктам:')
    print(report)
    print('Самый прибыльный продукт:', top_product)
    print('\nОбщая выручка:', total_revenue)

if __name__ == '__main__':
    main()


