import  matplotlib.pyplot as plt
import numpy as np

data =  np.loadtxt('benchmarks.dat')

plt.title('AA simulation on Bridges2 GPU nodes')
plt.rc('font' , size =12)
plt.ylabel('Performance (ns/day)')
plt.xlabel('GPUs')
#plt.xscale("log")
#plt.yscale("log")

x=data[:,0]
ymax=np.amax(data[:,1:],axis=1)

coef = np.polyfit(x[:2],ymax[:2],1)
fn =  np.poly1d(coef)



plt.xticks([1,2,4,8])
plt.plot(x, ymax,marker='o',  linewidth=2, label='best')

x0=np.linspace(1,4,4)
plt.plot(x0,fn(x0), '--k')

plt.savefig('AA-LLC-gpus.png')
plt.show()
plt.close()


exit()



