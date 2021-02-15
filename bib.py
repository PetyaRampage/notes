from numpy import random as rnd
import numpy as np
notes_ = ["C","D","E","F","G","A","B"]


def notes(*args,nrnd = True):

    # нету аргументов, нет рандома
    if       len(args) == 0 and nrnd:
        print("just 7 notes:")
        return notes_

    # нет аргументов, есть рандом
    elif     len(args) == 0 and not nrnd:
        print("7 notes permutation:")
        return rndnotes(())

    # есть аргументы, нету рандома
    elif not len(args) == 0 and nrnd:
        print("selected notes:")
        return select_notes(args)
    # есть и аргументы и рандом
    elif not len(args) == 0 and not nrnd:
        print("random selected notes:")
        return rndnotes(args)
        
    else:
        print("shit")

def rndnotes(tuple): #выбор нот сюда надо пихнуть
    arranged_notes = []
    if len(tuple) == 0:
        b = rnd.permutation(np.arange(1,8))
    else:
        b = rnd.permutation(tuple)
    for i in range(len(b)):
        arranged_notes.append(notes_[b[i]-1])
    return arranged_notes

def select_notes(tuple):
    arranged_notes = []
    for i in tuple:
        arranged_notes.append(notes_[i-1])
    return arranged_notes