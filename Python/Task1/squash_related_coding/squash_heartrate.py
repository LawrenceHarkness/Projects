import pandas as pd
import xlsxwriter


# import exel file

df =pd.read_excel('HR Data.xlsx',index_col=0)




df['max_hr'] = 220 - df['age']
max_hr = df['max_hr'][1]
df.loc[(df.hr <= max_hr) & (df.hr > (max_hr*0.9)), 'HRZone'] = 'Maximum'


df.loc[(df.hr <= (max_hr*0.9)) & (df.hr > (max_hr*0.8)), 'HRZone'] = 'Hard'

df.loc[(df.hr <= (max_hr*0.8)) & (df.hr > (max_hr*0.7)), 'HRZone'] = 'moderate'

df.loc[(df.hr <= (max_hr*0.7)) & (df.hr > (max_hr*0.6)), 'HRZone'] = 'easy'

df.loc[(df.hr <= (max_hr*0.6)) & (df.hr > (max_hr*0.5)), 'HRZone'] = 'very_easy'

df.loc[(df.hr <= (max_hr*0.5) ),  'HRZone'] = 'walk_in_the_park'


writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

writer.save()




print(df.describe())
print('a')

