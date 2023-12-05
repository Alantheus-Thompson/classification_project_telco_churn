import pandas as pd
import os
from pydataset import data
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import env
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import acquire as a


def prep_telco():
    
    '''
    
    This function calls the acquire function to get the telco data.  Then drops type_id columns with corresponding 
    factors. Nulls are filled in. Total charges converted from object to float and nulls/nan filled in
    
    '''
    df_telco_churn = a.get_telco_data()
    
    # drop type_id columns due to corresponding factor columns
    df_telco_churn=df_telco_churn.drop(
        columns= [
        'payment_type_id','internet_service_type_id','contract_type_id'
        ],errors='ignore'
    )
    
    # fill Internet service type Nulls
    df_telco_churn['internet_service_type'].fillna("No internet service", inplace=True)
    
    # total charges is detected as an object, but holds mainly numbers. use pd.to_numeric() to force everything to 
    # a number, and anything that it cannot convert, we'll make it Null and investigate those.
    df_telco_churn['total_charges'] = pd.to_numeric(
        df_telco_churn['total_charges'], errors='coerce'
    )
    
    # Total charges = 0 also has Tenure = 0. Assumption: they're new and haven't been charged
    df_telco_churn['total_charges'].fillna(0, inplace=True)
    
    
    # shorten payment type categories for graphing
    df_telco_churn["payment_type"].replace(
        {
            "Electronic check": "electronic check",
            "Mailed check": "mailed check",
            "Credit card (automatic)": "credit card",
            "Bank transfer (automatic)": "bank transfer",
        },
        inplace=True,
    )

    return df_telco_churn
def split_data(df, target_column):
    '''

    Splits a DataFrame into training, validation, and test sets, stratifying on the 'churn' variable.

    Parameters:
    df_telco (pandas.DataFrame): The DataFrame to split.

    Returns:
    tuple: A tuple containing the training, validation, and test DataFrames.
   
    '''
    train, validate_test = train_test_split(df,
                                            train_size=0.60,
                                            random_state=123,
                                            stratify=df[target_column])

 
    validate, test = train_test_split(validate_test,
                                      test_size=0.50,
                                      random_state=123,
                                      stratify=validate_test[target_column])

    return train, validate, test

