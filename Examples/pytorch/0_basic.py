# -*- coding: utf-8 -*-
"""
pytorch.ipynb

Automatically generated by Colaboratory.

"""

import torch.nn as nn
import torch
import matplotlib.pyplot as plt


# Attributes of a Tensor
# =====================
tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# Tensor operations
# =====================

# run on GPU
if torch.cuda.is_available():
  tensor = tensor.to('cuda')

# tensor.add()
# In-place operations: tensor.add_()
t1 = torch.ones(5)
print(t1, "\n")  # tensor([1., 1., 1., 1., 1.]) 

t2 = t1.add(5)
print(t1)        # tensor([1., 1., 1., 1., 1.]) 
print(t2)        # tensor([6., 6., 6., 6., 6.])

t1.add_(5)
print(t1)        # tensor([6., 6., 6., 6., 6.])

# torch.cat
t1 = torch.ones(2,3)
t1[:,1] = 0
t2 = torch.cat([t1, t1], dim=0)
print(t2)
#  tensor([[1., 0., 1.],
#         [1., 0., 1.],
#         [1., 0., 1.],
#         [1., 0., 1.]])

t3 = torch.cat([t1, t1], dim=1)
print(t3)
# tensor([[1., 0., 1., 1., 0., 1.],
#         [1., 0., 1., 1., 0., 1.]])

# torch.stack

# matrix multiplication
t1 = torch.ones(2,2)
y1 = t1 @ t1.T
y2 = t1.matmul(t1.T)
print(y1)
print(y2)

# element-wise product
t1 = torch.ones(2,2)
y1 = t1 * t1.T
y2 = t1.mul(t1.T)
print(y1)
print(y2)

# item()
# Returns the value of this tensor as a standard Python number. 
# This only works for tensors with one element.
# Example: 
#    running_loss += loss.item()

t1 = torch.ones(1,5)
print(t1.sum())         # tensor(5.)
print(t1.sum().item())  # 5.0


# Activation function
# =====================
# torch.nn.ReLU()
# torch tanh()
# torch sigmoid()
# torch.nn.Softmax()

x = torch.range(-5., 5., 0.1)
y1 = torch.sigmoid(x)
y2 = torch.tanh(x)

relu = torch.nn.ReLU()
y3 = relu(x)

plt.plot(x.numpy(), y1.numpy())
plt.plot(x.numpy(), y2.numpy())
plt.plot(x.numpy(), y3.numpy())

# torch.nn.Softmax()
# torch.randn()
# torch.sum()

softmax = nn.Softmax(dim=1)
x = torch.randn(1,3)
y = softmax(x)
print(x)
print(y)
print(torch.sum(y, dim=1))  # sum need to be 1.
print("")

# Loss function
# =====================
# torch.nn.MSELoss()             Normally for regression
# torch.nn.CrossEntropyLoss()    Normally for classification
# torch.tensor()                 Only Tensors of floating point and complex dtype can require gradients

loss_MSE = nn.MSELoss()
outputs = torch.tensor([1.,2.,2.], requires_grad=True)  
targets = torch.tensor([1.,2.,3.])   # mean = 2, MSE = (1/3) * (3-2)^2
print(outputs)
print(targets)
loss = loss_MSE(outputs, targets)
print(loss)
print("")


loss_CE = nn.CrossEntropyLoss()
outputs = torch.randn([2,3], requires_grad=True)
targets = torch.tensor([1,0], dtype=torch.int64)  # need to use int64
print(outputs)
print(targets)
loss = loss_CE(outputs, targets)
print(loss)

# Momentum
# AdaGrad
# Adam -> AdaGrad + Momentum



# Auto Grad
# =====================
# Disabling Gradient Tracking
# Reasons:
# 1)To mark some parameters in your neural network at frozen parameters. 
# 2)To speed up computations when you are only doing forward pass

# Method 1: surrounding computation code 
# with torch.no_grad() block:
x = torch.ones(5)
w = torch.randn(5,3, requires_grad=True)
b = torch.randn(3, requires_grad=True)

z = torch.matmul(x, w)+b
print(z.requires_grad)      # True

with torch.no_grad():
	z = torch.matmul(x, w)+b
print(z.requires_grad)      # False

# Method 2: detach()
z = torch.matmul(x, w)+b
z_det = z.detach()
print(z_det.requires_grad)  # False





