import sympy as sp

# Define the variable and the function
x = sp.symbols("x")
f = x**2

# Calculate the derivativeof the function
derivative = sp.diff(f, x)
print("Derivative of f(x) = x**2:", derivative)