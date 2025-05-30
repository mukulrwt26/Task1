import pandas as pd
import numpy as np

def extract_data(input_data):
    print("Extracted Data.")
    df=pd.read_csv(input_data)
    
    return df