import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as ticker
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches

data1=np.genfromtxt("Eb_redshift.txt")
data2=np.genfromtxt("redshift_tau.txt")
z1=data1[:,3]
L1=data1[:,4]


z2=data2[:,1]
L2=data2[:,2]


fig,ax = plt.subplots(figsize=(8,6))

# figure 1

ax.errorbar(z1,L1,fmt='o',color='grey',elinewidth=0.3,alpha=0.3,markersize=4,capsize=1,label='samples from E$_{b}-z$ relationship')
ax.errorbar(z2,L2,fmt='r*',elinewidth=1,markersize=7,capsize=1,label='samples from $\\tau-z$ relationship')

ax.set_ylabel("$L_{\gamma}$ (erg/s)")  
ax.set_xlabel("Redshift(z)") 
ax.legend(loc=4,fontsize='small')

fill_color='pink'
dark_color=mcolors.to_rgba(fill_color,alpha=1.0)
dark_color=(dark_color[0]*0.5,dark_color[1]*0.5,dark_color[2]*0.5,dark_color[3]*0.5)

ax.fill_between([0.3,1.3],3e+46,3e+47,edgecolor=dark_color,facecolor=fill_color,alpha=0.5,linewidth=1)
ax.text(0.1,5e+47,"$\delta \propto (1+z)^{1.7\pm 1.13}$",color="r", fontsize=12)


#ax.text(2.2, 5e+44, "2", color="black", fontsize=8)
#ax.text(2.6, 2.5e+45, "1", color="black", fontsize=8)
#ax.text(2.75, 1.6e+45, "3", color="black", fontsize=8)

ax.set_yscale('log')
plt.axis('tight')

#plt.ylim()
#plt.grid(True, linestyle="-.",color="grey",alpha=0.5)
#plt.axis('tight')
# show or save
plt.savefig("L-z.pdf")
