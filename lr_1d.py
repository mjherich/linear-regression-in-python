import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot data to see what it looks like
plt.scatter(X, Y)
plt.show()

# calculate a,b in y_hat=ax+b
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

# calculate y_hat
y_hat = a*X + b

# plot line of best fit
plt.scatter(X, Y)
plt.plot(X, y_hat)
plt.show()

# calculate r-squared
d1 = Y - y_hat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print "the r-squred value is", r2
