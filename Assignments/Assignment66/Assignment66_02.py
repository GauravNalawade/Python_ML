# 2: Write a Python program to demonstrate different activation functions.
# Functions to implement:
# 1. Sigmoid
# 2. ReLU
# 3. Tanh
# Tasks:
# 1. Accept input values from -10 to 10.
# 2. Plot all activation functions using Matplotlib.
# 3. Explain the use of each activation function.


import numpy as np
import matplotlib.pyplot as plt

# 1. Define Activation Functions5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


# 2. Accept User Input Between -10 and 10

while True:
    try:
        value = float(input("Enter a value between -10 and 10: "))

        if -10 <= value <= 10:
            break
        else:
            print("Please enter a value between -10 and 10.")

    except ValueError:
        print("Please enter a valid number.")


# 3. Display Activation Function Outputs

print("\nActivation Function Outputs:")

print("Sigmoid:", sigmoid(value))
print("ReLU   :", relu(value))
print("Tanh   :", tanh(value))


# 4. Generate Input Values for Plotting

x = np.linspace(-10, 10, 400)


# 5. Plot All Activation Functions

plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid(x), label="Sigmoid")
plt.plot(x, relu(x), label="ReLU")
plt.plot(x, tanh(x), label="Tanh")

plt.title("Different Activation Functions")
plt.xlabel("Input Values")
plt.ylabel("Activation Output")

plt.axhline(y=0, color="black", linewidth=0.5)
plt.axvline(x=0, color="black", linewidth=0.5)
 
plt.grid(True)
plt.legend()

plt.show()