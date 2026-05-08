import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp','_dept'))

    df['max_salary'] = df.groupby('name_dept')['salary'].transform('max')

    result_df = df[df['salary'] == df['max_salary']]

    result_df = result_df[['name_dept', 'name_emp', 'salary']]

    result_df.columns = ['Department', 'Employee', 'Salary']

    return result_df