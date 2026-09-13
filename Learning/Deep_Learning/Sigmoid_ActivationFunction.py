import math 
import matplotlib.pyplot as plt 
import numpy as np 

# Sigmoid Activation Function 
def sigmoid(z):
    """Sigmoid function values to (0,1) range."""
    return 1 / (1 + math.exp(-z))
 
# Neuron Calculation 
def Marvellous_neuron_forward(inputs,weights,bias):
    # 1.Display the inputs 
    print("Inputs (X):",inputs)
    print("Weights (w):",weights) 
    print("Bias (b):",bias)

    # 2.Summation z = w*x + b
    # z = np.dot(inputs,weights) + bias 

    z = sum (w * x for w, x in zip (weights,inputs)) + bias
    print("Summation (z = w * x + b):",z) 

    # 3 Activation Function   
    y_hat = sigmoid(z)
    print("Activation Function : Sigmoid")
    print("Output (y = sigmoid(z)):",y_hat)

    return z,y_hat

#---------Plot Sigmoid Function----------
def plot_sigmoid(): 
    z_values = np.linspace(-10,10,200) #range of z values
    sigmoid_values = 1/ (1 + np.exp(-z_values)) 
 
    plt.figure(figsize=(8,5))
    plt.plot(z_values,sigmoid_values,label="Sigmoid",linewidth=2, color="blue")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.title("Sigmoid Activation Function",fontsize=16)
    plt.xlabel("Summation (z)",fontsize=14)
    plt.ylabel("Activation Output",fontsize=14)
    plt.grid(True,linestyle="--",alpha=0.6)
    plt.legend()  
    plt.show()   
 
def main():
    inputs = [1.0,2.0,3.0]   # Example input features 
    weights = [0.6,0.4,-0.2] # weights for each input 

    bias=0.5

    z,y_hat = Marvellous_neuron_forward(inputs,weights,bias)

    # Plot Sigmoid curve
    plot_sigmoid() 

if __name__=="__main__":
    main()  