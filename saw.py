import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

#Plot thingys
fig=plt.figure(figsize=(10,3))
ax=fig.add_subplot(111)

name="Accent"
cmap= get_cmap('tab10')
colors=cmap.colors
ax.set_prop_cycle(color=colors)

dx= 0.001
L = np.pi #periodo
x = L * np.arange(-1+dx,1+dx,dx)
p= len(x)
phalf= int(np.floor(p/2))

f=np.zeros_like(x)
f[:phalf] = (6)*np.arange(1,phalf+1)
f[phalf:2*phalf] = (6)*np.arange(1,phalf+1)


ax.plot(x,f, color="#FA0000",  LineWidth= "1")

A0= np.sum(f*np.ones_like(x)) * dx
fFS = A0/2

i=100#número de armónicos
A = np.zeros (i)
B = np.zeros (i)
for n in range (i):
    A[n] =np.sum(f * np.cos(np.pi*(n+1)*x/L)) * dx
    B[n] =np.sum(f * np.sin(np.pi*(n+1)*x/L)) * dx
    fFS = fFS + A[n]*np.cos((n+1)*np.pi*x/L) +  B[n]*np.sin((n+1)*np.pi*x/L)
    ax.plot(x,fFS, LineWidth= "1")
ax.plot(x,fFS, LineWidth= "3")
    
ax.plot(x,f, color="#FA0000",  LineWidth= "2.5" , label="Function")
#More plot thingys
ax.set_xlabel("Coordenada de X",fontsize=14)
ax.set_ylabel("Amplitud",fontsize=14)
ax.legend(loc="upper left",fontsize=14)

