"""
Created on Sat Nov 26 07:47:22 2022

@author: Angel
"""


import matplotlib.pyplot as plt
import spm1d

import os
import scipy.io

#(0) Load data:
    
# load Matlab data:
dir0         = os.path.dirname("__file__")
fname        = os.path.join(dir0, 'data', 'Liso')
Liso            = scipy.io.loadmat(fname)['Liso']   #YA 5 curves, 100 nodes    
fname        = os.path.join(dir0, 'data', 'Text01_10000')  
Text01            = scipy.io.loadmat(fname)['Text01'] #YB 5 curves, 100 nodes

# Se declaran los nombres de las variable    



#(1) Conduct t test:
alpha      = 0.05
t          = spm1d.stats.ttest2(Liso, Text01, equal_var=False)
ti         = t.inference(alpha, two_tailed=True, interp=False)
print( ti )



#(2) Plot:
plt.close('all')
### plot mean and SD:
    



fig,AX = plt.subplots( 1, 2, figsize=(8, 3.5) )
ax     = AX[0]
plt.sca(ax)
spm1d.plot.plot_mean_sd(Liso)
spm1d.plot.plot_mean_sd(Text01, linecolor='r', facecolor='r')
ax.axhline(y=0, color='k', linestyle=':')
ax.set_xlabel('Walking cycle (%)')
ax.set_ylabel('COF  ($\mu$)')
### plot SPM results:
ax     = AX[1]
plt.sca(ax)
ti.plot()
ti.plot_threshold_label(fontsize=8)
ti.plot_p_values(size=10, offset_all_clusters=(0,0.9))
ax.set_xlabel('Walking cycle (%)')
plt.tight_layout()
plt.show()
