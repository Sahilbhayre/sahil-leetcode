import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    
    # 1. Calculate the order count for each customer and broadcast it back
    orders['order_count'] = orders.groupby('customer_number')['order_number'].transform('count')
    
    # 2. Filter for rows matching the absolute maximum count
    max_orders = orders[orders['order_count'] == orders['order_count'].max()]
    
    # 3. Extract unique customer numbers and drop duplicates
    result = max_orders[['customer_number']].drop_duplicates()
    
    return result