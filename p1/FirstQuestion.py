from matplotlib import pyplot as plt
import numpy as np

# with 0.01 time steps
t = np.linspace(-5, 5, 10000)

x = np.exp((-4) * t) * (np.heaviside(t, 0))

y = np.cos(t) * (np.heaviside(t + 2, 0) - np.heaviside(t - 2, 0))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.ylabel('x1(t)')
plt.xlabel('t')
plt.plot(t, x, 'm', )
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.ylabel('x1(t)')
plt.xlabel('t')

plt.plot(t, y, 'm', )
plt.show()
