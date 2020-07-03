import pandas as pd
import time




while True:

    df_action = pd.read_csv('SaturdayShowdownMockData.csv', header=0)

    df_action['score'] = df_action['kills'] + df_action['bedkill']*2 + df_action['wins']*8

    df_action.to_csv('saturdayshowdownresults.csv')
    print('update')
    time.sleep(0.1)

print('hello')