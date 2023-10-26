import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd



df1 = pd.read_csv('Test1.csv',sep =',',skiprows=13)
# df2 = df1['NE Name'].str.startswith('UPBNB01')

df1 = df1.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')
DPS_ASBC01 = df1[(df1['NE Name'] == 'SNBASBC01')]
DPS_ASBC02 = df1[(df1['NE Name'] == 'SNBASBC02')]
DPS_ASBC03 = df1[(df1['NE Name'] == 'SNBASBC03')]

headerinfo =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo2 =  "Number of ABCF Successful Initial Registrations (times)"

xdesc = (df1['NE Name'].value_counts()['SNBASBC01'])

time = DPS_ASBC01["Start Time"]
y1 = DPS_ASBC01[headerinfo]
y2 = DPS_ASBC02[headerinfo]
y3 = DPS_ASBC03[headerinfo]

y12 = DPS_ASBC01[headerinfo2]
y22 = DPS_ASBC02[headerinfo2]
y32 = DPS_ASBC03[headerinfo2]

print(xdesc)
# headerinfocount = time.count
# print(headerinfocount)

plt.title('Traffic')
plt.plot(time,y1, linewidth=0.5)
plt.plot(time,y2, linewidth=0.5)
plt.plot(time,y3, linewidth=0.5)
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.xticks([0, xdesc/2,xdesc-1])
plt.show()

# plt.title('Traffic')
# plt.plot(time,y12, linewidth=0.5)
# plt.plot(time,y22, linewidth=0.5)
# plt.plot(time,y32, linewidth=0.5)
# plt.xlabel('Dates')
# plt.ylabel('Nominal (juta)')
# plt.show()





