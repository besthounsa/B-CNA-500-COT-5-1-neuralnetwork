#!/usr/bin/env python3

import numpy as np
from sys import argv, exit
import pickle
from monreseau import Reseau, Couche
from mydatas import load_chess



def help():
    print("USAGE")
    print("\t./my_torch [--new IN_LAYER [HIDDEN_LAYERS...] OUT_LAYER |--load LOADFILE]")
    print("[--train |--predict] [--save SAVEFILE] FILE")
    print("DESCRIPTION")
    print("\t--new\tCreates a new neural network with random weights.")
    print("Each subsequent number represent the number of neurons on each layer, from left")
    print("to right. For example, ./my_torch–new 3 4 5 will create a neural network with")
    print("an input layer of 3 neurons, a hidden layer of 4 neurons and an output layer of 5 neurons. \n")
    print("\t--load\tLoads an existing neural network from LOADFILE.")
    print("\t--train\tLaunches the neural network in training mode. Each board in FILE")
    print("must contain inputs to send to the neural network, as well as the expected output.")
    print("\t--predict\tLaunches the neural network in predictin mode. Each board in FILE")
    print("must contain inputs to send to the neural network, and optionally an expected")
    print("output.")
    print("\t--save\tSave neural network internal state into SAVEFILE.\n")
    print("\tFILE\tFILE containing chessboards")

def test():
    # help()
    output_size = 4  # NoirGagne, BlancGagne, Egalite, EchecEtMate

    reseau = Reseau()
    reseau.ajouter(Couche(65, 128))
    reseau.ajouter(Couche(128, 64))
    reseau.ajouter(Couche(64, 4))
    x_train, y_train = load_chess("datasets\\boards\\10_pieces.txt", 12)
    reseau.train(x_train, y_train, epochs=2000, learning_rate=0.1)
    predict = reseau.predict(np.array([[[119, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 107, 46, 46, 46, 46, 66, 46, 98, 46, 46, 46, 46, 46, 81, 46, 46, 46, 46, 112, 46, 46, 46, 46, 46, 113, 112, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 75, 46, 46, 46, 46, 46, 46, 46, 46]]]))
    print(predict)

def creer_reseau(layers):
    reseau = Reseau()
    for i in range(len(layers)-1):
        reseau.ajouter(Couche(layers[i], layers[i+1]))
    return reseau

def sauvegarder(reseau, file):
    try:
        open(file, "wb").write(pickle.dumps(reseau))
    except Exception as e:
        print(e)
        exit(0)

def charger(file):
    try:
        tmp = open(file, "rb").read()
        return pickle.loads(tmp)
    except Exception as e:
        print(e)
        exit(0)

def main():
    # Reseau
    reseau = None
    mode = ""
    filename = ""
    dataset = ""
    # Afficher aide
    if len(argv) == 2 and argv[1] == "--help":
        help()
        exit(0)
    
    # Creer un neurone ou charger
    if len(argv) >= 2:
        suite = 0
        # Creer un reseau
        if argv[1] == "--new":
            layers = []
            try:
                i = 2
                while True:
                    if not "--" in argv[i]:
                        layers.append(int(argv[i]))
                        i = i + 1
                    else:
                        break
                suite = i
                assert len(layers) >= 3
                reseau = creer_reseau(layers)
            except:
                print("Argument incorrect pour --new")
                exit(0)
        # Charger un reseau
        elif argv[1] == "--load":
            if len(argv) >= 3:
                reseau = charger(argv[2])
                suite = 3
        
        # Entrainer ou predire
        if len(argv) > suite:
            if argv[suite] == "--train":
                mode = "train"
            elif argv[suite] == "--predict":
                mode = "predict"
            else:
                print("Argument must include --train or --predict")
                exit(0)
            suite = suite + 1
        # Enregistrer ?
        if len(argv) > suite:
            if argv[suite] == "--save":
                try:
                    suite = suite + 1
                    filename = argv[suite]
                    suite = suite + 1
                except:
                    print("Argument --save incorrect")
                    exit(0)
        # Dataset
        if len(argv) > suite:
            dataset = argv[suite]
        
    if dataset != "":
        if mode == "train":
            x_train, y_train = load_chess(dataset)
            reseau.train(x_train, y_train, epochs=2, learning_rate=0.1)
        elif mode == "predict":
            x_train, y_train = load_chess(dataset)
            predict = reseau.predict(x_train)
            print(predict)
    

        if(filename != ""):
            sauvegarder(reseau, filename)
            print("========== MyTorch ===========")
            print("Reseau enregistre a", filename)
            print("==============================")
    else:
        # Erreur
        help()
        exit(0)

if __name__ == "__main__":
    main()