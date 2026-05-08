import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates()
    sorted_salary = unique_salary.sort_values(ascending=False)
    if len(unique_salary) <= 1:
        result =  None
    else:
        result = sorted_salary.iloc[1]
    return pd.DataFrame({f'SecondHighestSalary': [result]})