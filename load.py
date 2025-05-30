import pandas as pd 
import numpy as np

def load_data(df, output):
    print("Loading data to file...")
    df.to_csv(output, index=False)
    print(f"Data saved to {output}")