import pandas as pd
import numpy as np 

dates = ["1/16/23","1/17/23","1/18/23","1/19/23","1/21/23","1/22/23","1/23/23","1/24/23","1/25/23","1/26/23","1/27/23",
        "1/28/23"]

hours = [2.52,2.25,1.63,2.35,3.13,2.09,2.06,1.58,2.00,2.44,2.56,2.85]
        

df_logs = pd.DataFrame(hours,dates)
#print(df_logs)

total = df_logs[0].sum()
average = np.average(df_logs[0])
count = np.count_nonzero(dates)

print(f'total_hours: {round(total,2)}')
print(f'avg_day: {round(average,2)}')
print(f'total_days: {count}')
