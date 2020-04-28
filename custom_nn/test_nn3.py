import math
import numpy as np

def sigmoid(t):
    """a step function made continous in order to use calculus (differential)"""
    return 1 / (1 + math.exp(-t)) # t=0 -> 1/2, t=100 -> ~ 1, t=-100 -> ~0

def neuron_output(weights, inputs):
    """reduces all values from input array and weights array to a value between 0 to 1"""
    return sigmoid(np.dot(weights, inputs)) 

def feed_forward(neural_network, input_vector):
    """takes in a neural network
    (represented as a list of lists(non-input layers) of lists(neurons) of weights)
    and returns the output from forward-propagating the input"""
    outputs = []
    # process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector + [1]               # add a bias input
        output = [neuron_output(neuron, input_with_bias)   # compute the output
            for neuron in layer]                           # for each neuron
        outputs.append(output)                             # and remember it
        
        # then the input to the next layer is the output of this one
        input_vector = output
    return outputs

def backpropagate(network, input_vector, targets):
    """
    1. Run feed_forward on an input vector to produce the outputs of all the neurons
    in the network.
    2. This results in an error for each output neuron—the difference between its out‐
    put and its target.
    3. Compute the gradient of this error as a function of the neuron’s weights, and
    adjust its weights in the direction that most decreases the error.
    4. “Propagate” these output errors backward to infer errors for the hidden layer.
    5. Compute the gradients of these errors and adjust the hidden layer’s weights in the
    same manner.
    """
    # We assume a single hidden layer from the network given to feed_forward function
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target)
                     for output, target in zip(outputs, targets)]
    
    # adjust weights for output layer, one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        # focus on the ith output layer neuron
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # adjust the jth weight based on both
            # this neuron's delta and its jth input
            output_neuron[j] -= output_deltas[i] * hidden_output
    # back-propagate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     np.dot(output_deltas, [n[i] for n in output_layer])
                     for i, hidden_output in enumerate(hidden_outputs)]
    # adjust weights for hidden layer, one neuron at a time
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input

import random
from tqdm import tqdm

random.seed(0)   # to get repeatable results
input_size = 50*50  # each input is a vector of length 25 (5x5 "pixels")

num_hidden = 5   # we'll have 5 neurons in the hidden layer
output_size = 10 # we need 10 outputs for each input

# each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for _ in range(input_size + 1)]
                 for _ in range(num_hidden)]
#print(hidden_layer)

# each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for _ in range(num_hidden + 1)]
                 for _ in range(output_size)]
#print(output_layer)

# the network starts out with random weights, one hidden layer and one output layer
network = [hidden_layer, output_layer]


import test_nn2 as tnn

images = tnn.get_images()
inputs = []
for image in images:
    i = []
    for row in image:
        for pixel in row:
            i.append(pixel)
    inputs.append(i)
#print(inputs)

targets = [[0 for j in range(10)] for i in inputs]

print('Training...')

# 10,000 iterations seems enough to converge
def loop(n):
    for input_vector, target_vector in zip(inputs, targets): # inputs is a matrix of 10x25 (ten digits by 25 pixels), target is a one-hot encoded matrix of 10x10 (10 digits by 10 indices where each row has only 1 one and 9 zeroes)
        backpropagate(network, input_vector, target_vector)


from multiprocessing import Pool

def predict(in_put):
    return feed_forward(network, in_put)[-1]

with Pool(4) as p:
      r = list(tqdm(p.imap(loop, range(10000)), total=10000))


images = tnn.get_images2()
inputs2 = []
for image in images:
    i = []
    for row in image:
        for pixel in row:
            i.append(pixel)
    inputs2.append(i)

images = tnn.get_images3()
inputs3 = []
for image in images:
    i = []
    for row in image:
        for pixel in row:
            i.append(pixel)
    inputs3.append(i)



for test_data in inputs3:
    result = predict(test_data)
    result = np.array(result)
    print(result)

