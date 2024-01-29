import pandas as pd
import numpy as np


def add_lags_feature(df: pd.DataFrame, lags: int, skip_lags: int = 24, drop_na: bool = True) -> pd.DataFrame:
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

    Returns:
    pd.DataFrame: The DataFrame with added lagged features.
    '''
    # Iterate over the range of lags and create a new column for each lag
    for i in range(0, lags):
        # Shift the 'CF' column by 'skip_lags + i' and create a new column
        df[f'CF_previous_{i + skip_lags}_hours'] = df['CF'].shift(skip_lags + i)

    # Optionally drop rows with NA values that result from lagging
    if drop_na:
        df.dropna(inplace=True)

    return df
