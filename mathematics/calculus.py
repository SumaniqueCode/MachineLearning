import sympy as sp

# Define the variable and the function
x = sp.symbols("x")
f = x**2

# Calculate the derivative of the function
derivative = sp.diff(f, x)
print("Derivative of f(x) = x**2 is ", derivative)

# partial derivative
y, z = sp.symbols("y z")
f= y**2 + 3*z**2 - 4*y*z
grad_y = sp.diff(f, y)
grad_z = sp.diff(f, z)
print("Gradiensts")
print("Partial derivative with respect to y: ", grad_y)
print("Partial derivative with respect to z: ", grad_z)