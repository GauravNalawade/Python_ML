import numpy as np

def ReLU(x):
    return max(0,x)

def Marvellous_Neuron_Forward(inputs,weights,bias):

    print("Inputs are : ",inputs)
    print("Weights are : ",weights)
    print("Bias is : ",bias)

    z = 0

    # z = np.dot(inputs,weights) + bias

    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i]) 
    
    z = z + bias 

    print("Weighted sum : ",z)
    
    y = ReLU(z) 
    return y 


def main():

    inputs = [1.0,2.0,3.0]
    
    weights = [0.6,0.4,-0.2]

    bias= 0.5

    result = Marvellous_Neuron_Forward(inputs,weights,bias)

    print("Predicted result is : ",result)


if __name__=="__main__":
    main()