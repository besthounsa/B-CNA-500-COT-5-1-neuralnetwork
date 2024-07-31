# Documentation of our project MyTorch


![Image about Neural Network project.](./neural.png)
# Neural Network

## Description

Neural Networks is an Epitech project for third year level, which consists to create neural network that can take a chess board as input, and outputs the status of the game using machine-learning-based solution.

## Installation

bash
git clone git@github.com:EpitechPromo2026/B-CNA-500-COT-5-1-neuralnetwork-best.hounsa.git
cd B-CNA-500-COT-5-1-neuralnetwork-best.hounsa
./my_torch ...

## How to test the project : 

**--new : Create a new neuronal network**
**--train: Command for the AI training**  
**--save : Save what the AI have learned in a file, we will use this file continuously to permit to the AI to learn by himself more quicly**


``` ./my_torch --new 65 128 30 4 --train --save test1.best datasets/boards/10_pieces.txt ```

**--predict :Command for prediction from the AI, we will see if the AI have really learned something**

``` ./mytorch --load test1.best --predict predict.txt ```


**If you have any questions, kindly send mail to best.hounsa@epitech.eu and send a copy here jaurio.dansou@epitech.eu**


## Usage

./my_torch [--new IN_LAYER [HIDDEN_LAYERS...] OUT_LAYER | --load LOADFILE] [--train | --predict] [--save SAVEFILE] FILE

| Flags          | Description                                          |
| ---------      | ---------------------------------------------------- |
| --new          | Creates a new neural network with random weights.    |
| --load         | Launches the neural network in training mode         |
| --train        | Integration for data retrieval                       |
| --predict      | Launches the neural network in predictin mode.       |
| --save         | Save neural network internal state into SAVEFILE.    |
| FILE           | File containing chessboards                          |

- new: Creates a new neural network with random weights.
Each subsequent number represent the number of neurons on each layer, from left to right. For example, ./my_torch –new 3 4 5 will create a neural network with an input layer of 3 neurons, a hidden layer of 4 neurons and an output layer of 5 neurons.
- --load: Loads an existing neural network from LOADFILE.
- --train: Launches the neural network in training mode. Each board in FILE must contain inputs to send to the neural network, as well as the expected output.
- --predict: Launches the neural network in predictin mode. Each board in FILE must contain inputs to send to the neural network, and optionally an expected output.
- --save: Save neural network internal state into SAVEFILE.
- FILE: FILE containing chessboards

## License

The [MIT License](https://choosealicense.com/licenses/mit/) is a permissive free software license originating at the Massachusetts Institute of Technology in the late 1980s. As a permissive license, it puts only very limited restriction on reuse and has, therefore, high license compatibility.