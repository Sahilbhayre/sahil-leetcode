import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = accounts[accounts['income']<20000].shape[0]
    avg_count = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
    high_count = accounts[accounts['income'] > 50000].shape[0]

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count' : [low_count, avg_count, high_count]
    })

    return result