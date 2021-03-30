import  matplotlib.pyplot as plt
import numpy as np


data =  np.loadtxt('benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('Nodes')
#plt.xscale("log")
#plt.yscale("log")

x=data[:,0]
y=data[:,2]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.plot(x, y, marker='o', linewidth=2)

plt.savefig('test_Nnodes.png')

plt.show()
exit()



