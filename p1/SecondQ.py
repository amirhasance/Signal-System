import matplotlib.pyplot as plt
import numpy as np

# x_values = [0,1,2,3,4,5]
# squares = [0,1,4,9,16,25]plt.scatter(x_values,squares, s=10, color = "pink")
# plt.show()

n = [x for x in range(-20, 21, 1)]

y1 = 5 * (np.cos(np.asanyarray(n)) * 3 * np.pi)

plt.bar(n, y1, )
plt.show()

y2 = 5 * np.cos(np.asanyarray(n) * 3)

plt.bar(n, y2, )
plt.show()

y3 = np.power(0.5, np.asanyarray(n)) * (np.heaviside(np.asanyarray(n), 0) - np.heaviside(np.asanyarray(n) - 10, 0))

plt.bar(n, y3, )
plt.show()
