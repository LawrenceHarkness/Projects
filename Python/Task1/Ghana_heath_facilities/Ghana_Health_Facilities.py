import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# Reading The data
df_facilities = pd.read_csv('health-facilities-gh.csv', header=0)
df_tiers = pd.read_csv('health-facility-tiers.csv', header=0)
# renaming the data to be the same
df_tiers = df_tiers.rename(columns = {'Facility':'FacilityName'})
# MAKING EVERYTHING UPPERCASE
df_facilities['FacilityName'] = df_facilities['FacilityName'].str.upper()
#merging the facilities and the tiers
df = pd.merge(df_facilities,df_tiers,how='outer', on=['FacilityName','Region'])

# create a new collum
df['description'] = ''

#tier three descripton
df.loc[df['Type'] == 'Training Institution', 'Tier'] = 1
df.loc[df['Type'] == 'Maternity Home' , 'Tier'] = 3
df.loc[df['Tier'] == 3 , 'description'] = 'Small clinics and maternity homes - <1,000 Patients/month '
df['Tier'].fillna(0, inplace=True)
df.loc[df['Tier'] == 2 , 'description'] = 'District hospitals and Large volume private hospitals - 3,000 Patients/month '
df.loc[df['Tier'] == 1 , 'description'] = 'Teaching hospitals and Regional hospitals - 5,000 Patients/month Tier'
# Create color map
categories = np.unique(df['Tier'])
colors = np.linspace(0, 1, len(categories))
colordict = dict(zip(categories, colors))
df['Color'] = df['Tier'].apply(lambda x: colordict[x])
# plotting area
df.plot(kind="scatter", x="Longitude", y="Latitude", alpha=0.4)
plt.show()

ghana_img=mpimg.imread('map_ghana.png')
ax = df.plot(kind="scatter", x="Longitude", y="Latitude", c=df.Color, alpha=0.9)
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)

plt.imshow(ghana_img, extent=[-3.2359, 1.11281, 4.84905, 11.0631], alpha=0.5)# [x_min, x_max,y_min,y_max]
plt.show()

print('hi')