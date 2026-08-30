import numpy as np
import math

def Sigmoid(z):
    return 1/(1+math.exp(-z))

def main():
    print("-------Marvellous Neural Network------")

    inputs=[1.0,2.0,3.0]
    weights=[0.6,0.4,-0.2]    # this is Random Value
    bias=0.5

    result=Marvellous_Neuron_Forward(inputs,weights,bias)   
    print("Preedicted Result:",result)


def Marvellous_Neuron_Forward(inputs,weights,bias):
    print("inputs are (X):",inputs)
    print("weights are (W):",weights)
    print("bias are (b): ",bias)

    z=0
    for i in range(len(inputs)):
        z=z+(inputs[i]*weights[i])
    z=z+bias

    # z=sum(w*x for w,x in zip(weights,inputs))+bias
    print("Weighted sum:",z)

    y=Sigmoid(z)

    return y


if __name__=="__main__":
    main()
