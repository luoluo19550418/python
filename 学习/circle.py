import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mptaches

xy1=np.array([100,100])
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z = np.sqrt(xs**2 + ys**2)

#fig = plt.figure(figsize=(5, 8))
fig = plt.figure()
ax=fig.add_subplot(111)
ax.imshow(z)
circle=mptaches.Circle(xy1,50, color='r', fill=False)
ax.add_patch(circle)
#ax.axis('equal')
plt.show()

'''import matplotlib.pyplot as plt
plt.figure(figsize=(4, 4))
plt.axis('equal')
ax = plt.gca()
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
disk1 = plt.Circle((0, 0), 1, color='r', fill=False)
ax.add_artist(disk1)
plt.show()'''


'''
plt.figure()
plt.imshow(z)
#圆形,指定坐标和半径
#circle=mptaches.Circle(xy1,5)
#plt.gca().add_patch(circle)

#plt.axis('equal')
plt.show()
'''