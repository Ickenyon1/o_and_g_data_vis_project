###########################################################################
# IMPORT PYTHON LIBRARIES AT THE TOP OF SCRIPT
###########################################################################

# this line imports pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###########################################################################
# READ DATA Files
###########################################################################

# Reading in csv data into variable called 'data'
data = pd.read_csv("data/sample_data.csv")


###########################################################################
# PRE - PROCESS DATA
###########################################################################


# Pandas thinks date column is a string Damn!
print(type(data.iloc[0,0]))

# Converting date column to to type 'datetime'
data['date'] = pd.to_datetime(data['date'])

print("converting...")

# now it's a dateime data type! Yay!
print(type(data.iloc[0,0]))



###########################################################################
# DO ANALYSIS
###########################################################################

# Selecting columns from data and removing date because we don't need that yet
cols = list(data.columns.values)
cols.remove('date')

# Calculating the average of all columns
ave_data = data[cols].mean(axis=0)


###########################################################################
# VISUALISE RESULTS
###########################################################################

# Plotting using pandas in built graphical functions (uses matplotlib).
# NOTE: Might not play well first time
ave_data.plot.bar()
plt.show()

###########################################################################
# OUTPUT RESULTS
###########################################################################

# This line turns pandas series into pandas dataframe and save it to file as a csv
ave_data.to_frame().to_csv("data/output_data.csv")
