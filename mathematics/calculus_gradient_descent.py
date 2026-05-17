import numpy as np

#define gradient descent function
def gradient_descent(x, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        # calculate the predicted values
        y_pred = np.dot(x, theta)
        # calculate the error
        error = y_pred - y
        # calculate the gradient
        gradient = (1/m) * np.dot(x.T, error)
        # update the parameters
        theta = theta - learning_rate * gradient
    return theta

# sample data
x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(x, np.array([1, 2])) + 3
# initial parameters
theta = np.array([0.1, 0.1])
# perform gradient descent
optimized_theta = gradient_descent(x, y, theta, learning_rate=0.01, iterations=1000)
print("Optimized parameters: ", optimized_theta)
