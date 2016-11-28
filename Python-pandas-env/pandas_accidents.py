import pandas as pd

# Read the file
data = pd.read_csv("../Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))
