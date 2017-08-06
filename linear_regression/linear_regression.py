import random
import numpy as np

# Create data
N = 100000
a = 0.856
b = 7.25
x = np.random.uniform(0, 10, N)
noise = np.random.normal(0, 1, N)
y = a*x + b + noise


def gradient_decent_line_filter(x, y):
    def partial_derivative_b(a, b, x, y):
        return np.mean(2 * a * x + 2 * b - 2 * y)

    def partial_derivative_a(a, b, x, y):
        return np.mean((2 * a * x + 2 * b - 2 * y) * x)

    stopping_criteria = 0.0000000000001
    learning_rate = 0.02
    max_iterations = 1000000000

    a = random.random()
    b = random.random()

    for i in xrange(max_iterations):
        old_a = a
        old_b = b
        a += -learning_rate * partial_derivative_a(old_a, old_b, x, y)
        b += -learning_rate * partial_derivative_b(old_a, old_b, x, y)

        if abs(a - old_a) < stopping_criteria and abs(b - old_b) < stopping_criteria:
            break

    return a, b

print gradient_decent_line_filter(x, y)
print a, b
