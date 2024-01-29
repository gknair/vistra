import pandas as pd
import numpy as np

import pandas as pd

class BaseLineModelAverage25Hour:
    """
    A baseline model for time series prediction.

    This model predicts the average electricity output based on observed outputs 
    at 24, 25, and 26 hours prior to the current hour. It is designed to provide 
    a simple benchmark for more complex forecasting models.
    """

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        Fit the model to the training data. 

        Since this is a baseline model that makes predictions based on simple 
        averaging, the fit method does not perform any operation.

        Parameters:
        X_train (pd.DataFrame): The training feature data.
        y_train (pd.Series): The training target data.
        """
        # No fitting process as this is a baseline model
        pass

    def predict(self, X_test: pd.DataFrame) -> pd.Series:
        """
        Predict using the baseline model.

        The predictions are computed as the average of the values from the 
        'CF_previous_24_hours', 'CF_previous_25_hours', and 'CF_previous_26_hours' 
        columns of the input DataFrame.

        Parameters:
        X_test (pd.DataFrame): The testing feature data.

        Returns:
        pd.Series: The predicted values as a Pandas Series.
        """
        # Compute the average of the specified previous hour values
        return 0.33 * (X_test['CF_previous_24_hours'] +
                       X_test['CF_previous_25_hours'] +
                       X_test['CF_previous_26_hours'])


import pandas as pd

class BaseLineModelPrevious24Hour:
    """
    A baseline model for time series prediction.

    This model predicts the electricity output based solely on the output 
    observed 24 hours prior, scaled by a factor of 0.85. It offers a simple 
    prediction benchmark for more sophisticated forecasting models.
    """

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        Fit the model to the training data.

        Since this baseline model makes predictions based on a single lagged value
        with a scaling factor, the fit method does not perform any operation.

        Parameters:
        X_train (pd.DataFrame): The training feature data.
        y_train (pd.Series): The training target data.
        """
        # No fitting process as this is a baseline model
        pass

    def predict(self, X_test: pd.DataFrame) -> pd.Series:
        """
        Predict using the baseline model.

        The predictions are made by taking the value from the 
        'CF_previous_24_hours' column of the input DataFrame and scaling it by 0.85.

        Parameters:
        X_test (pd.DataFrame): The testing feature data.

        Returns:
        pd.Series: The predicted values as a Pandas Series.
        """
        # Predicting by scaling the 'CF_previous_24_hours' value by 0.85
        return X_test['CF_previous_24_hours'] * 0.85
