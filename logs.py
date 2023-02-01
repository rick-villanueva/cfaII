import pandas as pd
import numpy as np 

dates = ["01/16/23","01/17/23","01/18/23","01/19/23","01/21/23","01/22/23","01/23/23","01/24/23","01/25/23","01/26/23","01/27/23",
        "01/28/23","01/29/23","01/30/23","01/31/23","02/01/23"]

hours = [2.52,2.25,1.63,2.35,3.13,2.09,2.06,1.58,2.00,2.44,2.56,2.85,2.02,2.36,2.99,2.40]
        

df_logs = pd.DataFrame(hours,dates)
#print(df_logs)

total = df_logs[0].sum()
average = np.average(df_logs[0])
count = np.count_nonzero(dates)

print(f'total_hours: {round(total,2)}')
print(f'avg_day: {round(average,2)}')
print(f'total_days: {count}')
