import numpy as np
import os

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

if __name__ == '__main__':
    loss, acc, val_loss, val_acc = get_log("tmp.txt")