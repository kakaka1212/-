import pandas as pd
import matplotlib.pyplot as plt

#CSV open hensu in
CSV_FILE_NAME = '/home/pi/Desktop/io31_kadai06_22/temp-hmdt.csv'
IMG_FILE_NAME = '/home/pi/Desktop/io31_kadai06_22/temp-hmdt.png'

data = pd.read_csv(CSV_FILE_NAME,names=['date_time','temp','hmdt']
                   ,index_col='date_time',parse_dates=[0])

data.plot()#graph output
plt.savefig(IMG_FILE_NAME)#graph img save

print("Content-Type; text/html; charset=utf-8")
print("")
print """
<!DOTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Graph Sample</title>
</head>
<body>
<img src="../data.png">
</body>
</html>
"""