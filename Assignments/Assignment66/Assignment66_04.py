import numpy as np

# 1. Define Mean Squared Error
def mean_squared_error(actual, predicted):
    loss = np.mean((actual - predicted) ** 2)
    return loss


# 2. Define Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    epsilon = 1e-7

    # Prevent log(0)
    predicted = np.clip(predicted, epsilon, 1 - epsilon)

    loss = -np.mean(
        actual * np.log(predicted) +
        (1 - actual) * np.log(1 - predicted)
    )

    return loss


# 3. Accept values for MSE (Regression)
print("----- Mean Squared Error -----")

actual_reg = np.array(
    list(map(float, input("Enter actual values: ").split(",")))
)

predicted_reg = np.array(
    list(map(float, input("Enter predicted values: ").split(",")))
)

if actual_reg.shape != predicted_reg.shape:
    raise ValueError("Actual and predicted values must have the same length.")

mse = mean_squared_error(actual_reg, predicted_reg)

print("Mean Squared Error:", mse)


# 4. Accept values for BCE (Binary Classification)
print("\n----- Binary Cross Entropy -----")

actual_cls = np.array(
    list(map(float, input("Enter actual labels (0 or 1): ").split(",")))
)

predicted_cls = np.array(
    list(map(float, input("Enter predicted probabilities (0 to 1): ").split(",")))
)

if actual_cls.shape != predicted_cls.shape:
    raise ValueError("Actual and predicted values must have the same length.")

if not np.all((actual_cls == 0) | (actual_cls == 1)):
    raise ValueError("Actual labels must contain only 0 or 1.")

if not np.all((predicted_cls >= 0) & (predicted_cls <= 1)):
    raise ValueError("Predicted probabilities must be between 0 and 1.")

bce = binary_cross_entropy(actual_cls, predicted_cls)

print("Binary Cross Entropy:", bce)import numpy as np

# 1. Define Mean Squared Error
def mean_squared_error(actual, predicted):
    loss = np.mean((actual - predicted) ** 2)
    return loss


# 2. Define Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    epsilon = 1e-7

    # Prevent log(0)
    predicted = np.clip(predicted, epsilon, 1 - epsilon)

    loss = -np.mean(
        actual * np.log(predicted) +
        (1 - actual) * np.log(1 - predicted)
    )

    return loss


# 3. Accept values for MSE (Regression)
print("----- Mean Squared Error -----")

actual_reg = np.array(
    list(map(float, input("Enter actual values: ").split(",")))
)

predicted_reg = np.array(
    list(map(float, input("Enter predicted values: ").split(",")))
)

if actual_reg.shape != predicted_reg.shape:
    raise ValueError("Actual and predicted values must have the same length.")

mse = mean_squared_error(actual_reg, predicted_reg)

print("Mean Squared Error:", mse)


# 4. Accept values for BCE (Binary Classification)
print("\n----- Binary Cross Entropy -----")

actual_cls = np.array(
    list(map(float, input("Enter actual labels (0 or 1): ").split(",")))
)

predicted_cls = np.array(
    list(map(float, input("Enter predicted probabilities (0 to 1): ").split(",")))
)

if actual_cls.shape != predicted_cls.shape:
    raise ValueError("Actual and predicted values must have the same length.")

if not np.all((actual_cls == 0) | (actual_cls == 1)):
    raise ValueError("Actual labels must contain only 0 or 1.")

if not np.all((predicted_cls >= 0) & (predicted_cls <= 1)):
    raise ValueError("Predicted probabilities must be between 0 and 1.")

bce = binary_cross_entropy(actual_cls, predicted_cls)

print("Binary Cross Entropy:", bce)
