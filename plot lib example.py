import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


df1 = pd.read_csv('traffic.csv',sep =',')
# df2 = df1['NE Name'].str.startswith('UPBNB01')

df1 = df1.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')
UPCBT03 = df1[(df1['NE Name'] == 'UPCBT03')]
UPPLB02 = df1[(df1['NE Name'] == 'UPPLB02')]
UPBNB02 = df1[(df1['NE Name'] == 'UPBNB02')]
UPPNB04 = df1[(df1['NE Name'] == 'UPPNB04')]
UPPNB06 = df1[(df1['NE Name'] == 'UPPNB06')] 

dfhead= df1.head()
print(dfhead)

headerinfo =  "User Plane L7 parser DNS uplink packets (number)"

time = UPCBT03["Start Time"]
y = UPCBT03[headerinfo]
y1 = UPPLB02[headerinfo]
y2 = UPBNB02[headerinfo]
y3 = UPPNB04[headerinfo]
y4 = UPPNB06[headerinfo]


plt.title('Traffic')
plt.plot(time,y, linewidth=0.5)
plt.plot(time,y1, linewidth=0.5)
plt.plot(time,y2, linewidth=0.5)
plt.plot(time,y3, linewidth=0.5)
plt.plot(time,y4, linewidth=0.5)
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.show()


