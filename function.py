import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

#Plot thingys
fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(111)

name="Accent"
cmap= get_cmap('tab10')
colors=cmap.colors
ax.set_prop_cycle(color=colors)

dx= 0.001
L = np.pi #periodo
x = L * np.arange(-1+dx,1+dx,dx)
p= len(x)
psext= int(np.floor(p/6))

f=np.zeros_like(x)
f[psext:2*psext] = (6/2000)*np.arange(1,psext+1)
f[2*psext:4*psext] = np.ones(2*psext) - (6/2000)*np.arange(0,2*psext)
f[4*psext:5*psext] = np.negative(np.ones(psext))+(6/2000)*np.arange(1,psext+1)

ax.plot(x,f, color="#FA0000",  LineWidth= "1", label="Function")

A0= np.sum(f*np.ones_like(x)) * dx
fFS = A0/2

i=25#número de armónicos
A = np.zeros (i)
B = np.zeros (i)
for n in range (i):
    A[n] =np.sum(f * np.cos(np.pi*(n+1)*x/L)) * dx
    B[n] =np.sum(f * np.sin(np.pi*(n+1)*x/L)) * dx
    fFS = fFS + A[n]*np.cos((n+1)*np.pi*x/L) +  B[n]*np.sin((n+1)*np.pi*x/L)
    ax.plot(x,fFS, LineWidth= "2")
    
#More plot thingys
ax.set_xlabel("Coordenada de X",fontsize=14)
ax.set_ylabel("Amplitud",fontsize=14)
ax.legend(loc="upper left",fontsize=14)
