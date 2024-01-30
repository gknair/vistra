## Vistra Wind Power Electricty Model 

- The repository is divided into 4 folders. 
- The notebooks 01xx.ipynb -> 03xx.ipynb are utilized for data exploration, feature engineering, model development, testing and hypertuning.  
- The data folder contains raw data, transformed data and visuals for analysis  
- The src folders contains a repo of functions and constants that can be used for productionlizing the code.  
    - ChatGPT is utilized to create comments and enhancing the function definitions.



## Model Selected
- XGBoost model has been utilized to predict the values. An MAE of 0.0409 is achieved as performance on a 10 fold train test set   
- Comparison of results with baseline and LightGBM provided evidence that a tuned XGBoost model performs best
- The lag features and date time feaetures do not rank high in the feature importance


## Additional Notes

- As next steps, ARIMA models can be tested to check if the patterns could be better mapped with statistical models
- There are around 16 days which do not have values every hour, This could be investigated to ascertain the cause of the same. Current assumptions are that the data was not captured. If there were events that allude to different issues , this could be incoorporated in the data set.


