import csv
import numpy as np
import matplotlib.pylab as plt
import FunctionLists

csv_file = open("./test.csv", "r", encoding="ms932")
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
print(header)

for row in f:
    print(row)

t0 = 0 #むだ時間
Func =FunctionLists.FunctionLists()
x = np.arange(-5.0, 5.0, 0.1)
#y = Func.step_function(x,t0)
y = Func.responce_fit(x, t0, 1, 2)
plt.plot(x,y)
#plt.ylim(-0.1, 1.1)
plt.show()

# もろもろの処理の後、close
csv_file.close()
