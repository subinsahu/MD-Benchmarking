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
ymax=np.amax(data[:,1:],axis=1)
plt.xticks([1,2,4,8])
plt.plot(x, y1, marker='o', linewidth=0, label='1 MPI/GPU')
plt.plot(x, y2, marker='v', linewidth=0, label='2 MPI/GPU')
plt.plot(x, y4, marker='s', linewidth=0, label='4 MPI/GPU')
plt.plot(x, y5, marker='*', linewidth=0, label='5 MPI/GPU')
plt.plot(x, ymax, linewidth=2, label='best')

plt.legend()
plt.savefig('test_GPU.png')
plt.show()
plt.close()

exit()



