import torch
import torch.nn as nn
import torch.optim as optim

class DigitRecognizer(nn.Module):

    def __init__(self):   #Class Constructor 
            super(DigitRecognizer, self).__init__()
            input_size = 784   # Because 28x28 pixels

            #Defining Layers and Neurons on each 
            hidden_size1 = 256 # Number of neurons in the first hidden layer.
            hidden_size2= 128 # Number of neurons in the second hidden layer 
            hidden_size3= 64 # Number of neurons in the second hidden layer 
            output_size=10 #Number of outputs(from 0 to 9 )

            #Layers Neurons 
            self.hidden1 = nn.Linear(input_size, hidden_size1)
            self.hidden2 = nn.Linear(hidden_size1, hidden_size2)
            self.hidden3= nn.Linear(hidden_size2, hidden_size3)
            self.output = nn.Linear(hidden_size3, output_size)

            #Activation function: ReLU
            self.relu=nn.ReLU()

                                    #Connecting Layers
    def forward(self, x): #X is the Data 
                    # Original x shape: [batch_size, 1, 28, 28] (batch of 28x28 images)
                    # We reshape it to: [batch_size, 784] (batch of 784-pixel vectors)
                    # view(-1, 784) means "reshape the tensor to have 784 columns and automatically calculate the number of rows".
                    x = x.view(-1, 784)

                    #First Layer
                    # input -> hidden1 -> ReLU
                    x = self.relu(self.hidden1(x))

                    #Second Layer
                    # input -> hidden2 -> ReLU
                    x = self.relu(self.hidden2(x))

                    #Third Layer
                    # input -> hidden2 -> ReLU
                    x = self.relu(self.hidden3(x))

                    #Output Layer
                    # -> output layer
                    x = self.output(x)

                    return x
