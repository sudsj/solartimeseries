import xml.etree.ElementTree as ET
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns                            # more plots
from dateutil.relativedelta import relativedelta # working with dates with style
from scipy.optimize import minimize 
# The data has been extracted from a website run by Energinet at the following link where time series data is publicly available:
# /https://www.energidataservice.dk/dataset/electricitybalance

tree = ET.parse('small.xml')
root = tree.getroot()
# print(root.tag)
# iters = 0
# for element in root.iter():
#     print(element.tag)
#     iters += 1
#     if iters > 10:
#         break
abstimes = []
dktimes = [] 
strtimes = []   
solar = []    
abstime = 0
for row in root.iter('row'):
    # print(row.attrib)    
    # print(row.text)
    dktime = 0
    for element in row.iter():
        # print(element.tag)
        if element.tag == 'HourDK':
            # print(element.text)
            strdktime = element.text
            dktime = int(strdktime[11:13])
            if dktime > 20 or dktime < 6:
                break
            else:
                strtimes.append(strdktime)
                dktimes.append(dktime)
                abstimes.append(abstime)
                abstime += 1
                # print(dktimes[-1])
        elif element.tag == 'SolarPowerProd':
            # print(element.text)
            spower = float(element.text)
            solar.append(spower)

sdata = pd.DataFrame(list(zip(solar,dktimes)),index=abstimes)
print(sdata)
plt.figure(figsize=(15, 7))
plt.xticks(abstimes, dktimes)
ax = plt.gca()
n = 5
ax.set_xticks(ax.get_xticks()[::30])
plt.plot(sdata)
plt.title('Ads watched (hourly data)')
plt.grid(True)
plt.show()

# sdata = pd.DataFrame(solar,index=pd.to_datetime(strtimes))
# plt.figure(figsize=(15, 7))

# plt.plot(sdata)
# plt.title('Ads watched (hourly data)')
# plt.grid(True)
# plt.show()