#  ht = tanh(Wx*Xt +Wh*ht - 1 + b)

# Xt    Current Input 
# Wx    Weights of curremt input 
# Wh    Weight of previous hidden state
# b     bias
# ht-1  previous hidden state
# tanh  Activation function (-1 to 1) 
# ht    New hidden state

import numpy as np

def Sigmoid(x):
    return 1/(1+np.exp(-x))

def MarvellousRNNPrediction():
    print("Calculations of RNN")

    # food was not good
    inputs = [1,2,5,3]

    hidden_state = 0

    # RNN Paramenters
    Wx = 0.5
    Wh = 0.8
    bias = 0.1

    # RNN Calculations 
    for time_step , x in enumerate(inputs):
        previous_hidden_state = hidden_state

        weighted_input = Wx*x
        Weighted_memory=Wh*previous_hidden_state

        total = weighted_input+Weighted_memory+bias

        hidden_state = np.tanh(total)

        print("TimeStep : ",time_step+1)
        print("Input : ",x)
        print("Hidden State : ",hidden_state)
        print("-"*30)

    # Step 2: Final Hidden State
    print("Final Hidden State : ",hidden_state)

    # Step 3: Output layer 
    # Output = Wy * FinalHiddenState +bias

    Wy = 1.0
    output_bias = 0.0

    output =( Wy * hidden_state )+output_bias

    print("Raw Output :",output)



def main():
    MarvellousRNNPrediction()

if __name__=="__main__":
    main()