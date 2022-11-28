import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import*
#-------axis------
x1, x2 =0, 150
y1, y2 = 150,0
plt.axis([x1, x2, y1, y2])
plt.xticks(range(x1, x2, 10))
plt.yticks(range(y1, y2,-10))
plt.grid(True, alpha =.1)
axes = plt.gca()
axes.set_aspect(1)
#-----deaw pologn----
pn = np.array([[20,45],[70,10],[100,30],
               [100,10],[110,10],[110,40],[120,45],[120,140],[20,140]])
poly = Polygon(pn, True, facecolor='c', edgecolor ='c')
axes.add_patch(poly)

#-----draw rectangle-----
for i in range(2):
    tr = Rectangle((30+50*i, 50), 30,20,facecolor='orange', edgecolor ='orange')
    axes.add_patch(tr)
#-----draw rectangle in door
pn = np.array([[50,140],[50,100],[90,100],[90,140]])
tr = Polygon(pn, facecolor='m', edgecolor ='m')
axes.add_patch(tr)    
#------draw wedge---
wdg = Wedge((70+.5,100),20,180,0,facecolor='m', edgecolor ='m')
axes.add_patch(wdg)
#-----draw circle----
cr = Circle((85,115),2,facecolor='y', edgecolor ='y')
axes.add_patch(cr)
plt.show()