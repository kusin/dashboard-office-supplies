# lib manipulation data
import numpy as np
import pandas as pd
# ----------------------------------------------------------------------------------------------

def get_data():

    # load-dataset with parse date
    dataset = pd.read_csv("dataset/dataset-supply.csv", parse_dates=["Ship Date"])

    # convert month to object
    dataset['Month'] = dataset['Ship Date'].dt.month
    
    # return values
    return dataset
    # ----------------------------------------------------------------------------------------------

# def profit(dataset):

#     # calculate all profit
#     df = 
    
#     # return values
#     return dataset
    # ----------------------------------------------------------------------------------------------