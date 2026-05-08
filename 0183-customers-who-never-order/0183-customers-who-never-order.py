import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(
        orders, 
        left_on='id', 
        right_on='customerId', 
        how = 'left'
    )

    result = merged[merged["customerId"].isna()][["name"]]
    
    return result.rename(columns={"name": "Customers"}) \
                 .sort_values("Customers") \
                 .reset_index(drop=True)