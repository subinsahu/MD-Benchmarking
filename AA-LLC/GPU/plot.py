import  matplotlib.pyplot as plt
import numpy as np


data =  np.loadtxt('benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('GPUs')
#plt.xscale("log")
#plt.yscale("log")

x=data[:,0]
y1=data[:,1]
y2=data[:,2]
y4=data[:,3]
y5=data[:,4]
plt.xticks([1,2,4,8])
plt.plot(x, y1, marker='o', linewidth=2, label='1 MPI/GPU')
plt.plot(x, y2, marker='v', linewidth=2, label='2 MPI/GPU')
plt.plot(x, y4, marker='*', linewidth=2, label='4 MPI/GPU')
plt.plot(x, y5, marker='s', linewidth=2, label='5 MPI/GPU')


plt.savefig('test_GPU.png')
plt.legend()

plt.show()
exit()



