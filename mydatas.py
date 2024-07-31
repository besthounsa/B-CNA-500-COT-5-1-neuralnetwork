#!/usr/bin/env python3


import numpy as np

import io, os

def get_data(file : io.TextIOWrapper, restant):
    X = []
    Y = [0, 0, 0, 0] # NoirGagne, BlancGagne, Egalite, EchecEtMate
    try:
        while True:
            if (restant < 64):
                break
            tmp = file.readline()
            if tmp == "":
                continue
            if "RES:" in tmp:
                if "0-1" in tmp:
                    Y[0] = 1
                elif "1-0" in tmp:
                    Y[1] = 1
                else:
                    Y[2] = 1
                break
        if Y == [0, 0, 0, 0]:
            return X, Y, False
        tmp = file.readline()
        assert "CHECKMATE:" in tmp
        if "True" in tmp:
            Y[3] = 1
        tmp = file.readline()
        assert "FEN:" in tmp
        tt = [ord(tmp.split()[2])]
        for i in range(9):
            tmp = file.readline()
            for i in tmp[:-1]:
                if i != " ":
                    tt.append(ord(i))
        X = tt
        Y = Y
        
    except Exception as e:
        print(e)
        return [], [], False
    return X, Y, True

#dload
def load_chess(filename, number=-1):
    print("Chargement des donees depuis :", filename)
    outX = []
    outY = []
    remain = True
    file = open(filename, "r")
    total = os.stat(filename).st_size
    i = 0
    while remain:
        restant = file.tell()
        X, Y, remain = get_data(file, total-restant)
        if remain:
            outX.append([X])
            outY.append([Y])
            print(f"{i} donees deja charges... {round((1 - (total-restant)/total)*100, 2)} %\r", end="")
            i = i + 1
        if i == number:
            break
    file.close()
    print("Chargement termine")
    return np.array(outX), np.array(outY)


# load_chess("datasets\\boards\\10_pieces.txt", 20)