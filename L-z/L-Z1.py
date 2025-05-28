import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as ticker
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches

data1=np.genfromtxt("Eb_redshift_no1.txt")
data2=np.genfromtxt("Eb_redshift_y.txt")
z1=data1[:,3]
L1=data1[:,4]
#errL1=data1[:,5]

z2=data2[:,3]
L2=data2[:,4]
#errL2=data2[:,5]

fig,ax = plt.subplots(figsize=(8,6))

# figure 1

ax.errorbar(z1,L1,fmt='bo',elinewidth=1,markersize=5,capsize=1)
ax.errorbar(z2,L2,fmt='bo',elinewidth=1,markersize=5,capsize=1)
#plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2g'))

#plt.axhline(y=1e+47,c='black',ls='--',lw=1)
ax.set_ylabel("$L_{\gamma}$ (erg/s)")  
ax.set_xlabel("Redshift(z)")     
#plt.text(2, 4e+46, "$\delta \propto (1+z)^{2\pm0.36}$", color="b", fontsize=10)
#plt.text(0.35, 7e+47, "$\delta \propto (1+z)^{0.67\pm0.24}$", color="r", fontsize=10)

ax.text(1.3, 5e+44, "2: $\delta \propto (1+z)^{1.29^{+0.26}_{-0.27}}$", color="gray", fontsize=12)
ax.text(1.3, 1e+45, "1: $\delta \propto (1+z)^{2.93^{+0.96}_{-0.97}}$", color="gray", fontsize=12)
ax.text(1.3, 2.5e+44, "3: $\delta \propto (1+z)^{1.8^{+0.71}_{-0.70}}$", color="gray", fontsize=12)
#ax.text(0.7, 1.8e+47, "1", color="r", fontsize=7)


fill_color='pink'
dark_color=mcolors.to_rgba(fill_color,alpha=1.0)
dark_color=(dark_color[0]*0.5,dark_color[1]*0.5,dark_color[2]*0.5,dark_color[3]*0.5)

ax.fill_between([0.4,1.5],3e+46,3e+47,edgecolor=dark_color,facecolor=fill_color,alpha=0.5,linewidth=1)
ax.fill_between([1.5,2.5],1e+47,1e+48,edgecolor=dark_color,facecolor=fill_color,alpha=0.5,linewidth=1)
ax.fill_between([0.4,1.5],1e+46,3e+46,edgecolor=dark_color,facecolor=fill_color,alpha=0.5,linewidth=1)

regions=[
(0.4,3e+46,1.1,(3e+47-3e+46)),
(1.5,1e+47,1.0,(1e+48-1e+47)),
(0.4,1e+46,1.1,2e+46)
]

ax_inset = fig.add_axes([0.65,0.2,0.2,0.2])
scale_factor=0.2

for (x,y,width,height) in regions:
    ax_inset.add_patch(patches.Rectangle((x*scale_factor,y*scale_factor),width*scale_factor,height*scale_factor,linewidth=1,fill=False))

ax_inset.set_xlim(0,8*scale_factor)
ax_inset.set_ylim(0,6*scale_factor)
ax_inset.set_yscale('log')
ax_inset.set_axis_off()
ax.text(2.34, 2.7e+44, "1", color="black", fontsize=8)
ax.text(2.34, 0.8e+45, "2", color="black", fontsize=8)
ax.text(2.75, 1.6e+45, "3", color="black", fontsize=8)

ax.set_yscale('log')
plt.axis('tight')
#plt.ylim()
#plt.grid(True, linestyle="-.",color="grey")
#plt.axis('tight')
# show or save
plt.savefig("L-z1.pdf")



