import pandas as pd
import numpy as np 

dates = ["01/16/23","01/17/23","01/18/23",#1
         "01/19/23","01/21/23","01/22/23",#2
         "01/23/23","01/24/23","01/25/23",#3
         "01/26/23","01/27/23","01/28/23",#4
         "01/29/23","01/30/23","01/31/23",#5
         "02/01/23","02/02/23","02/04/23",#6
         "02/05/23","02/06/23","02/07/23",#7
         "02/08/23","02/09/23","02/10/23",#8
         "02/11/23","02/12/23","02/13/23",#9
         "02/14/23","02/15/22","02/16/23",#10
         "02/17/23","02/18/23","02/20/23",#11
        "02/21/23","02/23/23","02/25/23",#12
        "02/26/23","02/27/23","02/28/23",#13
        "03/03/23","03/04/23","03/05/23",#14
        "03/06/23","03/07/23","03/08/23",#15
        "03/09/23","03/10/23","03/11/23",#16
        "03/13/23","03/14/23","03/16/23",#17
        "03/17/23","03/20/23","03/21/23",#18
        "03/22/23","03/23/23","03/24/23",#19
        "03/25/23","03/26/23","03/27/23",#20
        "03/28/23","03/29/23","03/30/23",#21
        "03/31/23","04/05/23","04/06/23",#22
        "04/08/23","04/10/23","04/11/23",#23
        "04/12/23","04/13/23","04/14/23",#24
        "04/15/23","04/16/23","04/17/23",#25
        "04/18/23","04/19/23","04/20/23",#26
        "04/21/23","04/22/23","04/23/23",#27
        "04/24/23","04/25/23","04/26/23",#28
        "04/27/23","04/28/23","04/29/23",#29
        "05/01/23","05/02/23","05/03/23",
        "05/04/23","05/05/23","05/06/23",
        "05/07/23","05/08/23","05/09/23",
        "05/10/23","05/11/23"]#30

hours = [2.52,2.25,1.63,#1
         2.35,3.13,2.09,#2
         2.06,1.58,2.00,#3
         2.44,2.56,2.85,#4
         2.02,2.36,2.99,#5
         2.40,1.66,4.50,#6
         1.89,2.63,1.33,#7
         3.50,3.47,1.92,#8
         3.99,3.74,1.86,#9
         2.57,1.15,1.64,#10
         2.59,2.66,2.71,#11
         2.23,2.75,1.60,#12
         1.00,1.00,2.16,#13
         2.12,2.27,2.15,#14
         2.75,2.85,2.04,#15
         3.57,2.14,1.44,#16
         2.76,2.33,1.00,#17
         1.25,2.85,1.66,#18
         1.00,1.55,1.62,#19
         1.68,0.36,2.00,#20
         3.00,1.00,4.39,#21
         3.07,1.24,1.00,#22
         3.83,2.64,2.18,#23
         2.69,2.31,1.00,#24
         2.28,1.00,1.82,#25
         1.20,2.08,1.23,#26
         1.0,2.00,2.00,#27
         1.55,1.71,2.00,#28
         2.00,2.00,2.00,#29
         1.07,2.04,1.23,
         2.73,1.40,1.80,
         2.82,3.77,2.68,
         1.00,4.00]#30
         
        

df_logs = pd.DataFrame(hours,dates)
#print(df_logs)

total = df_logs[0].sum()
average = np.average(df_logs[0])
count = np.count_nonzero(dates)

print(f'total_hours: {round(total,2)}')
print(f'avg_day: {round(average,2)}')
print(f'total_days: {count}')
