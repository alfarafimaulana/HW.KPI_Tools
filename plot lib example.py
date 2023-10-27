import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd



ASBCdf = pd.read_csv('Test3.csv',sep =',',skiprows=13)
ASBCCPUdf = pd.read_csv('ASBCCPUtest.csv',sep =',',skiprows=13)
CPUdf = pd.read_csv('VMCPUload.csv',sep =',',skiprows=13)
SCSCFkpi = pd.read_csv('SCSCF_plot.csv',sep =',',skiprows=13)
# df2 = ASBCdf['NE Name'].str.startswith('UPBNB01')

targetNE1 = 'DPS_ASBC01'
targetNE2 = 'DPS_ASBC02'
targetNE3 = 'DPS_ASBC03'

targetNE4 = 'DPS_CSCF01'


ASBCdf = ASBCdf.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')
ASBCCPUdf = ASBCCPUdf.sort_values(by=['NE Name','Start Time','Module CPU'], ascending=True, na_position='first')
CPUdf = CPUdf.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')
SCSCFkpidf = SCSCFkpi.sort_values(by=['NE Name','Start Time'], ascending=True, na_position='first')

DPS_ASBC01 = ASBCdf[(ASBCdf['NE Name'] == targetNE1 )]
DPS_ASBC02 = ASBCdf[(ASBCdf['NE Name'] == targetNE2 )]
DPS_ASBC03 = ASBCdf[(ASBCdf['NE Name'] == targetNE3 )]

CPU_ASBC01 = ASBCCPUdf[(ASBCCPUdf['NE Name'] == targetNE1 )]
CPU_ASBC02 = ASBCCPUdf[(ASBCCPUdf['NE Name'] == targetNE2 )]
CPU_ASBC03 = ASBCCPUdf[(ASBCCPUdf['NE Name'] == targetNE3 )]

CSCF_DPS = SCSCFkpidf[(SCSCFkpidf['NE Name'] == targetNE4 )]


CPU1 = CPUdf[(CPUdf['NE Name'] == "DPS_ASBC01_CGP" )]
CPU1_LBU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_LBU1_ARM_VDU1_0" )]
CPU1_LBU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_LBU1_ARM_VDU2_0" )]
CPU1_HRU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_HRU3_ARM_VDU_0" )]
CPU1_HRU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_HRU3_ARM_VDU_1" )]
CPU1_HRU3 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_HRU3_ARM_VDU_2" )]
CPU1_HIU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_HIU_ARM_VDU1_0" )]
CPU1_HIU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC01_HIU_ARM_VDU2_0" )]

CPU2 = CPUdf[(CPUdf['NE Name'] == "DPS_ASBC02_CGP" )]
CPU2_LBU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_LBU1_ARM_VDU1_0" )]
CPU2_LBU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_LBU1_ARM_VDU2_0" )]
CPU2_HRU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_HRU3_ARM_VDU_0" )]
CPU2_HRU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_HRU3_ARM_VDU_1" )]
CPU2_HRU3 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_HRU3_ARM_VDU_2" )]
CPU2_HIU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_HIU_ARM_VDU1_0" )]
CPU2_HIU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC02_HIU_ARM_VDU2_0" )]

CPU3 = CPUdf[(CPUdf['NE Name'] == "DPS_ASBC03_CGP" )]
CPU3_LBU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_LBU1_ARM_VDU1_0" )]
CPU3_LBU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_LBU1_ARM_VDU2_0" )]
CPU3_HRU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_HRU3_ARM_VDU_0" )]
CPU3_HRU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_HRU3_ARM_VDU_1" )]
CPU3_HRU3 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_HRU3_ARM_VDU_2" )]
CPU3_HIU1 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_HIU_ARM_VDU1_0" )]
CPU3_HIU2 = CPUdf[(CPUdf['VM'] == "Virtual machine name=DPS_ASBC03_HIU_ARM_VDU2_0" )]

headerinfo =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo2 =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo3 =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo4 =  "Rate of ABCF Successful Re-registrations (%)"
headerinfo5 =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo6 =  "Number of ABCF Successful Initial Registrations (times)"
headerinfo7 =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo8 =  "Number of ABCF Successful Initial Registrations (times)"
headerinfo9 =  "eSRVCC Success Rate (%)"
headerinfo10 =  "Average Module CPU Usage (%)"
headerinfo11 =  "Rate of ABCF Successful Initial Registrations (%)"
headerinfo12 =  "Number of ABCF Successful Initial Registrations (times)"
headerinfo13 =  "Number of S-CSCF Registered Users (number)" # test field
headerinfo14 =  "Maximum CPU Load (%)"

xdesc = (ASBCdf['NE Name'].value_counts()[targetNE1]) # usually used for Time
xdesc2 = (CPUdf['VM'].value_counts()["Virtual machine name=DPS_ASBC01_LBU1_ARM_VDU1_0"]) # usually used for Time
xdesc3 = (SCSCFkpidf['NE Name'].value_counts()[targetNE4]) # used for Maximu number
xdesc32 = (CSCF_DPS['Period (min)'].value_counts()[5]) # scrap


time1 = DPS_ASBC01["Start Time"]
time2 = DPS_ASBC02["Start Time"]
time3 = DPS_ASBC03["Start Time"]

time12 = CPU_ASBC01["Start Time"]
time22 = CPU_ASBC02["Start Time"]
time32 = CPU_ASBC03["Start Time"]

time13 = CPU1_LBU1["Start Time"]
time23 = CPU1_LBU2["Start Time"]
time33 = CPU1_LBU1["Start Time"]

timeCSCF = CSCF_DPS["Start Time"]

y1 = DPS_ASBC01[headerinfo]
y2 = DPS_ASBC02[headerinfo]
y3 = DPS_ASBC03[headerinfo]

y12 = DPS_ASBC01[headerinfo2]
y22 = DPS_ASBC02[headerinfo2]
y32 = DPS_ASBC03[headerinfo2]

y13 = DPS_ASBC01[headerinfo2]
y23 = DPS_ASBC02[headerinfo2]
y33 = DPS_ASBC03[headerinfo2]

y14 = DPS_ASBC01[headerinfo4]
y24 = DPS_ASBC02[headerinfo4]
y34 = DPS_ASBC03[headerinfo4]

y15 = DPS_ASBC01[headerinfo2]
y25 = DPS_ASBC02[headerinfo2]
y35 = DPS_ASBC03[headerinfo2]

y16 = DPS_ASBC01[headerinfo2]
y26 = DPS_ASBC02[headerinfo2]
y36 = DPS_ASBC03[headerinfo2]

y17= DPS_ASBC01[headerinfo2]
y27= DPS_ASBC02[headerinfo2]
y37 = DPS_ASBC03[headerinfo2]

y18 = DPS_ASBC01[headerinfo2]
y28 = DPS_ASBC02[headerinfo2]
y38 = DPS_ASBC03[headerinfo2]

y19 = DPS_ASBC01[headerinfo9]
y29 = DPS_ASBC02[headerinfo9]
y39 = DPS_ASBC03[headerinfo9]

y110 = CPU_ASBC01[headerinfo10]
y210 = CPU_ASBC02[headerinfo10]
y310 = CPU_ASBC03[headerinfo10]

y111 = DPS_ASBC01[headerinfo11]
y211 = DPS_ASBC02[headerinfo11]
y311 = DPS_ASBC03[headerinfo11]

y112 = DPS_ASBC01[headerinfo11]
y212 = DPS_ASBC02[headerinfo11]
y312 = DPS_ASBC03[headerinfo11]

y113 = CSCF_DPS[headerinfo13]
maxy113 = y113.sort_values(ascending=False).iloc[0]
y213 = DPS_ASBC02[headerinfo11] # does not need
y313 = DPS_ASBC03[headerinfo11] # does not need

y114 = CPU1_LBU1[headerinfo14]
y214 = CPU1_LBU2[headerinfo14]
y314 = CPU1_HRU1[headerinfo14]
y414 = CPU1_HRU2[headerinfo14]
y514 = CPU1_HRU3[headerinfo14]
y614 = CPU1_HIU1[headerinfo14]
y714 = CPU1_HIU2[headerinfo14]

y115 = CPU2_LBU1[headerinfo14]
y215 = CPU2_LBU2[headerinfo14]
y315 = CPU2_HRU1[headerinfo14]
y415 = CPU2_HRU2[headerinfo14]
y515 = CPU2_HRU3[headerinfo14]
y615 = CPU2_HIU1[headerinfo14]
y715 = CPU2_HIU2[headerinfo14]

# headerinfocount = time.count
# print(headerinfocount)

# Rate of Successful Initial Registrations CSCF #

headerinfoPlot = plt.figure(1)
plt.title(headerinfo)
plt.plot(time1,y1,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y2,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y3,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
headerinfoPlot.show()

# Rate of Successful Initial Registrations ASBC # already working need ASBC reg

headerinfoPlot = plt.figure(2)
plt.title(headerinfo)
plt.plot(time1,y1,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y2,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y3,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
headerinfoPlot.show()

# Rate of Successful Re-Registrations CSCF # 

headerinfoPlot2 = plt.figure(3)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot2.show()

# Rate of Successful Re-Registrations ASBC # already working need ASBC reg

headerinfoPlot4 = plt.figure(4)
plt.title(headerinfo4)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
headerinfoPlot4.show()

headerinfoPlot3 = plt.figure(5)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

headerinfoPlot3 = plt.figure(6)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

headerinfoPlot3 = plt.figure(7)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

headerinfoPlot3 = plt.figure(8)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

# eSrvcc already working need ASBC reg

headerinfoPlot9 = plt.figure(9)
plt.title(headerinfo9)
plt.plot(time1,y19,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y29,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y39,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
headerinfoPlot9.show()

headerinfoPlot10 = plt.figure(10)
plt.title(headerinfo10)
plt.plot(time12,y110,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time22,y210,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time32,y310,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
#plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot10.show()

headerinfoPlot3 = plt.figure(11)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

headerinfoPlot3 = plt.figure(12)
plt.title(headerinfo2)
plt.plot(time1,y12,label=targetNE1, linewidth=0.7, marker=".")
plt.plot(time2,y22,label=targetNE2, linewidth=0.7, marker=".")
plt.plot(time3,y32,label=targetNE3, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot3.show()

headerinfoPlot13 = plt.figure(13) #Testing purpose here
plt.title(headerinfo2)
plt.plot(timeCSCF,y113,label=targetNE4, linewidth=0.7, marker=".")
plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Nominal (juta)')
plt.ylim(ymin=0)
plt.grid()
plt.xticks([0,(xdesc3-1)*0.10,(xdesc3-1)*0.20,(xdesc3-1)*0.30,(xdesc3-1)*0.40,(xdesc3-1)*0.50,(xdesc3-1)*0.60,(xdesc3-1)*0.70,(xdesc3-1)*0.80, (xdesc3-1)*0.90,(xdesc3-1)])
plt.yticks([0,(maxy113-1)*0.10,(maxy113-1)*0.20,(maxy113-1)*0.30,(maxy113-1)*0.40,(maxy113-1)*0.50,(maxy113-1)*0.60,(maxy113-1)*0.70,(maxy113-1)*0.80, (maxy113-1)*0.90,(maxy113-1)])

headerinfoPlot13.show()

# CPU util ASBC01

headerinfoPlot14 = plt.figure(14)
plt.title(headerinfo14)
plt.plot(time13,y114,label="DPS_ASBC01_LBU1_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y214,label="DPS_ASBC01_LBU1_ARM_VDU2_0", linewidth=0.7, marker=".")
plt.plot(time23,y314,label="DPS_ASBC01_HRU3_ARM_VDU_0", linewidth=0.7, marker=".")
plt.plot(time23,y414,label="DPS_ASBC01_HRU3_ARM_VDU_1", linewidth=0.7, marker=".")
plt.plot(time23,y514,label="DPS_ASBC01_HRU3_ARM_VDU_2", linewidth=0.7, marker=".")
plt.plot(time23,y614,label="DPS_ASBC01_HIU_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y714,label="DPS_ASBC01_HIU_ARM_VDU2_0", linewidth=0.7, marker=".")

plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0,ymax=100)
plt.grid()
plt.xticks([0,(xdesc2-1)*0.10,(xdesc2-1)*0.20,(xdesc2-1)*0.30,(xdesc2-1)*0.40,(xdesc2-1)*0.50,(xdesc2-1)*0.60,(xdesc2-1)*0.70,(xdesc2-1)*0.80, (xdesc2-1)*0.90,(xdesc2-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot14.show()

# CPU util ASBC02

headerinfoPlot15 = plt.figure(15)
plt.title(headerinfo14)
plt.plot(time13,y115,label="DPS_ASBC02_LBU1_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y215,label="DPS_ASBC02_LBU1_ARM_VDU2_0", linewidth=0.7, marker=".")
plt.plot(time23,y315,label="DPS_ASBC02_HRU3_ARM_VDU_0", linewidth=0.7, marker=".")
plt.plot(time23,y415,label="DPS_ASBC02_HRU3_ARM_VDU_1", linewidth=0.7, marker=".")
plt.plot(time23,y515,label="DPS_ASBC02_HRU3_ARM_VDU_2", linewidth=0.7, marker=".")
plt.plot(time23,y615,label="DPS_ASBC02_HIU_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y715,label="DPS_ASBC02_HIU_ARM_VDU2_0", linewidth=0.7, marker=".")

plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0,ymax=100)
plt.grid()
plt.xticks([0,(xdesc2-1)*0.10,(xdesc2-1)*0.20,(xdesc2-1)*0.30,(xdesc2-1)*0.40,(xdesc2-1)*0.50,(xdesc2-1)*0.60,(xdesc2-1)*0.70,(xdesc2-1)*0.80, (xdesc2-1)*0.90,(xdesc2-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot15.show()

# CPU util ASBC03

headerinfoPlot15 = plt.figure(16)
plt.title(headerinfo14)
plt.plot(time13,y115,label="DPS_ASBC03_LBU1_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y215,label="DPS_ASBC03_LBU1_ARM_VDU2_0", linewidth=0.7, marker=".")
plt.plot(time23,y315,label="DPS_ASBC03_HRU3_ARM_VDU_0", linewidth=0.7, marker=".")
plt.plot(time23,y415,label="DPS_ASBC03_HRU3_ARM_VDU_1", linewidth=0.7, marker=".")
plt.plot(time23,y515,label="DPS_ASBC03_HRU3_ARM_VDU_2", linewidth=0.7, marker=".")
plt.plot(time23,y615,label="DPS_ASBC03_HIU_ARM_VDU1_0", linewidth=0.7, marker=".")
plt.plot(time23,y715,label="DPS_ASBC03_HIU_ARM_VDU2_0", linewidth=0.7, marker=".")

plt.legend(loc="best")
plt.xlabel('Dates')
plt.ylabel('Percentages (%)')
plt.ylim(ymin=0,ymax=100)
plt.grid()
plt.xticks([0,(xdesc2-1)*0.10,(xdesc2-1)*0.20,(xdesc2-1)*0.30,(xdesc2-1)*0.40,(xdesc2-1)*0.50,(xdesc2-1)*0.60,(xdesc2-1)*0.70,(xdesc2-1)*0.80, (xdesc2-1)*0.90,(xdesc2-1)])
#plt.yticks([0,(xdesc-1)*0.10,(xdesc-1)*0.20,(xdesc-1)*0.30,(xdesc-1)*0.40,(xdesc-1)*0.50,(xdesc-1)*0.60,(xdesc-1)*0.70,(xdesc-1)*0.80, (xdesc-1)*0.90,(xdesc-1)])
headerinfoPlot15.show()


input()







