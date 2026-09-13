import math 
import matplotlib.pyplot as plt 
import numpy as np 

# ReLU Activation Function 
def relu(z):
    return max(0,z)
 
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
    y_hat = relu(z) 
    print("Activation Function : ReLU")
    print("Output (y = relu(z)):",y_hat)


#---------Plot ReLU Function----------
def plot_relu(): 
    z_values = np.linspace(-10,10,200) #range of z values
    relu_values = np.maximum(0,z_values)
 
    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label="ReLU",linewidth=2, color="green")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.title("ReLU Activation Function",fontsize=16) 
    plt.xlabel("Summation (z)",fontsize=14)
    plt.ylabel("Activation Output",fontsize=14)
    plt.grid(True,linestyle="--",alpha=0.6)
    plt.legend()  
    plt.show()   
 
def main():
    inputs = [1.0,2.0,3.0]   # Example input features 
    weights = [0.6,0.4,-0.2] # weights for each input 

    bias=0.5

    Marvellous_neuron_forward(inputs,weights,bias)

    # Plot Sigmoid curve
    plot_relu() 

if __name__=="__main__":
    main()  