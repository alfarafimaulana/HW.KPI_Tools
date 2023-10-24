import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


df1 = pd.read_csv('Test1.csv',sep =',')
# df2 = df1['NE Name'].str.startswith('UPBNB01')

df1 = df1.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')
DPS_ASBC01 = df1[(df1['NE Name'] == 'DPS_ASBC01')]
DPS_ASBC02 = df1[(df1['NE Name'] == 'DPS_ASBC02')]
DPS_ASBC03 = df1[(df1['NE Name'] == 'DPS_ASBC03')]


dfhead= df1.head()
print(dfhead)
headerinfo =  "User Plane L7 parser DNS uplink packets (number)"

time = DPS_ASBC01["Start Time"]
y1 = DPS_ASBC01[headerinfo]
y2 = DPS_ASBC02[headerinfo]
y3 = DPS_ASBC03[headerinfo]



plt.title('Traffic')
plt.plot(time,y1, linewidth=0.5)
plt.plot(time,y2, linewidth=0.5)
plt.plot(time,y3, linewidth=0.5)
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.show()


