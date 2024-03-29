# -*- coding: utf-8 -*-
"""
pytorch.ipynb

Automatically generated by Colaboratory.

"""

# MLP: multilayer perceptron 

import torch.nn as nn
import torch.nn.functional as F

class MultilayerPerceptron(nn.Module):
  def __init__(self, input_dim, hidden_dim, output_dim):
    super(MultilayerPerceptron, self).__init__()
    self.fc1 = nn.Linear(input_dim, hidden_dim)
    self.fc2 = nn.Linear(hidden_dim, output_dim)
  
  def forward(self, x_in, softmax_enable=False):
    output1 = F.relu(self.fc1(x_in))
    output2 = self.fc2(output1)
    if softmax_enable:
      output2 = F.softmax(output2, dim=1)
    return output2


batch_size = 2
input_dim = 3
hidden_dim = 100
output_dim = 4

mlp = MultilayerPerceptron(input_dim, hidden_dim, output_dim)
print(mlp)

def describe(x):
  print("\nType: {}".format(x.type()))
  print("Shape: {}".format(x.shape))
  print("Values: {}".format(x))

x_input = torch.rand(batch_size, input_dim)
describe(input)

y_output = mlp(x_input)
describe(y_output)      # batch_size * output_dim

y_output = mlp(x_input, softmax_enable=True)
describe(y_output)
