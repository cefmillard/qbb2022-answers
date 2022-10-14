import sys
import numpy as np
import matplotlib.pyplot as plt
from bdg_loader import load_data

f1, f2, f3, f4 = sys.argv[1:5]

data1 = load_data(f1)
data2 = load_data(f2)
data3 = load_data(f3)
data4 = load_data(f4)

fig,ax=plt.subplots(nrows=4)
plt.tight_layout()
ax[0].fill_between(data1['X'],data1['Y'],y2=0)
ax[0].set_title("D0_H3K27ac_treat")
ax[1].fill_between(data2['X'],data2['Y'],y2=0)
ax[1].set_title("D2_H3K27ac_treat")
ax[2].fill_between(data3['X'],data3['Y'],y2=0)
ax[2].set_title("D2_Klf4_treat")
ax[3].fill_between(data4['X'],data4['Y'],y2=0)
ax[3].set_title("Sox2_treat")
plt.savefig("Sox2_track.pdf")