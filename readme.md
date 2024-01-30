## Vistra Wind Power Electricty Model 

- The repository is divided into 4 folders. 
- The notebooks 01xx.ipynb -> 06xx.ipynb are utilized for data exploration, feature engineering, model development, testing ,hypertuning and prediction  
- The data folder contains raw data, transformed data and visuals for analysis  
- The src folders contains a repo of functions and constants that can be used for productionlizing the code.  
    - ChatGPT is utilized to create comments and enhancing the function definitions.



## Model Selected
- XGBoost model has been utilized to predict the values. An MAE of 0.0408 is achieved as performance on a 10 fold train test set   
- Comparison of results with baseline and LightGBM provided evidence that a tuned XGBoost model performs best
- The lag features and date time feaetures do not rank high in the feature importance


## Next Steps/ Notes

- As next steps, ARIMA models can be tested to check if the patterns could be better mapped with statistical models
- Pipelines can be created to make the model training and testing more seamless. It has not been implemented, currently.
    - There are a few additional functions that need to be created and then these could be transformed using transformer function to create the pipeline
- There are around 16 days which do not have values every hour, This could be investigated to ascertain the cause of the same. Current assumptions are that the data was not captured. If there were events that allude to different issues , this could be incoorporated in the data set.
- The seasonal pattern of wind energy as described by the EIA, is not captured here since the training set does not include multiple years of data.  
Additional data could enable more accurate predictions
- The data files have been comitted to git here since it is a small data excercise, in practice we would not be commit data to a git repo



