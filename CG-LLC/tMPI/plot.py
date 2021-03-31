import  matplotlib.pyplot as plt
import numpy as np


data =  np.loadtxt('benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('Num. processors')
plt.xscale("log")
plt.yscale("log")

plt.plot(data[:,0], data[:,1], marker='o', linewidth=2)

plt.savefig('test_NP.png')

plt.show()
exit()



