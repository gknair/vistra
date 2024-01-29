import pandas as pd
import numpy as np

# Utilized ChatGPT to add comments and function definition to the function defined in the notebooks

def add_missing_slots(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to add missing hourly observations to the wind data DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing wind data.

    Returns:
    pd.DataFrame: The DataFrame with missing hourly observations added.
    '''
    
    # Generate a complete range of hourly datetime objects from the minimum to the maximum datetime in the DataFrame
    full_range = pd.date_range(df['DATETIME'].min(), df['DATETIME'].max(), freq='H')

    # Set the 'DATETIME' column as the index of the DataFrame for easier manipulation
    df = df.set_index("DATETIME")

    # Ensure the index is a DatetimeIndex for proper alignment and reindexing
    df.index = pd.DatetimeIndex(df.index)

    # Reindex the DataFrame to include the full range of hourly datetimes. 
    # This step inserts missing rows (hours) and aligns existing rows with the new hourly index.
    df = df.reindex(full_range)
    
    # Return the modified DataFrame with the missing hourly slots added
    return df


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to perform linear interpolation to fill in missing values in a DataFrame.
    It also marks rows where interpolation has been applied for future analysis.

    Parameters:
    df (pd.DataFrame): The DataFrame that needs missing value treatment.

    Returns:
    pd.DataFrame: DataFrame with missing values filled and an additional column indicating where interpolation was applied.
    '''
    
    # Add a new column to mark rows with missing observations. Initialized to 0 (no missing values).
    df['Missing_Observation'] = 0

    # Mark rows where 'CF' column has missing values (NaNs) as 1 in the 'Missing_Observation' column
    df.loc[df.CF.isna(), 'Missing_Observation'] = 1

    # Define columns to exclude from interpolation (like identifiers or non-numeric columns)
    columns_to_exclude = ['Missing_Observation', 'Date']
    
    # Create a list of columns that will be considered for interpolation
    selected_columns = [col for col in df.columns if col not in columns_to_exclude]

    # Apply linear interpolation to each selected column
    for col in selected_columns:
        df[col] = df[col].interpolate(method='linear')
    
    # Return the DataFrame with missing values filled
    return df
