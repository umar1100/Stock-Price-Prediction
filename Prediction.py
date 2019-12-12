import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn.preprocessing

stock_data_bac = pd.read_csv('BAC.csv')
stock_data_bac.info()
stock_data_bac.head()

