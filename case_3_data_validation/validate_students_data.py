import pandas as pd

def main():
    df = pd.read_csv('data/students_raw.csv')

    total_rows = len(df)

    df['lessons'] = pd.to_numeric(df['lessons'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    valid_mask = (
        df['name'].notna() &
        (df['lessons'] > 0) &
        (df['price'] > 0)
    )

    valid_rows = len(df[valid_mask])
    invalid_rows = len(df[~valid_mask])

    print('Всего строк:', total_rows)
    print('Валидных:', valid_rows)
    print('Невалидных:', invalid_rows)
    print('\nПричины ошибок:')

    if (df['lessons'] <= 0).any():
        print('-lessons <= 0')
    if (df['lessons'].isna()).any():
        print('-lessons не число или пусто')
    if (df['price'] <= 0).any():
        print('-price <= 0')
    if (df['price'].isna()).any():
        print('-price не число или пусто')
    if (df['name'].isna()).any():
        print('-name пустоe')
if __name__ == '__main__':
    main()









