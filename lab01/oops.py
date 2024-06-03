from sympy import symbols, integrate, sqrt, pi

# Define the variable and function
x = symbols('x')
y = (x**3 / 3) + (1 / (4 * x))
dy_dx = x**2 - 1/(4 * x**2)
integrand = 2 * pi * y * sqrt(1 + dy_dx**2)

# Compute the integral
integral_result = integrate(integrand, (x, 1/2, 2))
print(integral_result)
