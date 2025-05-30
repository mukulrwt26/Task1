import pandas as pd
import numpy as np
from extract import extract_data
from transform import transform_data
from load import load_data

def etl_pipeline_func(inputData,outputData):
    df=extract_data(inputData)
    df_transformed=transform_data(df)
    load_data(df_transformed,outputData)




if __name__=='__main__':
    etl_pipeline_func("Fashion_Retail_Sales.csv","output_data.csv")