import pandas as pd
import os
from pydataset import data
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import env
import acquire as a
import prepare as p
import explore as e

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

def telco_encoded(train, validate, test):
    '''
    For loops through the train, validate, and test dfs to create an encoded df list.  Encoding skips customer id & total charges.  A key feature being evaluated is monthly charges.  Since monthly charges is a float datatype pd.cut is used to create bins that align with corresponding spikes in churn (increments of 30) and labels are created to show bin range.  If datatype is object gets dummies dropping the first subfeature into 0,0 as true indicator.
    
    Parameters:
    train: Training dataset.
    validate: Validation dataset.
    test: Testing dataset.

    '''
    encoded_dfs = []

    for df in [train, validate, test]:
        df_encoded = df.copy()

        for col in df.columns:
            if col == 'customer_id':
                continue
            if col == 'total_charges':
                continue
            elif df[col].dtype == 'O' or col == 'monthly_charges':
                if col == 'monthly_charges':
                    # Convert 'monthly_charges' to categorical bins before one-hot encoding
                    df_encoded['monthly_charges'] = pd.cut(df_encoded['monthly_charges'], bins=[0, 30, 60, 90, 120, float('inf')], labels=['0-30', '30-60', '60-90', '90-120', '120+'])
                df_dummies = pd.get_dummies(df_encoded[col], prefix=col, drop_first=True).astype(int)
                df_encoded = df_encoded.join(df_dummies).drop(columns=[col])

        encoded_dfs.append(df_encoded)

    return encoded_dfs

def prep_xy(df):
    """
    Use function to preprocesses train, validate, and test Telco data and returns X and y.  Ne

    Parameters:
    df: use 

    Returns:
    X (pd.DataFrame): Features.
    y (pd.Series): Target variable.
    """
    # List of columns to drop
    columns_to_drop = [
        'churn_Yes', 'customer_id', 'total_charges', 'senior_citizen', 'tenure',
        'gender_Male', 'partner_Yes', 'dependents_Yes', 'phone_service_Yes',
        'multiple_lines_No phone service', 'multiple_lines_Yes',
        'online_security_No internet service', 'online_security_Yes',
        'online_backup_No internet service', 'online_backup_Yes',
        'device_protection_No internet service', 'device_protection_Yes',
        'tech_support_No internet service', 'tech_support_Yes',
        'streaming_tv_No internet service', 'streaming_tv_Yes',
        'streaming_movies_No internet service', 'streaming_movies_Yes',
        'paperless_billing_Yes'
    ]

    # Drop specified columns
    X = df.drop(columns=columns_to_drop)
    y = df['churn_Yes']

    return X, y

def decision_tree_model(X_train, y_train, X_validate, y_validate, max_depth_values):
    '''
    Train and evaluate Decision Tree models with different max_depth values on the training and validation data to find optimal
    max depth.

    Parameters:
    X_train: Features for training.
    y_train: Target variable for training.
    X_validate: Features for validation.
    y_validate: Target variable for validation.
    max_depth_values (list): List of max_depth values to try.

    '''
    for max_depth in max_depth_values:
        # Create an instance of DecisionTreeClassifier with the current max_depth
        dt_model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

        # Fit the model on the training data
        dt_model.fit(X_train, y_train)

        # Make predictions on the training set
        y_pred_train = dt_model.predict(X_train)

        # Make predictions on the validation set
        y_pred_validate = dt_model.predict(X_validate)

        # Print results for the current max_depth
        print(f"\nResults for max_depth={max_depth}:\n")
        print('Classification Report (Training):\n', classification_report(y_train, y_pred_train))
        print('Classification Report (Validation):\n', classification_report(y_validate, y_pred_validate))