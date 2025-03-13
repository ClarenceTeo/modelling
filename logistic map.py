import numpy as np 
import matplotlib.pyplot as plt

def logistic_map(x, y):
	'''a function to calculate the next step of the discrete map.  Inputs
	x and y are transformed to x_next, y_next respectively'''
	y_next = y * x * (1 - y)
	x_next = x + 3/steps
	yield x_next, y_next
steps = 300000000

Y = np.zeros(steps + 1)
X = np.zeros(steps + 1)

X[0], Y[0] = 1, 0.5

# map the equation to array step by step using the logistic_map function above
for i in range(steps):
	x_next, y_next = next(logistic_map(X[i], Y[i])) # calls the logistic_map function on X[i] as x and Y[i] as y
	X[i+1] = x_next
	Y[i+1] = y_next



plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.plot(X, Y, ',', color='white',alpha = 0.2, markersize = 0.2)
plt.xlim(3.5,4)
#plt.ylim(0.8,0.815)
plt.axis('on')
plt.savefig('yeah.png',dpi=1200)
plt.show()

