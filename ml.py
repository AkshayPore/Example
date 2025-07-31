import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklean.LinearModel import LinearRegression

data=pd.read_csv("E:/python/Datasets/004 1.01.Simple-linear-regression.csv")
data.head()