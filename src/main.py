import numpy as np
import pandas as pd
import plotly.graph_objects as go

data_file = "../data/penguins.csv"

dataset = pd.read_csv(data_file, sep=',', index_col=0)

print(dataset)



