import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salary = unique_salaries.sort_values(ascending=False)
    
    if N<=0 or N>len(sorted_salary):
        result = None
    else:
        result = sorted_salary.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})