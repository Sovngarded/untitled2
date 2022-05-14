
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')

tableTask3 = pd.read_csv("C:/Users/Admin/Desktop/vvv/Task3.csv")
print(tableTask3.head(20))

x = tableTask3['record_id']
y = tableTask3['species_id']

plt.plot(x, y, label='real')
plt.show()