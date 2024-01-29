import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from sklearn.model_selection import TimeSeriesSplit

def add_lags_feature(df: pd.DataFrame, lags: int, skip_lags: int = 24, drop_na: bool = True, target_column: str="CF") -> pd.DataFrame:
    '''
    Adds lagged features to a DataFrame for time series analysis.

    This function shifts a specified column ('CF') by a range of periods (lags), 
    creating new columns for each shifted period. The function can skip a certain number of initial lags 
    (defined by skip_lags) and has an option to drop rows with NA values that result from lagging.

    Parameters:
    df (pd.DataFrame): The DataFrame to which lagged features will be added.
    lags (int): The total number of lags to create.
    skip_lags (int, optional): The number of initial lags to skip. Defaults to 24.
    drop_na (bool, optional): Whether to drop rows with NA values. Defaults to True.
    target_column(str, optional): The target column of the dataframe

    Returns:
    pd.DataFrame: The DataFrame with added lagged features.
    '''
    # Iterate over the range of lags and create a new column for each lag
    for i in range(0, lags):
        # Shift the target column by 'skip_lags + i' and create a new column
        df[f'{target_column}_previous_{i + skip_lags}_hours'] = df[target_column].shift(skip_lags + i)

    # Optionally drop rows with NA values that result from lagging
    if drop_na:
        df.dropna(inplace=True)

    return df



def train_test_kfolds(df: pd.DataFrame, time_split: TimeSeriesSplit, features_target: List) -> Dict[str, Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]]:
    '''
    Create time series split of k folds based on the TimeSeriesSplit object.
    The key in the returned dictionary is the last date of the training set.
    The value is a Tuple of (X_train, y_train, X_test, y_test).
    The first column of the dataframe should be the target column.
    The dataframe should have a timeseries index.

    Parameters:
    df (DataFrame): The DataFrame to split.
    time_split (TimeSeriesSplit): An instance of TimeSeriesSplit for splitting the data.
    features_target (List[str]): List of column names to include, with the target column first.

    Returns:
    Dict[strTuple[DataFrame, DataFrame, DataFrame, DataFrame]]: 
        A dictionary where keys are the last date of the training set, 
        and values are tuples of (X_train, y_train, X_test, y_test).
    '''

    output = {}
    df_topnfeatures = df[features_target]

    for i, (train_index, test_index) in enumerate(time_split.split(df_topnfeatures)):
        # Extracting train and test sets based on the indices provided by TimeSeriesSplit
        X_train = df_topnfeatures.iloc[train_index, 1:]
        y_train = df_topnfeatures.iloc[train_index, 0]
        X_test = df_topnfeatures.iloc[test_index, 1:]
        y_test = df_topnfeatures.iloc[test_index, 0]

        # Storing the splits in a dictionary with the last date of the training set as the key
        output[X_train.index.max()] = (X_train, y_train, X_test, y_test)

    return output
