import numpy as np
import matplotlib.pyplot as plt

trainingExample = [
(1,1),
(2,3),
(4,3),
]



# defining the function or the predictor:
def fun(x):
  return np.array([1,x])

def weightvec():
  return np.zeros(2) #where the 2 is the dimension of the array wrt the fun(x) 

# now we need to define MSE as a loss function:
def trainLoss(w):
  return 1.0 / len(training example) * sum((w.dot(fun(x)) - y)**2 for x,y in trainingExample)

# now we need to define optimizer function aka gradient for the loss function:
def GradientTrainLoss(w):
  return 1.0 / len(training example) * sum( 2*(w.dot(fun(x)) - y) * fun(x) for x,y in trainingExample)

# Gradient descent Function:
def GradientDescentFun(F, gradientF, weightvec):
  w = weightvec()
  iter = 0.1
  for t in range(500): # 500 is the number of epochs
    value = F(w)
    gradient = gradientF(w)
    w = w - iter * gradient
    print(f'epoch {t}: w ={w}, F(w)= value, gradientF ={gradient}')

GradientDescentFun(trainLoss, GradientTrainLoss, weightvec)
