import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').filter(lambda x: len(x) >= 5)

    return df[['class']].drop_duplicates()