
import os
import numpy as np
import matplotlib.pyplot as plt

t,a,b,m1,m2 = np.loadtxt('file.txt', delimiter=' ' , unpack=True)

plt.figure(figsize=(15,5))
plt.xlabel('x label (unit)')
plt.ylabel('y label (unit)')

plt.plot(t,m1,'r-', linewidth=3)
# plt.plot(t,m2,'ko',markersize=2)

# plt.legend(['Instantaneous', 'Average'], loc='upper left')
plt.legend(['Average'], loc='upper left')

# plt.show()
plt.savefig("toto.png")
plt.close()

#plt.title("Simple Plot")
