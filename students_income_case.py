import pandas as pd

def main():
    df = pd.read_csv('data/students_dirty.csv')
    df['lessons'] = pd.to_numeric(df['lessons'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df.dropna()

    df['income'] = df['lessons'] * df['price']

    total_week = df['income'].sum()
    total_month = total_week * 4
    top_student = df.loc[df['income'].idxmax(), 'name']

    print(df)
    print('Доход за неделю:', total_week)
    print('Доход за месяц:', total_month)
    print('Больше всего приносит:', top_student)

if __name__ == '__main__':
    main()
