import  matplotlib.pyplot as plt
import numpy as np


data =  np.loadtxt('benchmarks.dat')
plt.title('AA simulation on Bridges2 RM nodes')
plt.rc('font' , size =12)
plt.ylabel('Performance (ns/day)')
plt.xlabel('Cores')
#plt.xscale("log")
#plt.yscale("log")

x=data[:,0]
y=data[:,1]

coef = np.polyfit(x[:6],y[:6],1)
fn =  np.poly1d(coef)

plt.plot(x,y, marker='o', linewidth=2)

x0=np.linspace(0,128,129)
plt.plot(x0,fn(x0), '--k')

plt.savefig('AA-LLC-cores.png')

plt.show()
exit()



