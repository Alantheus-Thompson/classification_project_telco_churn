from env import get_db_url
import pandas as pd
from pydataset import data
import os

def get_telco_data():
    
    '''
    
    This function retrieves data from the 'customers' table in the 'telco_churn' database, and joins it with the 'contract_types', 'internet_service_types', and 'payment_types' tables. The resulting dataframe contains information about customers' contracts, internet service types, payment types, and other relevant information.
    
    '''
    
    filename = "churn.csv"
        
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)

    else:
        url = get_db_url('telco_churn')
        df_telco_churn = pd.read_sql(('''
        SELECT * From customers
        join contract_types
            using (contract_type_id)
        join internet_service_types
            using(internet_service_type_id)
        join payment_types
            using(payment_type_id)'''), url)
        df_telco_churn.to_csv(filename)
    return df_telco_churn     
  

