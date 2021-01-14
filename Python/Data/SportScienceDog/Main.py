import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

df = pd.read_csv("SportScienceDog/20201008034217-52040-data.txt",sep='\t')
print(df)

#https://www.movable-type.co.uk/scripts/latlong.html

R = 6.3781 * math.pow(10, 6)
y1 = df['longitude']
x1 = df['latitude']
y2 = df['longitude'].shift(-1)
x2 = df['latitude'].shift(-1)

theta1 = x1 * math.pi/180
theta2 = x2 * math.pi/180
deltaTheta = (x2 - x1) * math.pi/180
deltaLander = (x2 - x1) * math.pi/180
a = np.sin(deltaTheta/2) * np.sin(deltaTheta/2) + np.cos(theta1) * np.cos(theta2) * np.sin(deltaLander/2) * np.sin(deltaLander/2)

c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
d = R * c

df['distance'] = d
df['distance'] = df['distance'].shift(1)
df['k/h'] = df['distance'] * 3.6

df['distance'] = df['distance'].replace(np.nan,0)
cumDistance = 0
df['cumDistance'] = 0.00

for i,row in df.iterrows():
    cumDistance += row['distance']
    df.at[i,'cumDistance'] = cumDistance
''' 
x = df['time']
y = df['distance']

plt.xlabel('time')
plt.ylabel('distance')
plt.plot(x,y)

x = df['time']
y = df['cumDistance']

plt.xlabel('time')
plt.ylabel('cumDistance')
plt.plot(x,y)

plt.show()
'''


t = df['time']
data1 = df['distance']
data2 = df['cumDistance']

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Distance', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('cumDistance', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

print(df)