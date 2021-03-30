import  matplotlib.pyplot as plt
import numpy as np


data =  np.loadtxt('benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('Num. openMP')
plt.xscale("log")
plt.yscale("log")

plt.plot(data[:,1], data[:,2], marker='o', linewidth=2)

plt.savefig('test_openMP.png')

plt.show()
exit()



