import os
import keras
import pickle
import numpy as np
import tensorflow as tf
import keras.utils as utils
from functools import reduce
import matplotlib.pyplot as plt
from keras import regularizers
from keras import backend as K
from keras.optimizers import Adam
from keras.models import Model, Sequential
from keras.layers import Dense, Input, Activation, Dropout
from keras.layers import Flatten, Reshape, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, UpSampling2D
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D, UpSampling1D
from keras.layers import SimpleRNN, RNN, LSTM, Embedding
from keras.optimizers import Adam, SGD

def get_log(path):
    with open(path, "r") as f:
        text = f.read()
    loss, acc, val_loss, val_acc = list(), list(), list(), list()
    for line in text.strip().split("\n"):
        if "Epoch" in line or len(line) == 0:
            continue
        tokens = [x.strip() for x in line.split("-")]
        loss.append(float(tokens[2][len("loss:"):]))
        acc.append(float(tokens[3][len("acc:"):]))
        val_loss.append(float(tokens[4][len("val_loss:"):]))
        val_acc.append(float(tokens[5][len("val_acc:"):]))

    loss, acc, val_loss, val_acc = np.array(loss), np.array(acc), np.array(val_loss), np.array(val_acc)
    return loss, acc, val_loss, val_acc

###############
#### Utils ####
###############

def load_pkl(path):
    return pickle.load(open(path, "rb"))

def load_data(data):
    keys = ['message_seqs', 'encoded_seqs', 'noisy_seqs', 'viterbi_decoded_seqs']
    x = data[keys[2]] # noisy sequences will be our input to our models
    y = data[keys[0]]
    y_viterbi_decoded = data[keys[3]]
    
    x = np.array(x)
    y = np.array(y)
    y_viterbi_decoded = np.array(y_viterbi_decoded)
    
    return x, y, y_viterbi_decoded

def load(path):
    return load_data(load_pkl(path))

def load_pkl_paths_from_folder(dir_path, recursive=False):
    if recursive:
        return np.sort(list(filter(lambda x: ".pkl" in x,
                            [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(dir_path)) 
                                                 for f in fn])))
    else:
        return np.sort([dir_path + "/" + x for x in os.listdir(dir_path) if ".pkl" in x ])

def get_param_from_filename(filename, param):
    split_token = "_"
    if param == "k":
        split_token = "_k"
    elif param == "p":
        split_token = "_p"
    elif param == "r":
        split_token = "_r"
    elif param == "l":
        split_token = "_l"
    elif param == "e":
        split_token = "_e"
    elif param == "n":
        split_token = "_n"
    else:
        raise ValueError("unrecognized parameter", param)
        
    res = filename.split("/")[-1].split(split_token)[1].split("_")[0]
    if ".pkl" in res:
        res = res.split(".pkl")[0]
    
    return float(res)


#########################
#### Data Processing ####
#########################

def train_test_split(x, y, test_ratio=0.2):
    indicies = np.arange(len(x))
    np.random.shuffle(indicies)
    
    split_inx = int(len(x) * (1-test_ratio))
    X_train, X_test = x[indicies[:split_inx]], x[indicies[split_inx:]]
    y_train, y_test = y[indicies[:split_inx]], y[indicies[split_inx:]]
    
    return X_train, X_test, y_train, y_test

def group_sort(benchmark, *args):
    sorted_indicies = np.argsort(benchmark) 
    
    benchmark = np.array(benchmark)
    args = list(map(lambda x: np.array(x), args))
    
    benchmark_sorted = benchmark[sorted_indicies]
    args_sorted = list(map(lambda x: x[sorted_indicies], args))
    
    return benchmark_sorted, args_sorted

def one_hot(data):
    return utils.np_utils.to_categorical(data)

def one_hot_datasets(y):
    return np.array(list(map(lambda x: one_hot(x), y)))

def onehot_to_normal(dataset):
    return np.argmax(dataset, axis=2)

