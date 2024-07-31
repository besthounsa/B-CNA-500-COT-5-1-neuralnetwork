#!/usr/bin/env python3


import numpy as np


# Mon Reseau
class Reseau:
    def __init__(self):
        self.layers = []
        self.loss = mse
        self.loss_p = mse_prime

    def ajouter(self, layer):
        self.layers.append(layer)
        self.layers.append(Activation(tanh, tanh_prime))

    def predict(self, input):
        long = len(input)
        out = []

        for i in range(long):
            output = input[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            out.append(output)
        
        if len(out[0][0]) == 4:
            tmp = out[0][0]
            mate = tmp[-1]
            tmp = list(tmp[:-1])
            gagnant = max(tmp)
            if tmp.index(gagnant) == 0:
                gagnant = "0-1"
            elif tmp.index(gagnant) == 1:
                gagnant = "1-0"
            else:
                gagnant = "1/2-1/2"
            if mate >= 0.5:
                mate = "True"
            else:
                mate = "False"
            out_formate = f"""RES: {gagnant}\nCHECKMATE: {mate}"""
            print(out_formate)
            return out
        return out

    def train(self, x_train, y_train, epochs, learning_rate):
        long = len(x_train)
        for i in range(epochs):
            err = 0
            for j in range(long):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)
                err += self.loss(y_train[j], output)
                error = self.loss_p(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)
                print(f"Data Train {j+1}/{long} {round(((j+1)/long)*100,2)} % | epoch {i+1}/{epochs}   erreur={round(err/(j+1), 6)}\r", end="")

            # calculate average error on all samples
            err /= long
            print(f"epoch {i+1}/{epochs}   erreur=%f" % ( err))
            print()



# Une couche
class Couche():
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size):
        self.input = None
        self.output = None
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    # returns output for a given input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    # computes dE/dW, dE/dB for a given output_error=dE/dY. Returns input_error=dE/dX.
    def backward_propagation(self, output_error, learning_rate):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)
        # dBias = output_error

        # update parameters
        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * output_error
        return input_error
    


class Activation():
    def __init__(self, activation, activation_prime):
        self.input = None
        self.output = None
        self.activation = activation
        self.activation_prime = activation_prime

    # returns the activated input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

    # Returns input_error=dE/dX for a given output_error=dE/dY.
    # learning_rate is not used because there is no "learnable" parameters.
    def backward_propagation(self, output_error, learning_rate):
        return self.activation_prime(self.input) * output_error



def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1-np.tanh(x)**2


# Pertes
def mse(y, y_pred):
    return np.mean(np.power(y-y_pred, 2))

def mse_prime(y, y_pred):
    return 2*(y_pred-y)/y.size