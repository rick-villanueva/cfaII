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
        "05/10/23","05/11/23","05/12/23",
        "05/13/23","05/14/23","05/15/23",
        "05/16/23","05/17/23","05/18/23",
        "05/19/23","05/21/23","05/22/23", #DEFERRAL OF EXAM TO NOVEMBER 21,2023
        "05/29/23","05/30/23","06/01/23",
        "06/05/23","06/06/23","06/08/23",
        "07/03/23","07/05/23","07/06/23",
        "07/10/23","07/11/23","07/12/23",
        "07/14/23","07/15/23","07/16/23",
        "07/17/23","07/18/22","07/19/23",
        "07/20/23","07/21/23","07/22/23",
        "07/23/23","07/24/23","07/25/23",
        "07/26/23","07/27/23","07/28/23",
        "07/29/23","07/30/23","07/31/23",
        "08/01/23","08/02/23","08/03/23",
        "08/04/23","08/05/23","08/06/23",
        "08/07/23","08/08/23","08/09/23",
        "08/10/23","08/11/23","08/14/23",
        "08/15/23","08/16/23","08/17/23",
        "08/20/23","08/21/23","08/22/23",
        "08/23/23","08/25/23","08/26/23",
        "08/27/28","08/28/23","08/29/23",
        "08/30/23","08/31/23","09/01/23",
        "09/02/23","09/04/23","09/05/23",
        "09/06/23","09/07/23","09/08/23",
        "09/10/23","09/11/23","09/12/23",
        "09/14/23","09/15/23","09/16/23",
        "09/17/23","09/18/23","09/19/23",
        "09/20/23","09/21/23","09/22/23",
        "09/24/23","09/25/23","09/26/23",
        "09/27/23","09/28/23","09/29/23",
        "09/30/23","10/1/23","10/2/23",
        "10/03/23","10/04/23","10/05/23",
        "10/06/23","10/08/23","10/09/23",
        "10/10/23","10/11/23","10/12/23",
        "10/13/23","10/15/23","10/16/23",
        "10/23/23","10/24/23","10/25/23", #Leave starts: goal is 7 hrs 
        "10/26/23","10/27/23","10/28/23",
        "10/29/23","10/30/23","10/31/23",
        "11/01/23","11/02/23","11/03/23",
        "11/04/23","11/05/23","11/06/23",
        "11/07/23","11/08/23","11/09/23",
        "11/10/23","11/13/23","11/14/23",
        "11/15/23","11/16/23","11/17/23",
        "11/18/23","11/19/23","11/20/23"] 

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
         1.00,4.00,2.52,
         2.84,2.23,3.84,
         2.67,2.84,1.00,
         2.50,3.49,2.18,
         3.28,2.75,3.86,
         2.88,1.00,1.00,
         1.53,2.84,1.53,
         1.00,2.22,1.16,
         1.00,1.02,1.12,
         2.35,1.99,2.33,
         2.78,2.72,3.00,
         3.00,1.00,1.00,
         1.00,1.00,1.00,
         1.00,1.48,2.34,
         1.32,3.95,3.02,
         1.68,3.10,1.53,
         3.13,2.33,2.54,
         2.00,2.65,2.37,
         2.26,1.81,3.36,
         1.6,2.61,2.79,
         1.84,2.40,1.50,
         2.15,1.71,2.03,
         1.53,2.61,1.50,
         4.30,2.32,2.47,
         2.38,2.33,1.50,
         3.03,3.00,2.00,
         2.40,2.04,2.40,
         1.40,3.73,3.32,
         2.45,1.54,1.60,
         2.44,3.49,2.81,
         2.73,2.89,2.49,
         2.03,1.99,2.68,
         3.06,2.84,2.63,
         2.35,1.72,2.11,
         1.91,2.66,3.38,
         2.00,2.00,1.00,
         4.74,3.59,4.65,
         3.77,4.54,1.87,
         3.37,4.30,2.94,
         5.24,4.07,3.65,
         2.00,2.00,5.51,
         4.15,4.00,2.77,
         1.20,2.63,2.50,
         2.00,2.00,3.35,
         2.00,2.00,4.00]#30
         
        

df_logs = pd.DataFrame(hours,dates)
#print(df_logs)

total = df_logs[0].sum()
average = np.average(df_logs[0])
count = np.count_nonzero(dates)

print(f'total_hours: {round(total,2)}')
print(f'avg_day: {round(average,2)}')
print(f'total_days: {count}')
