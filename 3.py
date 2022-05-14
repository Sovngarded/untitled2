
import pandas as pd


from matplotlib import pyplot as plt
plt.style.use('ggplot')

tableTask3 = pd.read_csv("C:/Users/Admin/Desktop/vvv/Task3.csv")
print(tableTask3.head(20))


newTable = tableTask3.loc[tableTask3['gender'] == 'F']
x = newTable['record_id']
y = newTable['species_id']
print(y)#женщин species_id
plt.plot(x, y, label='real')
plt.show() #график