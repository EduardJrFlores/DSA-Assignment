import numpy as np
import matplotlib.pyplot as plt

# Read values from file
with open("values.txt", "r") as file:
    x = np.array([int(line.strip()) for line in file])

# Define expressions
expressions = {
    1: {'formula': 'x^2 + 7x + 2', 'expression': x**2 + 7*x + 2},
    2: {'formula': '3x + 2', 'expression': 3*x + 2},
    3: {'formula': 'x^2', 'expression': x**2},
    4: {'formula': 'x^3', 'expression': x**3},
    5: {'formula': 'x^5', 'expression': x**5},
    6: {'formula': 'x^3 + 2x^2 + x + 10', 'expression': x**3 + 2*x**2 + x + 10},
    7: {'formula': 'x^4 - 3x^3 + 2x^2 - x + 11', 'expression': x**4 - 3*x**3 + 2*x**2 - x + 11},
    8: {'formula': 'sin(x)', 'expression': np.sin(x)},
    9: {'formula': 'cos(x)', 'expression': np.cos(x)},
    10: {'formula': 'x^5 + 4x^4 + x^3 - 2x^2 + 100', 'expression': x**5 + 4*x**4 + x**3 - 2*x**2 + 100}
}

# Print options
print("Choose an expression to graph:")
for key, expr in expressions.items():
    print(f"{key}. {expr['formula']}")

# Input choice
choice = int(input("Enter your choice (1-11): "))

# Plot and save results
if choice == 11:
    with open("answers.txt", "w") as output_file:
        for key, expr in expressions.items():
            y = expr['expression']
            plt.plot(x, y, label=f'Expression {key}: {expr["formula"]}')
            output_file.write(f"Expression {key}: {expr['formula']}\n")
            output_file.write(np.array2string(y, separator=', ') + '\n\n')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
else:
    y = expressions[choice]['expression']
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title(f"Expression {choice}: {expressions[choice]['formula']}")
    with open("answers.txt", "w") as output_file:
        output_file.write(f"Expression {choice}: {expressions[choice]['formula']}\n")
        output_file.write(np.array2string(y, separator=', ') + '\n\n')
    plt.show()