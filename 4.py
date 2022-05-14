
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')
tableTask3 = pd.read_csv("C:/Users/Admin/Desktop/vvv/Task3.csv")
print(tableTask3.head(20))

tableTask3desc = tableTask3['hindfoot_length'].describe()

#hmin = tableTask3.min['hindfoot_length']
hmax = tableTask3desc['max']
hmin = tableTask3desc['min']
print(hmax - hmin)